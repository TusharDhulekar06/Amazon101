from PageObjects.Loginpage import Loginpage
from Utilities.customLogger import Loggen
from Utilities.readProperties import ReadConfig
class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    logger=Loggen.loggen()

    def test_account_reg(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp=Loginpage(self.driver)

        self.lp.hover_over_element()

        self.lp.clrSignIn("cfptushardhulekar@gmail.com")
        self.lp.clkCont()

        self.lp.clePwd("08Megha@12")
        self.lp.clkConPwd()

        self.lp.hover_over_element1()
        self.lp.clkLogout()
        self.driver.close()





