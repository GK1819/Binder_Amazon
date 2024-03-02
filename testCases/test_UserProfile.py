import random
import string
import time


from pageObjects.UserProfilePage import UserProfile_Class
from testCases.conftest import getDataForLogin
from utilities.readproperties import Readconfig
from utilities.Logger import Logging_Class


class Test_User_Profile:

    LoginUrl = Readconfig.getLoginUrl()
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = Logging_Class.log_generator()


    def test_UserLogin(self, setup):
        self.log.info("test is started")
        self.log.debug("this is debug log")
        self.log.info("this is info log")
        self.log.warning("this is warning log")
        self.log.error("this is error log")
        self.log.critical("this is critical log")
        self.driver = setup
        self.log.info(" Opening Browser")
        self.driver.get(self.LoginUrl)
        self.log.info("Going to Url-->" + self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        self.ur.Click_SignUp()
        self.ur.Enter_Email(self.Email)
        self.log.info("Entering the Email")
        self.ur.Click_Continue_Button()
        self.ur.Enter_Password(self.Password)
        self.log.info("Entering the Password")
        self.ur.Click_LoginButton()
        time.sleep(2)
        if self.ur.Validate_Login() == "Login Pass":
            self.log.info("test is Pass")
            self.driver.save_screenshot(
                "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\Login_Pass.png")
        else:
            self.log.info("test is Fail")
            self.driver.save_screenshot(
                "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\Login_Fail.png")

            self.driver.close()


def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"

