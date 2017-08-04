#--------------------------------------------------------------------------------------------------------------
# Name:        configurefileparser.py
# Purpose:     This module deals with the configuration file parsing
# Created:     30 Aug 2016
# Copyright:   (c) Esri 2016
#----------------------------------------------------------------------------------------------------------------


import ConfigParser
from pbivisbase import FileNotFoundError


class ConfigFileParser():
    """ Parse the Configuration File """
    
    filename = "config.ini"
    
    def __init__(context):
        context.config = ConfigParser.ConfigParser()

    def fileparser(context):
        try:
            context.config.read(context.filename)
        
        except IOError, err:
            print "Problem opening configuration file. %s" %err
        
        except ConfigParser.ParsingError:
            print "Cannot parse configuration file!"
        
        except:
            raise FileNotFoundError("File not Found: {}".format(context.filename))
        
            
    def powerbiusername(context):
        context.fileparser()
        return context.config.get('PowerBI', 'username')
    
    def powerbipassword(context):
        context.fileparser()
        return context.config.get('PowerBI', 'password')
    
    def pbixpackage(context):
        context.fileparser()
        return context.config.get('PowerBI', 'package')
    
    



