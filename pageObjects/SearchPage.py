from selenium.webdriver.common.by import By


class AmazonSearchPage:
    search_box = (By.ID, "twotabsearchtextbox")
    search_button = (By.XPATH, "//input[@value='Go']")
    result_links = (By.CSS_SELECTOR, "a.a-link-normal.a-text-normal")
    no_results_message = (
        By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div/h1/span')

    def __init__(self, driver):
        self.driver = driver

    def Search_Product(self, product):
        self.driver.find_element(*AmazonSearchPage.search_box).click()
        self.driver.find_element(*AmazonSearchPage.search_box).send_keys(product)
        # self.driver.find_element(*AmazonSearchPage.search_box).clear()

    def Validate_Product(self):
        try:
            self.driver.find_element(*AmazonSearchPage.no_results_message)
            return "Here your product"
        finally:
            return "No such product"
