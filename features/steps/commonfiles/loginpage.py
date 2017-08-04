# --------------------------------------------------------------------------------------------------------------
# Name:        loginpage.py
# Purpose:     This module defines the login class, which handles the PowerBI login 
# Created:     06 May 2016
# Copyright:   (c) Esri 2016
# ----------------------------------------------------------------------------------------------------------------

from configurefileparser import ConfigFileParser
from selenium.common.exceptions import NoSuchElementException
from utility import UtilityHelperClass



class LoginPage(object):
    "Login Class"

    _username_locator = ".//*[@id='cred_userid_inputtext']"
    _password_locator = ".//*[@id='cred_password_inputtext']"
    _signinbutton_locator = ".//*[@id='cred_sign_in_button']"
    _loginclass_locator = ".//*[text()=\'Power BI\']"
    _setting_icon = ".//*[@id=\'settingsMenuBtn\']"
    _navigation_pane = "//div[@class='expanderBtn slideFadeIn']//following::i[@class='glyphicon " \
                       "pbi-glyph-globalnavbutton'] "

    username = ConfigFileParser().powerbiusername()
    password = ConfigFileParser().powerbipassword()

    def __init__(context, browser):
        context.browser = browser

    def setusername(context,username):
        "set user name"
        UtilityHelperClass(context.browser).wait_interval(1)
        context.browser.find_element_by_xpath(context._username_locator).click()
        context.browser.find_element_by_xpath(context._username_locator).send_keys(username)


    def setpassword(context, password):
        "set password"
        context.browser.find_element_by_xpath(context._password_locator).send_keys(password)
    
    def clicklogin(context):
        "Click on the Login Button"
        UtilityHelperClass(context.browser).wait_interval(1)
        context.browser.find_element_by_xpath(context._signinbutton_locator).click()
        
    def getlogintext(context):
        "Extract the PowerBI text on the Page"
        return context.browser.find_element_by_xpath(context._loginclass_locator).text
    
    def is_setting_icon_visible(context):
        "Check whether Setting Icon is visible"
        return context.browser.find_element_by_xpath(context._setting_icon)
    
    def check_navigation_pane_visible(context):
        "Check for Navigation pane is available"
        return context.browser.find_element_by_xpath(context._navigation_pane)

    def login(context):
        "Login method : specify the username and password"
        UtilityHelperClass(context.browser).wait_interval(2)
        try:
            img = context.browser.find_element_by_xpath(".//*[@alt='Work or school account symbol']")
            if (img.is_displayed()):
                context.setpassword(context.password)
        except NoSuchElementException:
            context.setusername(context.username)
            context.setpassword(context.password)
        context.clicklogin()
        #WebbrowserWait(context.browser, 3).until(lambda s: s.find_element_by_xpath(context._loginclass_locator))
        UtilityHelperClass(context.browser).wait_interval(2)
    
    
    
    