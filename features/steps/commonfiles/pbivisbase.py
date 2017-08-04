#--------------------------------------------------------------------------------------------------------------
# Name:        pbivisbase.py
# Purpose:     This module defines the pbivisbase object, this PbiBasePage object will act as parent 
#              object for all the objects in the Test Suite
#              And InvalidPageException class, this class throws the exception when you don't find the correct page
# Created:     27 Aug 2016
# Copyright:   (c) Esri 2016
#----------------------------------------------------------------------------------------------------------------


from abc import abstractmethod

class PbiVisBaseObject(object):
    """ All page objects inherits from this class """
    
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver
    
    @abstractmethod
    def _validate_page(self, driver):
        return
    
    
    """ Regions define functionality available through all 
        pages objects """
    
    @property
    def arcgislayer(self):
        #from lib.arcgislayer import LayerfromArcGIS
        #return LayerfromArcGIS(self.driver)
        pass
    

class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page"""
    pass

class FileNotFoundError(Exception):
    """ Throw this exception when no File Not Found """
    pass
    
    
    
    
    

    
    