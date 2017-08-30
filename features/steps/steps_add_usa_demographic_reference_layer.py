from behave import *
from commonfiles.utility import UtilityHelperClass
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")


@given("I open the Analytics menu from the toolbar")
def step_i_select_analytics_tool_from_toolbar(context):
    UtilityHelperClass(context.browser).wait_interval(1)
    #context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]").click()
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]")).click().perform()

@when("I select the Reference layer from the Analytics menubar")
def step_referencelayer_from_analytics_menu(context):
    context.browser.find_element_by_xpath("//*[contains(text(),'Reference layer')]").click()
    UtilityHelperClass(context.browser).selenium_wait_interval(2)

@when("I select the demographic USA density index reference layer")
def step_select_the_demographic_usa_density_index_reference_layer(context):
    #ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[@id='dojox_mvc_Templated_0']/div/div[2]/div[3]/div/div[3]/div/input")).click().perform()
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//*[contains(@name,'bbf7e47981234e48b958b9344a2e27db')]")).click().perform()
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//div[@class='esriMapsSidePanelButton esriMapsClose'][@title='Close']")).click().perform()
    UtilityHelperClass(context.browser).wait_interval(2)

@then("I see that USA demographic density index reference layer on the map")
def step_usa_density_index_layer_display_on_the_map(context):
    assert context.browser.find_element_by_xpath(".//*[@id='esri.Map_0_gc']/*").get_attribute('data-geometry-type') == "polygon", "No demographic reference layer is display on " \
                                                                     "the map "
