from selenium.webdriver.common.by import By


class UserProfile_Class:

    Text_Email_ID = (By.XPATH, '//*[@id="ap_email"]')
    Text_Password_ID = (By.XPATH, '//*[@id="ap_password"]')
    Continue_Button_Xpath = (By.XPATH,'//*[@id="continue"]')
    SignIn_Button_Xpath = (By.XPATH,'//*[@id="signInSubmit"]')
    SignUp_Button_Xpath = (By.XPATH, '//*[@id="nav-signin-tooltip"]/a/span')
    search_input = (By.ID, "twotabsearchtextbox")
    Error_Message = (By.ID, "auth-error-message-box")



    def __init__(self, driver):
        self.driver = driver

    def Click_SignUp(self):
        self.driver.find_element(*UserProfile_Class.SignUp_Button_Xpath).click()

    def Enter_Email(self, email):
        self.driver.find_element(*UserProfile_Class.Text_Email_ID).send_keys(email)

    def Click_Continue_Button(self):
        self.driver.find_element(*UserProfile_Class.Continue_Button_Xpath).click()

    def Enter_Password(self, password):
        self.driver.find_element(*UserProfile_Class.Text_Password_ID).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(*UserProfile_Class.SignIn_Button_Xpath).click()

    def Validate_Login(self):
        try:
            self.driver.find_element(*UserProfile_Class.search_input)
            return "Login Pass"
        except:
            return "Login Fail"