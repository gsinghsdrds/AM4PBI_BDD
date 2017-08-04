#--------------------------------------------------------------------------------------------------------------
# Name:        add_map_visual.py
# Purpose:     add map visual to the Esri Viz
# Created:     April 2017
# Copyright:   (c) Esri 2017
#----------------------------------------------------------------------------------------------------------------

import os
from commonfiles_error_display import print_error_msg
from configurefileparser import ConfigFileParser
from utility import UtilityHelperClass


class Add_Map_Visual(object):
    """Add Map Visual to the PowerBI"""

    def __init__(context, browser): 
        context.browser = browser
        context.pbixpackage = ConfigFileParser().pbixpackage()
        
    
    def import_from_file(context):
        try:
            UtilityHelperClass(context.browser).wait_interval(2)
            context.browser.find_element_by_xpath(".//*[text()='Import from file']").click()
        except Exception as e:
            print_error_msg(e)


    def import_custom_visual(context):
        try:
            #context.browser.find_element_by_xpath("//*[@title='Import a custom visual']").click()
            UtilityHelperClass(context.browser).wait_interval(2)
            context.browser.find_element_by_xpath("//*[contains(@title,'Import a custom visual')]").click()
        except Exception as e:
            print_error_msg(e)

    def select_import_button(context):
        try:
            UtilityHelperClass(context.browser).wait_interval(1)
            context.browser.find_element_by_xpath("//*[text()='Import']").click()
        except Exception as e:
            print_error_msg(e)
            
            
    def add_pbix_package(context, package):
        try:
            cmd = "C:\\AutoIt3\\Chrome.exe "+package
            #cmd = "C:\\AutoIt3\\esriviz_ff.exe " + package
            os.system(cmd)
            UtilityHelperClass(context.browser).wait_interval(6)
            
        except Exception as e:
            print_error_msg(e)
        
    
    
    
    
    
        
        