#coding: utf-8
from lib.gui_tests import test_case
import time
from dx_test.dx_test import DXTest
from login_slides_list_page import LoginSlidesListPage
from login_slides_edit_page import LoginSlidesEditPage
from login_slides_show_page import LoginSlidesShowPage
from admin_page import AdminPage
from search.search import SearchPage

class LoginSlidesTest(DXTest):

    @test_case()
    def set_page_objects(self):
        self.login_slides_list_page = LoginSlidesListPage(self.driver.get_browser())
        self.login_slides_edit_page = LoginSlidesEditPage(self.driver.get_browser())
        self.login_slides_show_page = LoginSlidesShowPage(self.driver.get_browser())
        self.search_page = SearchPage(self.driver.get_browser())
        self.admin_page = AdminPage(self.driver.get_browser())

    @test_case()
    def availability_and_functionality_of_login_screen_slides_link(self):
        self.search_page.go_to_link('Admin')
        self.admin_page.wait_till_visible(self.admin_page.login_screen_slides_link[0],
                                          self.admin_page.login_screen_slides_link[1])
        self.admin_page.click_login_screen_slides_link()
        self.login_slides_list_page.wait_till_visible(self.login_slides_list_page.new_login_slides_btn[0],
                                                      self.login_slides_list_page.new_login_slides_btn[1])
        self.login_slides_list_page.page_should_contain("Login Screen Slides")

    @test_case()
    def login_screen_slides_list_page_contents(self):
        for page_contents in self.login_slides_list_page.login_slides_list_page_contents:
            self.login_slides_list_page.page_should_contain(page_contents)
        assert self.login_slides_list_page.is_element_present(self.login_slides_list_page.new_login_slides_btn)

    @test_case()
    def login_screen_slides_edit_page_contents(self):
        self.login_slides_list_page.click_new_login_slides_btn()
        self.login_slides_edit_page.wait_till_visible(self.login_slides_edit_page.create_login_slide_btn[0],
                                                      self.login_slides_edit_page.create_login_slide_btn[1],)
        self.login_slides_edit_page.page_should_contain("New login_screen_slide")
        for elements in self.login_slides_edit_page.login_slides_edit_page_elements:
            assert self.login_slides_edit_page.is_element_present(getattr(self.login_slides_edit_page, elements))

    @test_case()
    def creation_of_new_login_screen_slide(self):
        login_slide_name = 'login-screen-name-' + self.login_slides_edit_page.get_random_string()
        self.login_slides_edit_page.enter_login_slide_name(login_slide_name)
        self.login_slides_edit_page.enter_login_slide_body('login-slide-body-' + self.login_slides_edit_page.get_random_string())
        self.login_slides_edit_page.click_create_login_slide_btn()
        self.login_slides_show_page.wait_till_visible(self.login_slides_show_page.edit_link[0],
                                                      self.login_slides_show_page.edit_link[1])
        self.login_slides_show_page.page_should_contain("Login screen slide was successfully created.")
        self.login_slides_show_page.page_should_contain(login_slide_name)

    @test_case()
    def login_screen_slides_show_page_contents_and_links_functionality(self):
        self.login_slides_show_page.click_back_link()
        self.login_slides_list_page.wait_till_visible(self.login_slides_list_page.new_login_slides_btn[0],
                                                      self.login_slides_list_page.new_login_slides_btn[1])
        self.login_slides_list_page.click_first_login_slide_name()
        self.login_slides_show_page.wait_till_visible(self.login_slides_show_page.edit_link[0],
                                                      self.login_slides_show_page.edit_link[1])
        self.login_slides_show_page.click_edit_link()
        self.login_slides_edit_page.wait_till_visible(self.login_slides_edit_page.create_login_slide_btn[0],
                                                      self.login_slides_edit_page.create_login_slide_btn[1])

    @test_case()
    def updating_existing_login_screen_slide(self):
        login_slide_name = 'login-screen-name-' + self.login_slides_edit_page.get_random_string()
        self.login_slides_edit_page.enter_login_slide_name(login_slide_name)
        self.login_slides_edit_page.click_create_login_slide_btn()
        self.login_slides_show_page.wait_till_visible(self.login_slides_show_page.edit_link[0],
                                                      self.login_slides_show_page.edit_link[1])
        self.login_slides_show_page.page_should_contain("Login screen slide was successfully updated.")
        self.login_slides_show_page.page_should_contain(login_slide_name)

    @test_case()
    def login_screen_slide_with_cancel(self):
        self.availability_and_functionality_of_login_screen_slides_link()
        login_slide_name = self.login_slides_list_page.get_first_login_screen_slide_name()
        self.login_slides_list_page.click_gear_icon()
        self.login_slides_list_page.click_delete_link()
        self.login_slides_list_page.dismiss_alert()
        self.login_slides_list_page.page_should_contain(login_slide_name)

    @test_case()
    def login_screen_slide_with_ok(self):
        login_slide_name = self.login_slides_list_page.get_first_login_screen_slide_name()
        self.login_slides_list_page.click_gear_icon()
        self.login_slides_list_page.click_delete_link()
        self.login_slides_list_page.accept_alert()
        self.login_slides_list_page.wait_till_visible(self.login_slides_list_page.new_login_slides_btn[0],
                                                      self.login_slides_list_page.new_login_slides_btn[1])
        self.login_slides_list_page.page_should_not_contain(login_slide_name)
