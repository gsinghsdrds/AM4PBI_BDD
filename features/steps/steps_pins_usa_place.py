from behave import *
from commonfiles.utility import UtilityHelperClass
from selenium.webdriver.common.keys import Keys
use_step_matcher("re")


@given("I select the Analytics menu from the toolbar")
def step_i_select_analytics_toolbar(context):
    context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]").click()

@when("I select the Pins from the Analytics Menu")
def step_driv_time_from_analytics_menu(context):
    context.browser.find_element_by_xpath("//*[contains(text(),'Pins')]").click()
    UtilityHelperClass(context.browser).selenium_wait_interval(0.5)


@when("In the search box, I enter this text - Pizza place in USA")
def step_search_for_text_pizza_place_in_usa(context):
    pin_search_box = context.browser.find_element_by_xpath("//*[contains(@id,'dijit_form_TextBox')]/div/input")
    pin_search_box.send_keys("Pizza place in USA")
    pin_search_box.send_keys(Keys.ENTER)
    UtilityHelperClass(context.browser).wait_interval(0.5)



@then("One Pin will be display on the map area")
def step_pin_display_map_area(context):
    assert context.browser.find_element_by_xpath("//*[starts-with(@id,'dijit__TemplatedMixin')]/div[2]/div/div/div[2]/div[2]").text == "1 locations"
    UtilityHelperClass(context.browser).wait_interval(1)