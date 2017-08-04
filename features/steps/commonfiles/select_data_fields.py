# --------------------------------------------------------------------------------------------------------------
# Name:        select_data_fields.py
# Purpose:     add data fields to the Esri Viz
# ----------------------------------------------------------------------------------------------------------------

import time
from commonfiles_error_display import print_error_msg
from utility import UtilityHelperClass


class Select_Fields_EsriViz(object):
    """Add Data to the PowerBI"""

    def __init__(context, browser):
        context.browser = browser

    def add_fields_esri_viz(context):
        """Select First Field in the Esri Viz"""
        try:
            context.browser.find_element_by_xpath(".//*[@title='ArcGIS Maps for Power BI']").click()
            context.browser.find_element_by_xpath(".//*[starts-with(@id,'container')][1]/li/ng-include/label").click()
            UtilityHelperClass(context.browser).wait_interval(10)
        except Exception as e:
            print_error_msg(e)