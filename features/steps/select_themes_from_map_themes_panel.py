#!/usr/bin/env python
# coding=UTF-8


from behave import *
from commonfiles.utility import UtilityHelperClass
use_step_matcher("parse")


@given(u'Customer opens the Map themes Panel')
def step_customer_opens_map_themes_panel(context):
    mapthemepanel = context.browser.find_element_by_xpath("//*[contains(text(),'Map theme')]")
    context.browser.execute_script("arguments[0].click();", mapthemepanel)
    UtilityHelperClass(context.browser).wait_interval(0.5)

@when(u'Customer go to  {mapthemes} Map theme')
def step_impl(context, mapthemes):
    context.mapthemes = mapthemes
    xpath_elem = "//*[contains(@title,{})]".format(context.mapthemes)
    context.browser.find_element_by_xpath(xpath_elem).click()
    UtilityHelperClass(context.browser).wait_interval(1.5)


@then(u'Customer expects {mapthemes} map theme will open')
def step_impl(context, mapthemes):
    context.mapthemes = mapthemes
    if (context.mapthemes == "Heat Map"):
        elem = context.browser.find_element_by_xpath(".//*[contains(@id,'MyLayer_layer')]")
        assert elem.get_attribute('opacity') == "0.6"

    if (context.mapthemes == "Clustering"):
        assert len(context.browser.find_elements_by_xpath(".//*[starts-with(@fill, 'rgb')]")) == 9

    if (context.mapthemes == "Location Only"):
        elem = context.browser.find_element_by_xpath(".//*[contains(@id,'MyLayer_layer')]")
        assert elem.get_attribute('opacity') == "1"
    UtilityHelperClass(context.browser).wait_interval(0.5)
