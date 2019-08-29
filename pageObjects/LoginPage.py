class LoginPage():

    #---IDENTIFY LOCATORS OF ALL THE ELEMENTS---

    textbox_username_id = "Email"

    textbox_password_id = "Password"

    button_login_xpath = "//input[@value='Log in']"

    link_logout_linkText = "welcome"

    link_logout_linkText = "Logout"



    #---we need to create CONSTRUCTOR below to Initialize the driver---

    #Here we'll get the "driver" later from Actual TC
    def __init__(self, driver):

        #Once we get the driver, we'll initiate it with local driver
        self.driver = driver


    #And this Constructor automatically Invoke whenever we'll create an Object f
    # for this LOGIN PAGE, so driver is Initiated


    # Then for every Element above we should create an Action Method
    # How to create them? - so we should give them meaningful name


    def setUserName(self, username):

        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)



    def setPassword(self, password):

        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)



    def clickLogIn(self):

        self.driver.find_element_by_xpath(self.button_login_xpath).click()



    def clickLogOut(self):

        self.driver.find_element_by_xpath(self.link_logout_linkText).click()











