from selenium.webdriver.support import expected_conditions as EC
from base.dx import Dx
import time

class ReadOnlyPage(Dx):
    def verify_admin_link(self):
        self.go_to_link(self.admin_link)
    
    def verify_dashboard_link(self):
        self.go_to_link(self.dashboard_link)
        time.sleep(2)
        
    def verify_campaign_link(self):
        self.go_to_link(self.campaigns_link)
        time.sleep(2)
        
    def verify_report_link(self):
        self.go_to_link(self.reports_link)
        time.sleep(30)
        
    def verify_creative_link(self):
        self.go_to_link(self.creatives_link)
        time.sleep(2)
        
    def verify_audiences_link(self):
        self.go_to_link(self.audiences_link)
        time.sleep(2)  
        
    def verify_activities_link(self):
        self.go_to_link(self.activities_link)
        time.sleep(5)
        
    def verify_inventory_link(self):
        self.go_to_link(self.inventory_link)
        time.sleep(12)
        
    def verify_agency_group_link(self):
        self.go_to_link(self.agency_group_link)
        time.sleep(2)        
        
    def verify_agencies_link(self):
        self.go_to_link(self.agencies_link)
        time.sleep(2)
        
    def verify_advertiser_link(self):
        self.go_to_link(self.advertiser_link)
        time.sleep(4)
        
    def verify_buisiness_inrelligence_reports(self):
        self.go_to_link(self.buisiness_inrelligence_reports)
        time.sleep(2)
        
    def verify_customer_intelligence_dataset(self):
        self.go_to_link(self.customer_intelligence_dataset)
        time.sleep(2)   
        
    def verify_product_feature(self):
        self.go_to_link(self.product_feature)
        time.sleep(2)
        
    def verify_login_screen_slides(self):
        self.go_to_link(self.login_screen_slides)
        time.sleep(2)
        
    def verify_ad_server_tag_versions(self):
        self.go_to_link(self.ad_server_tag_versions)
        time.sleep(2) 
        
    def verify_edit_my_account_link(self):
        self.go_to_link(self.edit_my_account)
        time.sleep(2)
        
    def verify_subscription_link(self):
        self.go_to_link(self.subscription)
        time.sleep(2)
        
    def verify_report_inbox(self):
        self.go_to_link(self.report_inbox)
        time.sleep(20)
        
    def verify_new_system_message_link(self):
        self.go_to_link(self.new_system_message_link)
        time.sleep(2)
     
    def verify_user_link(self):
        self.go_to_link(self.user_link)
        time.sleep(2)
        
    def verify_create_new_user(self):
        self.go_to_link(self.create_new_user)
        time.sleep(2)
