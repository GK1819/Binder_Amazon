import time

from pageObjects.SearchPage import AmazonSearchPage
from pageObjects.UserProfilePage import UserProfile_Class
from pageObjects.CheckoutPage import Checkout_Class, Checkout
from pageObjects.AddProduct import AddProduct_Class
from utilities.readproperties import Readconfig


class Test_VerifyAmount:
    LoginUrl = Readconfig.getLoginUrl()
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    Product_1 = "gym bag"

    def test_VerifyAmount(self, setup):
        self.driver = setup
        self.ur = UserProfile_Class(self.driver)
        self.sp = AmazonSearchPage(self.driver)
        self.Ap = AddProduct_Class(self.driver)
        self.chk = Checkout_Class(self.driver)
        self.ch = Checkout(self.driver)
        self.driver.get(self.LoginUrl)
        self.ur.Click_SignUp()
        self.ur.Enter_Email(self.Email)
        self.ur.Click_Continue_Button()
        self.ur.Enter_Password(self.Password)
        self.ur.Click_LoginButton()
        self.sp.Search_Product(self.Product_1)
        self.chk.Get_Product()
        self.ch.Click_AddToCart()
        self.ch.get_cart_count()
        self.chk.Proceed()
        time.sleep(10)
        self.chk.Payment()
        time.sleep(5)
        self.driver.save_screenshot(
            "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\Final Page.png")

