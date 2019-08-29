import unittest

import HtmlTestRunner

import time

from selenium import webdriver

import sys


#Project Path Declaring
ProjectPath = "//home//elyor//PycharmProjects//"

#Directing to Project path
sys.path.append(ProjectPath)

#Here we'll import "LoginPage" from "pageObjects" package
from pageObjects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    # ---------DECLARING VARIABLES -------------

    chromePath = "/home/elyor/Selenium/chromedriver"


    URL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"

    username = "admin@yourstore.com"

    password = "admin"

    #--------------------------------------------

    #1 Launching Chrome Browser
    driver = webdriver.Chrome(executable_path=chromePath)


    #2. Now I'll Create "setup" Class

    @classmethod
    def setUpClass(cls): # 'cls' is Variable here

        # Get Particular URL
        cls.driver.get(cls.URL)

        cls.driver.maximize_window()

        cls.driver.implicitly_wait(20)



    # Now I'll start Write ACTUAL TEST

    def test_login(self):

        # To call the Method, I'll Create the object of "LoginPage" Class

        #We have declared "CONTRUCTOR" in our class & here we'll pass that Constructor
        # and it'll initiate with driver

        logIn = LoginPage(self.driver)


        #By Using this Object we'll call our Methods

        #1
        logIn.setUserName(self.username)

        time.sleep(5)

        #2
        logIn.setPassword(self.password)

        time.sleep(5)

        #3
        logIn.clickLogIn()

        #4
        time.sleep(5)


        #5 Verify Validation
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "WebPage Title is Not Correct")






    # Here we are closing the test

    @classmethod
    def tearDownClass(cls):

        #cls.driver.close()

        print("Close")




# Finnaly we'll Generate the Report

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..//reports'))





