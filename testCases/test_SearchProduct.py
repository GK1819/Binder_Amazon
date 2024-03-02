
from pageObjects.SearchPage import AmazonSearchPage
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig


class Test_Product:
    LoginUrl = Readconfig.getLoginUrl()
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    Product_Name = "AppleMacBook"
    No_such_Product = "3bhk f"


    def test_product(self, setup):
        self.driver = setup
        self.ur = UserProfile_Class(self.driver)
        self.sp = AmazonSearchPage(self.driver)
        self.driver.get(self.LoginUrl)
        self.ur.Click_SignUp()
        self.ur.Enter_Email(self.Email)
        self.ur.Click_Continue_Button()
        self.ur.Enter_Password(self.Password)
        self.ur.Click_LoginButton()

        self.sp.Search_Product(self.Product_Name)
        self.driver.save_screenshot(
            "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\Product_Result.png")

    def test_No_such_product(self,setup):
        self.driver = setup
        self.ur = UserProfile_Class(self.driver)
        self.sp = AmazonSearchPage(self.driver)
        self.driver.get(self.LoginUrl)
        self.ur.Click_SignUp()
        self.ur.Enter_Email(self.Email)
        self.ur.Click_Continue_Button()
        self.ur.Enter_Password(self.Password)
        self.ur.Click_LoginButton()

        self.sp.Search_Product(self.No_such_Product)
        if self.sp.Validate_Product() == "No such product":
            self.driver.save_screenshot(
                "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\No such product.png")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\Product_result.png")
