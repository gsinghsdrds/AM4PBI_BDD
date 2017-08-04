#--------------------------------------------------------------------------------------------------------------
# Name:        utility.py
# Purpose:     Call selenium and helper methods
#----------------------------------------------------------------------------------------------------------------
import time

class UtilityHelperClass(object):
    """call selenium and helper method from this call"""

    def __init__(context, browser):
        context.browser = browser

    def selenium_wait_interval(context, waittime):
        "Wait for Waittime period, time is in seconds"
        context.browser.implicitly_wait(waittime)

    def wait_interval(context, waittime):
        time.sleep(waittime)