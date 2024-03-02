

from selenium.webdriver.common.by import By
from pageObjects.AddProduct import AddProduct_Class


class Checkout_Class:
    Add_to_cart = (By.XPATH,"//input[contains(@type,'submit') and (@id='add-to-cart-button')]")
    cart_count = (By.ID, "nav-cart-count")
    delete_item_button = (By.XPATH, "//input[@value='Delete']")
    Go_to_cart= (By.ID, "nav-cart-count")
    Proceed_btn = (By.XPATH, '//input[contains(@type,"submit") and (@name="proceedToRetailCheckout")]')
    Select_Add = (By.XPATH,'//input[contains(@type,"radio") and (@name="submissionURL")]')
    Use_Add_btn = (By.XPATH,'//input[contains(@type,"submit") and (@aria-labelledby="shipToThisAddressButton-announce")]')
    COD_btn = (By.XPATH,"//span[contains(.,'Cash on Delivery/Pay on Delivery')]/parent::label")
    payment_method =(By.XPATH,"//input[contains(@type,'submit') and (@name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent')]")


    def __init__(self, driver):
        self.driver = driver

    def Get_Product(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(
            "https://www.amazon.in/Harissons-Compartment-Detachable-Versatile-Access-Front-Pocket/dp/B07NCYVRMN/ref=sr_1_1?crid=1JAOUASHPODH6&dib=eyJ2IjoiMSJ9.GNQHXdn53hZ2zzie53EPSRa8dvPf-NaxGW4JIfHCN0eD74tcX2nZWf72ireFJKHnHBaF6uWW_qGzv8FSfoFneB1MAwrV8tUV6id-BaXG0X8kEx6dYa4PmX_rL8Z5Ud0SpitBVJRH5EIgoYLvhg_wB9jt7DgEulG8VAa5WYneTmsjlS-g4lligkAeAsRnhIjodIEm_a8FWQXGRjiGG07uMZoPvi9xuKc7bpSr4hUaxTSSoVdAjgLoJ1Quh5cegVzqOXfwRtcPQNJPnJpml9mT2d89rz4J9wBkHiM8eR9tdkQ.h5hwkGjOjzfw8EsPaDycUcRf3LB0DLEDh_59Imyvhhc&dib_tag=se&keywords=gym+bag&qid=1708955284&sprefix=gym+bag%2Caps%2C246&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")



    def Click_AddToCart(self):
        self.driver.find_element(*Checkout_Class.Add_to_cart).click()


    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text


    def Proceed(self):
        self.driver.find_element(*Checkout_Class.Proceed_btn).click()
        self.driver.find_element(*Checkout_Class.Select_Add).click()
        self.driver.find_element(*Checkout_Class.Use_Add_btn).click()


    def Payment(self):
        self.driver.find_element(*Checkout_Class.COD_btn).click()
        self.driver.find_element(*Checkout_Class.payment_method).click()



class Checkout(AddProduct_Class):

    Add_to_cart = AddProduct_Class.Add_to_cart
    cart_count = AddProduct_Class.cart_count

    def __init__(self, driver):
        super().__init__(driver)

    def Click_AddToCart(self):
        self.driver.find_element(*Checkout.Add_to_cart).click()

    def get_cart_count(self):
        return self.driver.find_element(*Checkout.cart_count).text

