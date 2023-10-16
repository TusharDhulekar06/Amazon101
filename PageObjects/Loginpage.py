from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Loginpage():
    lnk_firstpageatt1_xpath="//span[normalize-space()='Account & Lists']"
    lnk_sign_xpath="//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][normalize-space()='Sign in']"

    lnk_clrsignin_xpath="//input[@id='ap_email']"
    lnk_cont_xpath="//input[@id='continue']"
    lnk_passwd_xpath="//input[@id='ap_password']"
    lnk_pwdcont_xpath="//input[@id='signInSubmit']"

    lnk_firstpageatt2_xpath="//span[normalize-space()='Account & Lists']//span[@class='nav-icon nav-arrow']"
    lnk_logout_xpath="//span[normalize-space()='Sign Out']"

    def __init__(self,driver):
        self.driver=driver
    def hover_over_element(self):
        element=self.driver.find_element(By.XPATH,"//span[normalize-space()='Account & Lists']")
        element1=self.driver.find_element(By.XPATH,"//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][normalize-space()='Sign in']")
        action=ActionChains(self.driver)
        action.move_to_element(element).move_to_element(element1).click().perform()
    def clrSignIn(self,email):
        self.driver.find_element(By.XPATH, self.lnk_clrsignin_xpath).clear()
        self.driver.find_element(By.XPATH, self.lnk_clrsignin_xpath).send_keys(email)
    def clkCont(self):
        self.driver.find_element(By.XPATH,self.lnk_cont_xpath).click()
    def clePwd(self,pawd):
        self.driver.find_element(By.XPATH, self.lnk_passwd_xpath).clear()
        self.driver.find_element(By.XPATH, self.lnk_passwd_xpath).send_keys(pawd)
    def clkConPwd(self):
        self.driver.find_element(By.XPATH,self.lnk_pwdcont_xpath).click()
    def hover_over_element1(self):
        element2=self.driver.find_element(By.XPATH,self.lnk_firstpageatt2_xpath)
        act1=ActionChains(self.driver)
        act1.move_to_element(element2).perform()
    def clkLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()






