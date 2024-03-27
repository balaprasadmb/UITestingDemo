from functools import wraps
import sys
import time
from configs.dx_web_driver import DXWebDriver
from screenshot import ScreenshotCapturer


# TODO WITH CLASS(NOT WORKING YET WITH ROBOT FRAMEWORK)
def screenshot_decorator(self, fn):
    def decorator(*args, **kwargs):
        if isinstance(self.driver, DXWebDriver):
            capture = ScreenshotCapturer(self.driver.get_browser())
        else:
            capture = ScreenshotCapturer(self.driver)
        try:
            return fn(*args, **kwargs)
        except AssertionError as e:
            capture.on_test_failure(fn.__name__, None, e)
            tb = sys.exc_info()[2].tb_next
            raise e, None, tb
        except Exception as e:
            capture.on_test_error(fn.__name__, None, e)
            tb = sys.exc_info()[2].tb_next
            raise e, None, tb
        finally:
            pass
    return decorator

def gui_tests(*method_names):
    def class_rebuilder(cls):
        class NewClass(cls):
            def __getattribute__(self, attr_name):
                obj = super(NewClass, self).__getattribute__(attr_name)
                if hasattr(obj, '__call__'):
                        return screenshot_decorator(self, obj)
                return obj

        return NewClass
    return class_rebuilder


# decorator for error stacktrace
class StackTrace(object):
    def __init__(self, with_call=True, with_return=False,
                       with_exception=False, max_depth=3):
        self._frame_dict = {}
        self._options = set()
        self._max_depth = max_depth
        if with_call: self._options.add('call')
        if with_return: self._options.add('return')
        if with_exception: self._options.add('exception')

    def __call__(self, frame, event, arg):
        ret = []
        if event == 'call':
            back_frame = frame.f_back
            if back_frame in self._frame_dict:
                self._frame_dict[frame] = self._frame_dict[back_frame] + 1
            else:
                self._frame_dict[frame] = 0

        depth = self._frame_dict[frame]

        if event in self._options\
          and (self._max_depth<0\
               or depth <= self._max_depth):
            ret.append(frame.f_code.co_name)
            ret.append('[%s]'%event)
            if event == 'return':
                ret.append(arg)
            elif event == 'exception':
                ret.append(repr(arg[0]))
            ret.append('in %s line:%s'%(frame.f_code.co_filename, frame.f_lineno))
        if ret:
            print("%s%s"%('  '*depth, '\t'.join([str(i) for i in ret])))

        return self

#WITH METHOD WORKING FINE
def test_case(tries = 3):
    def wrapper(func):
 
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            self = args[0]
            exception = None
            tb = None
            if isinstance(self.driver, DXWebDriver):
                capture = ScreenshotCapturer(self.driver.get_browser())
            else:
                capture = ScreenshotCapturer(self.driver)
            for _ in range(tries):
                try:
                    st = StackTrace()
                    sys.settrace(st)
                    return func(*args, **kwargs)
                except AssertionError as e:
                    print "Retry, exception: " + str(e)
                    tb = sys.exc_info()[2].tb_next
                    tb
                    exception = e
                except Exception as e:
                    print "Retry, exception: " + str(e)
                    tb = sys.exc_info()[2].tb_next
                    tb
                    exception = e
                finally:
                    sys.settrace(None)
            if exception:
                capture.on_test_error(func.__name__, None, e)
                raise exception
        return wrapped_func

    return wrapper
