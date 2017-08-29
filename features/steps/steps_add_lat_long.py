from behave import *
from commonfiles.utility import UtilityHelperClass
use_step_matcher("re")


@given("I have loaded PowerBI and signed in as a free user")
def step_i_loaded_data_powebi(context):
    UtilityHelperClass(context.browser).wait_interval(1)
    """data is already loaded to the mafp"""
    #context.browser.find_element_by_xpath(".//*[@id='pvExplorationHost']/div/div/div/div[1]/div[2]/div/ul/li[1]/button").click()
    pass

@when(u"User drag the latitude field into the Latitude field well")
def step_drag_latitude_field(context):
    context.browser.switch_to.default_content()
    UtilityHelperClass(context.browser).wait_interval(0.5)

    context.browser.find_element_by_xpath("//*[contains(@id,'container')][5]/li/ng-include/label").click()

@when("I drag the longitude field into the Longitude field well")
def step_drag_longitude_field(context):
    context.browser.find_element_by_xpath(".//*[starts-with(@id,'container')][6]/li/ng-include/label").click()
    UtilityHelperClass(context.browser).wait_interval(0.5)
    'Make sure latitude and longitude fields are not summarize'
    context.browser.find_element_by_xpath(
        "//field-well-bucket[@ng-repeat='bucket in viewModel.buckets'][1]//field-well-field[contains(@id,'container')]/li/h2/button[2]").click()
    UtilityHelperClass(context.browser).wait_interval(1)


@when("I will make sure that latitude and longitude fields are not summarized")
def step_fields_not_summarized(context):
    context.browser.find_element_by_xpath(
        "//field-well-bucket[@ng-repeat='bucket in viewModel.buckets'][2]//field-well-field[contains(@id,'container')]/li/h2/button[1]").click()
    UtilityHelperClass(context.browser).wait_interval(0.5)
    dont_summarize_string = '//*[text()="{} summarize"]'.format("Don't")
    context.browser.find_element_by_xpath(dont_summarize_string).click()
    UtilityHelperClass(context.browser).wait_interval(0.5)
    context.browser.find_element_by_xpath(
        "//field-well-bucket[@ng-repeat='bucket in viewModel.buckets'][3]//field-well-field[contains(@id,'container')]/li/h2/button[1]").click()
    UtilityHelperClass(context.browser).wait_interval(0.5)
    context.browser.find_element_by_xpath(dont_summarize_string).click()
    UtilityHelperClass(context.browser).wait_interval(2)


@then("points should appear on the map in the correct lat/long position")
def step_impl(context):
    iframe = context.browser.find_element_by_tag_name('iframe')
    context.browser.switch_to_frame(iframe)
    points = len(context.browser.find_elements_by_xpath(".//*[@id='MyLayer_layer']//*[starts-with(@fill, 'rgb')]"))
    print (points)
    assert points > 590, 'Expected 592 points, but {} points are visible on the map'.format(points)

@when("I go into edit mode")
def step_go_to_edit_mode(context):
    "already map is opened in edit mode"
    pass

@then("the toolbar should not have the Location type button")
def step_toolbar_should_not_have_location_type_button(context):
    if len(context.browser.find_elements_by_xpath("//*[contains(text(),'Location Type')]")) > 0:
        assert 1 > 2, "Location type button is present in the tool bar"












