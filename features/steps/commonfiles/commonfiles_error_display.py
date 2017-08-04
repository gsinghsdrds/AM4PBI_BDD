# This module is used to display error messages

import os, sys


def print_error_msg(msg):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print("Test file name:", fname, " Test Fail at Line no#:", exc_tb.tb_lineno)
    print (msg)
    sys.exit()