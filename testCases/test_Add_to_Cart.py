
from pageObjects.SearchPage import AmazonSearchPage
from pageObjects.UserProfilePage import UserProfile_Class
from pageObjects.AddProduct import AddProduct_Class
from utilities.readproperties import Readconfig


class Test_VerifyAmount:
    LoginUrl = Readconfig.getLoginUrl()
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    Product_1 = "iphone 15 pro max"

    def test_Add_to_Cart(self, setup):
        self.driver = setup
        self.ur = UserProfile_Class(self.driver)
        self.sp = AmazonSearchPage(self.driver)
        self.atc = AddProduct_Class(self.driver)
        self.driver.get(self.LoginUrl)
        self.ur.Click_SignUp()
        self.ur.Enter_Email(self.Email)
        self.ur.Click_Continue_Button()
        self.ur.Enter_Password(self.Password)
        self.ur.Click_LoginButton()
        self.sp.Search_Product(self.Product_1)
        self.atc.Get_Product()
        self.atc.Click_AddToCart()
        self.driver.save_screenshot(
            "C:\\Users\\girish kadam\\Desktop\\Binder\\ScreenShots\\Product Added in Cart.png")
        self.atc.get_cart_count()
        self.atc.remove_item_from_cart()

