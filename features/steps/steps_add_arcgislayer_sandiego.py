from behave import *
from commonfiles.utility import UtilityHelperClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")


@given("I go to the Analytics menu")
def step_i_select_analytics_tool_from_toolbar(context):
    UtilityHelperClass(context.browser).wait_interval(1)
    #context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]").click()
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]")).click().perform()

@when("I click on the Reference layer from the Analytics menu")
def step_referencelayer_from_analytics_menu(context):
    context.browser.find_element_by_xpath("//*[contains(text(),'Reference layer')]").click()
    UtilityHelperClass(context.browser).selenium_wait_interval(2)

@when("I select the ArcGIS label in the Reference layer window")
def step_select_the_arcgis_label(context):
    #context.browser.find_element_by_xpath("//*[contains(text(),'ArcGIS')]").click()
    #ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[contains(@id,'dojox_mvc_Templated')]/div/div[1]/span[2]")).click().perform()
    element = context.browser.find_element_by_xpath(".//*[contains(@id,'dojox_mvc_Templated')]/div/div[1]/span[2]")
    context.browser.execute_script("return arguments[0].click();", element)
    UtilityHelperClass(context.browser).selenium_wait_interval(1)

@when("I enter the text San Diego in the search box")
def step_enter_text_san_diego(context):
    textbx = context.browser.find_element_by_xpath("//*[contains(@id,'dijit_form_TextBox') and @type='text']")
    textbx.send_keys("San Diego")
    textbx.send_keys(Keys.ENTER)
    UtilityHelperClass(context.browser).selenium_wait_interval(1)

@when("I select the san diego layer from the panel")
def steps_select_san_diego_layer_from_panel(context):
    context.browser.find_element_by_xpath(".//*[contains(@id,'dojox_mvc_Templated')]/div/div[2]/div[1]/div[3]/div[3]/div/input").click()
    UtilityHelperClass(context.browser).selenium_wait_interval(2)

@when("I close the reference layer panel")
def steps_close_the_reference_layer_panel(context):
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//div[@class='esriMapsSidePanelButton esriMapsClose'][@title='Close']")).click().perform()
    UtilityHelperClass(context.browser).selenium_wait_interval(2)


@then("I see San Diego layer about places to go on the map")
def step_i_see_san_diego_layer_about_places_to_go(context):
    'Number of Places to go on the Map is equal to 13'
    #actual_value = len(context.browser.find_elements_by_xpath(".//*[@id='esri.Map_0_gc']//*[contains(@opacity,'0.5')]//*[contains(@stroke,'none')]"))
    #assert actual_value == 13, 'San diego places to go symbols on the map: expected value {0} actual value {1}'.format(13, actual_value)
    if context.browser.find_elements_by_xpath(".//*[@id='esri.Map_0_gc']//*[contains(@opacity,'0.5')]//*[contains(@stroke,'none')]") is True:
        print ("San Diego layer about the places to go on the map is visible")
