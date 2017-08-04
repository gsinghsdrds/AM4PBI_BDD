#--------------------------------------------------------------------------------------------------------------
# Name:        add_data.py
# Purpose:     Bring data from Excel, csv files
#----------------------------------------------------------------------------------------------------------------

from commonfiles_error_display import print_error_msg
from utility import UtilityHelperClass


class AddData(object):
    """Add Data to the PowerBI"""
    _navigation_pane    =   "//div[@class='expanderBtn slideFadeIn']//following::i[@class='glyphicon pbi-glyph-globalnavbutton']"

    def __init__(context, browser): 
        context.browser = browser
        
    def adddata_specify_contentlist_url(context):
        try:
            url = 'https://powerbi-df.analysis-df.windows.net/groups//contentlist?approvedResourcesDisabled=true'
            context.browser.get(url)
        except Exception as e:
            print ("Content list url is not accessible: {0}", url)
            print_error_msg(e)
         
         
    def adddata_open_dataset_page(context):
        try:
            'select the Datasets tab on the page'
            #context.browser.find_element_by_xpath("//*[text()='Datasets']").click()
            context.browser.find_element_by_xpath(".//*[@id='contentListLandingContainer']//div[3]/div[1]/div[4]").click()
            UtilityHelperClass(context.browser).wait_interval(2)
        except Exception as e:
           print_error_msg(e)
            
            
    def adddata_enter_datafilename(context, filename):
        try:
            UtilityHelperClass(context.browser).wait_interval(1)
            context.browser.find_element_by_xpath(".//*[@id='contentListLandingContainer']/content-list-container-v2/div/div[2]/div/input").send_keys(filename)
            UtilityHelperClass(context.browser).wait_interval(1)
        except Exception as e:
            print ("Unable to find Dataset File on the server")
            print_error_msg(e)
    
    
    def adddata_open_dataset(context):
        try:
            UtilityHelperClass(context.browser).wait_interval(1)
            context.browser.find_element_by_xpath("//*[@title='Create report'][1]").click()
        except Exception as e:
            print ("Unable to open the Dataset.")
            print_error_msg(e)
    
  
  