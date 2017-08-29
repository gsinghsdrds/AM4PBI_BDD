#!/usr/bin/env python
# -*- coding: utf-8 -*-

"Program starts from environment.py file"
import sys, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from steps.commonfiles import add_data, add_map_visual, select_data_fields
from steps.commonfiles import switch_to_edit_mode
from steps.commonfiles.loginpage import LoginPage
from steps import add_dataset_import_custom_visual
from selenium.webdriver.common.action_chains import ActionChains



#Global values
dataseturl = "https://powerbi-df.analysis-df.windows.net/groups/me/contentlist/datasets?approvedResourcesDisabled=true"


def before_all(context):
     print("Executing before all")

     # Assign Buildnum path to package variable
     package = context.config.userdata['buildnum']
     print ("Package Path:", package)

     # If no package path is specified, then exit the program
     if not package:
          sys.exit(2)

     with open("package.cfg", 'w') as f:
         f.write(package)

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


def before_feature(context, feature):
    """ Create a drive time and radius around a location in USA"""

    #Read the package name
    with open("package.cfg") as f:
        packageurl= f.readlines()

    if (feature.name == 'create a drive time and radius around a location in USA'):
        context.browser.switch_to.default_content()
        #context.browser.switch_to.default_content()
        context.browser.find_element_by_xpath("//*[contains(@title,'Get Data')]").click()
        #context.browser.find_element_by_xpath("html/body/div[2]/div/div/div/div[4]/input[2]").click()
        ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//*[@class='infonav-modalContainerHost']/div/div/div/div[4]/input[2]")).click().perform()
        context.browser.implicitly_wait(1)
        context.browser.get(dataseturl)
        context.browser.implicitly_wait(1)
        add_data.AddData(context.browser).adddata_enter_datafilename("USA_Cities")
        add_dataset_import_custom_visual.AddDataFileImportCustomVisual(context.browser).add_datafile_loadesriviz(packageurl[0])


#     print("Before feature\n")
#Scenario level objects are popped off context when scenario exits
#def before_scenario(context,scenario):
#    print("Before scenario\n")
#def after_scenario(context,scenario):
#    print("After scenario\n")



def after_feature(context,feature):
    print("\nAfter feature")
    context.browser.implicitly_wait(1)
    #Read the package name
    with open("package.cfg") as f:
        packageurl = f.readlines()

    if (feature.name == 'create a drive time and radius around a location in USA'):
        context.browser.switch_to.default_content()
        context.browser.find_element_by_xpath("//*[contains(@title,'Get Data')]").click()
        ActionChains(context.browser).move_to_element(context.browser.find_element_by_xpath("//*[@class='infonav-modalContainerHost']/div/div/div/div[4]/input[2]")).click().perform()
        context.browser.implicitly_wait(1)
        context.browser.get(dataseturl)
        context.browser.implicitly_wait(1)
        add_data.AddData(context.browser).adddata_enter_datafilename("sample customer data")
        add_dataset_import_custom_visual.AddDataFileImportCustomVisual(context.browser).add_datafile_loadesriviz(packageurl[0])



