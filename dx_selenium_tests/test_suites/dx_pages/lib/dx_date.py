from datetime import timedelta
from datetime import datetime

class DXDate(object):
    def date_after_two_days(self):
        return ((datetime.today()+timedelta(days=2)).strftime('%m/%d/%Y'))

    def last_date_of_current_month(self):
        return ((datetime.today()+timedelta(days=28)).strftime('%m/%d/%Y'))

    def date_before_three_days(self):
        return ((datetime.today()+timedelta(days=-3)).strftime('%m/%d/%Y'))

    def date_before_two_days(self):
        return ((datetime.today()+timedelta(days=-2)).strftime('%m/%d/%Y'))

    def todays_date(self):
        return ((datetime.today().strftime('%m/%d/%Y')))
    
    def date_after_one_month(self):
        return ((datetime.today() + relativedelta(months=1)).strftime('%m/%d/%Y'))
    
    def get_formated_date(self, format):
        return (datetime.today().strftime(format))
