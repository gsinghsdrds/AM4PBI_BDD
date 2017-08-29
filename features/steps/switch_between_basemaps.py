from behave import *
from commonfiles.utility import UtilityHelperClass
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")


#Scenario 1 -  Change basemap to streetmap basemap

@given("user visit the Basemap Panel")
def step_impl(context):
    basemapmenu = context.browser.find_element_by_xpath("//*[contains(text(),'Basemap')]")
    context.browser.execute_script("arguments[0].click();", basemapmenu)
    UtilityHelperClass(context.browser).wait_interval(1)

@when("select streetmap basemap from the Basemap Panel")
def step_impl(context):
    backgroundmap = context.browser.find_element_by_xpath("//*[contains(text(),'Streets')]")
    backgroundMapRoot = backgroundmap.find_element_by_xpath("./parent::*").find_element_by_xpath("./parent::*")
    streetsbasemap = backgroundMapRoot.find_element_by_class_name("esriBasemapGalleryThumbnail")
    context.browser.execute_script("arguments[0].click();", streetsbasemap)
    UtilityHelperClass(context.browser).wait_interval(1)

@then("user will see that existing basemap will change to streetmap basemap")
def step_impl(context):
    basemapname = context.browser.find_element_by_xpath("//*[text()='Streets']").text
    assert basemapname == "Streets", "Wrong Basemap Found, Expected Output -  StreetsMap to get open"
    UtilityHelperClass(context.browser).wait_interval(1)


# Scenario 2 - User will change basemap from streetmap to lightcanvas basemap

@given("Basemap panel is open for the user")
def step_impl(context):
    basemapmenu = context.browser.find_element_by_xpath("//*[contains(text(),'Basemap')]")
    context.browser.execute_script("arguments[0].click();", basemapmenu)
    UtilityHelperClass(context.browser).wait_interval(1)

@when("select lightcanvas basemap from the Basemap Panel")
def step_impl(context):
    backgroundmap = context.browser.find_element_by_xpath("//*[contains(text(),'Light Gray Canvas')]")
    backgroundMapRoot = backgroundmap.find_element_by_xpath("./parent::*").find_element_by_xpath("./parent::*")
    lightgraycanvasbasemap = backgroundMapRoot.find_element_by_class_name("esriBasemapGalleryThumbnail")
    context.browser.execute_script("arguments[0].click();", lightgraycanvasbasemap)
    UtilityHelperClass(context.browser).wait_interval(2)


@then("user will see that existing basemap will change to lightcanvas basemap")
def step_impl(context):
    basemapname = context.browser.find_element_by_xpath("//*[text()='Light Gray Canvas']").text
    assert basemapname == "Light Gray Canvas", "Wrong Basemap Found, Expected Output -  Light Gray Canvas Basemap to get open"


#Scenario 3 - User will change basemap from lightcanvas to darkgraycanvas basemap

@when("select darkgraycanvas basemap from the Basemap Panel")
def step_impl(context):
    backgroundmap = context.browser.find_element_by_xpath("//*[contains(text(),'Dark Gray Canvas')]")
    backgroundMapRoot = backgroundmap.find_element_by_xpath("./parent::*").find_element_by_xpath("./parent::*")
    lightgraycanvasbasemap = backgroundMapRoot.find_element_by_class_name("esriBasemapGalleryThumbnail")
    context.browser.execute_script("arguments[0].click();", lightgraycanvasbasemap)
    UtilityHelperClass(context.browser).wait_interval(2)


@then("user will see that existing basemap will change to darkgraycanvas basemap")
def step_impl(context):
    basemapname = context.browser.find_element_by_xpath("//*[text()='Dark Gray Canvas']").text
    assert basemapname == "Dark Gray Canvas", "Wrong Basemap Found, Expected Output -  Dark Gray Canvas Basemap to get open"


@then("user will close the Basemap panel")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@class='esriMapsSidePanelButton esriMapsClose'][@title='Close']").click()





