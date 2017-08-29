# --------------------------------------------------------------------------------------------------------------
# Name:        switch_to_edit_mode.py
# Purpose:     Move to Infocus Edit mode
# ----------------------------------------------------------------------------------------------------------------

from commonfiles_error_display import print_error_msg
from utility import UtilityHelperClass


class Switch_Edit_Mode(object):
    """Switch to edit infocus mode"""

    def __init__(context, browser):
        context.browser = browser

    def move_to_infocus_edit_mode(context):
        """ Switch to the Edit mode"""
        try:
            context.browser.find_element_by_xpath(".//button[@class='vcMenuBtn']").click()
            context.browser.implicitly_wait(1)
            #context.browser.find_element_by_xpath("//*[text()='Edit']").click()
            'Switch to the Edit mode'
            context.browser.find_element_by_xpath("html/body/div[6]/ul/li[1]/i").click()
            context.browser.implicitly_wait(1)
            #context.browser.switch_to_frame(context.browser.find_element_by_xpath(
            #    ".//iframe[@class='visual-sandbox'][@sandbox='allow-same-origin allow-popups allow-scripts']"))
            'Switch to Esri Viz iframe'
            iframe = context.browser.find_element_by_tag_name('iframe')
            context.browser.switch_to_frame(iframe)
            UtilityHelperClass(context.browser).wait_interval(1)

        except Exception as e:
            print_error_msg(e)

