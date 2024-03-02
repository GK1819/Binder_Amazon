
from selenium.webdriver.common.by import By


class AddProduct_Class:
    Add_to_cart = (By.XPATH,'//input[contains(@type,"submit") and (@id="add-to-cart-button")]')
    cart_count = (By.ID, "nav-cart-count")

    delete_item_button = (By.XPATH, "//input[@value='Delete']")
    Go_to_cart= (By.ID, "nav-cart-count")


    def __init__(self, driver):
        self.driver = driver

    def Get_Product(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(
            "https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHWV2WYK/ref=sr_1_1?crid=3UGOP3CYMF1PM&dib=eyJ2IjoiMSJ9.5Hp02l3KCumhkK8HtcxB3Z-rXboAEYdt4Uex3iyv0QcyEobsazBeJAB0TQVYsJg9TZrgNnEk9f3D1QHDuStSpo8znV0y8KjA7JKzNl-lJ3nhh744U9kbG6v0PKTKRFsRWOiGZNHPYKSueABbbD00IoihoGCnqA0MH9-bodISpgpyPizAPMTVlHnBNytxm_-CDPxiTwc_Nxaq80S27AZ21ZXdq0vk14KTtIQbE92xFtc.CEsQQD0Lm8t3ORuaSBDxCeDS-_x7CEYgmHpLami6qgQ&dib_tag=se&keywords=iphone+15+pro+max&qid=1708697266&sprefix=iphone+15+pro+ma%2Caps%2C217&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
        self.driver.find_element(*AddProduct_Class.Add_to_cart).click()


    def Click_AddToCart(self):
        self.driver.find_element(*AddProduct_Class.Add_to_cart).click()


    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text


    def remove_item_from_cart(self):
        self.driver.find_element(*AddProduct_Class.Go_to_cart).click()
        self.driver.find_element(*AddProduct_Class.delete_item_button).click()
