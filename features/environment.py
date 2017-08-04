#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Program starts from environment.py file"

import time
from steps.commonfiles import add_data, add_map_visual, select_data_fields
from steps.commonfiles.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from steps.commonfiles import switch_to_edit_mode

packname = "abc"

def before_all(context):
     print("Executing before all")
     #try:
     #   context.config.userdata['buildnum']
     #except KeyError:
     #    context.config.userdata['buildnum'] = r"\\devtfs2012la\PowerBIPackages\freelunch.esri.com\powerbi\1.0.98.884"
     #    pass

     # Assign Buildnum path to package variable
     package = context.config.userdata['buildnum']
     print ("Package Path:", package)

     #if not package:
     #    sys.exit()

     # Initiate Selenium Web Driver
     context.browser = webdriver.Chrome()
     context.browser.maximize_window()

     # navigate to the application home page
     context.browser.get('https://powerbi-df.analysis-df.windows.net?approvedResourcesDisabled=true')
     WebDriverWait(context.browser, 10).until(lambda s: s.find_element_by_xpath(".//*[text()='Microsoft Power BI']"))
     LoginPage(context.browser).login()

     'Add dataset to the PBI'
     add_data.AddData(context.browser).adddata_specify_contentlist_url()
     add_data.AddData(context.browser).adddata_open_dataset_page()
     add_data.AddData(context.browser).adddata_enter_datafilename("sample customer data")
     add_data.AddData(context.browser).adddata_open_dataset()

     'Add Map Visual to the Esri Viz'
     add_map_visual.Add_Map_Visual(context.browser).import_custom_visual()
     add_map_visual.Add_Map_Visual(context.browser).import_from_file()
     add_map_visual.Add_Map_Visual(context.browser).select_import_button()

     'Reading PBIX package from command line argument'
     add_map_visual.Add_Map_Visual(context.browser).add_pbix_package(package)

     'Select Fields into Esri Viz'
     select_data_fields.Select_Fields_EsriViz(context.browser).add_fields_esri_viz()

     'Switch to Infocus Edit Mode'
     switch_to_edit_mode.Switch_Edit_Mode(context.browser).move_to_infocus_edit_mode()
     context.browser.implicitly_wait(1)


def after_all(context):
    context.browser.quit()
    print("Executing after all")


#def before_feature(context, feature):
#     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
#def before_scenario(context,scenario):

#    print("Before scenario\n")

#def after_scenario(context,scenario):
#    print("After scenario\n")

#def after_feature(context,feature):
#    print("\nAfter feature")



