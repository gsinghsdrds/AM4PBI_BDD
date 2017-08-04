#--------------------------------------------------------------------------------------------------------------
#!/usr/bin/env python
# coding=UTF-8
# Purpose : This module selects dataset in PBI, import custom Esri Visual and Switch to Edit mode
#--------------------------------------------------------------------------------------------------------------

from commonfiles import add_data, add_map_visual, switch_to_edit_mode
from commonfiles.commonfiles_error_display import print_error_msg


class AddDataFileImportCustomVisual(object):
    """ Add data to PowerBI, Import Custom Esri Visual and Switch to edit mode"""
    def __init__(context, browser):
        context.browser = browser


    def add_datafile_esri_map_visual_switch_edit_mode(context, filename):
        try:
            'Add dataset to the PBI'
            add_data.AddData(context.browser).adddata_specify_contentlist_url()
            add_data.AddData(context.browser).adddata_open_dataset_page()
            add_data.AddData(context.browser).adddata_enter_datafilename(filename)
            add_data.AddData(context.browser).adddata_open_dataset()

            'Add Map Visual to the Esri Viz'
            add_map_visual.Add_Map_Visual(context.browser).import_custom_visual()
            add_map_visual.Add_Map_Visual(context.browser).import_from_file()
            add_map_visual.Add_Map_Visual(context.browser).select_import_button()

            'Reading PBIX package from command line argument'
            #add_map_visual.Add_Map_Visual(context.browser).add_pbix_package(context.pkname)

            'Switch to Infocus Edit Mode'
            switch_to_edit_mode.Switch_Edit_Mode(context.browser).move_to_infocus_edit_mode()
            context.browser.implicitly_wait(1)

        except Exception as e:
            print_error_msg(e)




