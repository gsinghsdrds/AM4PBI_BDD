from behave import *
from commonfiles.utility import UtilityHelperClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



use_step_matcher("parse")


@given("I load the USA_Cities dataset to the Esri Viz")
def step_i_select_analytics_toolbar(context):
    UtilityHelperClass(context.browser).wait_interval(1)
    print ("USA_Cities data is loaded")


@when("I select a single city feature point on the map")
def step_i_select_single_city_feature_on_the_map(context):
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[@id='MyLayer_layer']//*[starts-with(@fill, 'rgb')][1]")).click().perform()
    UtilityHelperClass(context.browser).selenium_wait_interval(0.5)


@when("Click on the Analytics in the ToolBar")
def step_click_on_analytics_toolbar(context):
    ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath(".//*[starts-with(@id, 'uniqName')][2]/div/span/span[1]")).click().perform()
    UtilityHelperClass(context.browser).selenium_wait_interval(0.5)


@when("Click on Analytcs menu from the Maps for PowerBI toolbar")
def step_i_select_drive_time_from_analyticsmenu_map(context):
    elem = context.browser.find_element_by_xpath("//*[contains(text(),'Drive time')]")
    context.browser.execute_script("return arguments[0].click();", elem)
    UtilityHelperClass(context.browser).selenium_wait_interval(1)


@when(u'I created {drivetimetype} of {mins} minutes around a location in USA')
def step_i_createtimetype_of_mins(context, drivetimetype, mins):
    context.drivetimetype = drivetimetype
    context.mins = mins
    textbx = context.browser.find_element_by_xpath("//*[contains(@id,'dijit_form_TextBox') and @type='text']")
    #ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//div[@class='distanceParams']/div/div/input")).send_keys(Keys.CONTROL + "a").send_keys(Keys.DELETE).send_keys(context.mins).send_keys(Keys.ENTER)
    textbx.send_keys(Keys.CONTROL + "a")
    textbx.send_keys(Keys.DELETE)
    textbx.send_keys(context.mins)
    textbx.send_keys(Keys.ENTER)

    if (context.drivetimetype == 'Radius'):
        # select Radius from the drop down menu
        #ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//div[@class='studyAreasOptions']/table/tbody/tr/td[2]/input")).click().perform()
        context.browser.find_element_by_xpath("//div[@class='studyAreasOptions']/table/tbody/tr/td[1]").click()
        UtilityHelperClass(context.browser).selenium_wait_interval(1)
        context.browser.find_element_by_xpath(".//*[@class='dijitReset dijitMenuItemLabel'][text()='Radius']").click()
        UtilityHelperClass(context.browser).selenium_wait_interval(1)

    context.browser.find_element_by_xpath("//*[contains(text(),'OK')]").click()
    UtilityHelperClass(context.browser).selenium_wait_interval(1)



@then(u'I will see {drivetimetype} of {mins} minutes on the map')
def step_i_see_drivetimetype_of_mins_on_the_map(context, drivetimetype, mins):
    context.drivetimetype = drivetimetype
    context.mins = mins
    if (context.drivetimetype == 'Radius' and context.mins == '10'):
        print ("Radius:", context.browser.find_element_by_xpath("//div[@class='bufferResultSummary']/div[2]/div").text)
        assert context.browser.find_element_by_xpath("//div[@class='bufferResultSummary']/div[2]/div").text == "10 miles Radius"

    if (context.drivetimetype == 'Drive time' and context.mins == '10'):
        if ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//*[contains(text(),'10 minutes Drive time')]")).perform() is True:
            print ("10 minutes Drive time is visible on the map ")

    if (context.drivetimetype == 'Radius' and context.mins == '30'):
        print ("Radius:", context.browser.find_element_by_xpath("//div[@class='bufferResultSummary']/div[2]/div").text)
        assert context.browser.find_element_by_xpath("//div[@class='bufferResultSummary']/div[2]/div").text == "30 miles Radius"

    if (context.drivetimetype == 'Drive time' and context.mins == '30'):
        if ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//*[contains(text(),'30 minutes Drive time')]")).perform() is True:
            UtilityHelperClass(context.browser).selenium_wait_interval(5)
            print ("30 minutes Drive time is visible on the map ")

    if (context.drivetimetype == 'Drive time' and context.mins == '31'):
        if context.browser.find_element_by_xpath("//*[contains(text(),'Maximum value supported is 30 minutes')]") is True:
            print ("No drive time areas on the map")

    if (context.drivetimetype == 'Radius' and context.mins == '101'):
        if context.browser.find_element_by_xpath("//*[contains(text(),'Maximum value supported is 100 miles')]") is True:
            print ("No drive time areas on the map")

    if (context.drivetimetype == 'Radius' and context.mins == '-10'):
        if context.browser.find_element_by_xpath("//*[contains(text(),'Invalid distance value')]") is True:
            print ("Invalid distance value -10 Radius")

    if (context.drivetimetype == 'Drive time' and context.mins == '-10'):
        if context.browser.find_element_by_xpath("//*[contains(text(),'Invalid distance value')]") is True:
            print ("Invalid distance value - 10 Drive time")

    if (context.drivetimetype == 'Radius' and context.mins == '*$@'):
        if context.browser.find_element_by_xpath("//*[contains(text(),'Invalid distance value')]") is True:
            print ("Invalid distance value - *$@ Radius")

    if (context.drivetimetype == 'Drive time' and context.mins == '#&@'):
        if context.browser.find_element_by_xpath("//*[contains(text(),'Invalid distance value')]") is True:
            print ("Invalid distance value - #&@ Drive time")

    UtilityHelperClass(context.browser).wait_interval(1)


@then(u'zoom to extent and close the drive time panel of {mins} minutes')
def step_zoom_to_extent_close_the_panel(context, mins):
    context.mins = mins
    UtilityHelperClass(context.browser).wait_interval(1)

    if (context.mins == '31' or context.mins == '101' or context.mins == '*$@' or context.mins == '#&@' or context.mins == '-10'):
        context.browser.find_element_by_xpath("//div[@class='esriMapsSidePanelButton esriMapsClose'][@title='Close']").click()
        UtilityHelperClass(context.browser).wait_interval(1)
        return

    context.browser.find_element_by_xpath("//*[text()='Remove drive time areas']").click()
    UtilityHelperClass(context.browser).wait_interval(0.5)
    for i in range(0, 3):
        context.browser.find_element_by_xpath(".//*[@id='esri.Map_0_zoom_slider']/div[2]").click()

    context.browser.find_element_by_xpath(
        "//div[@class='esriMapsSidePanelButton esriMapsClose'][@title='Close']").click()
    UtilityHelperClass(context.browser).wait_interval(1)
