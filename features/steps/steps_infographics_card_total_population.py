from behave import *
from commonfiles.utility import UtilityHelperClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")


@given("Customer goes to the Analytics menu")
def step_i_select_analytics_toolbar(context):
    UtilityHelperClass(context.browser).wait_interval(1)
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]")).click().perform()

@when("Customer selects Infographics from the Analytics menu")
def step_driv_time_from_analytics_menu(context):
    context.browser.find_element_by_xpath("//*[contains(text(),'Infographics')]").click()
    UtilityHelperClass(context.browser).selenium_wait_interval(1)


@when("Customer selects the total population inforgraphics card")
def step_search_for_text_pizza_place_in_usa(context):
    #ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//div[@class='demographicsPanel']/div[1]/div[2]/div[1]/div/input")).click().perform()
    element = context.browser.find_element_by_xpath("//div[@class='demographicsPanel']/div[1]/div[2]/div[1]/div/input")
    context.browser.execute_script("return arguments[0].click();", element)
    UtilityHelperClass(context.browser).wait_interval(1)


@then("Customer will see total population infographics card will appear")
def step_pin_display_map_area(context):
    if ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//div[@class='infographicsVariableGroup']/table/tbody/tr/td[1]/div[1]/span")) is True:
        print ("USA Total Population Card is Visible ")
    UtilityHelperClass(context.browser).wait_interval(1)