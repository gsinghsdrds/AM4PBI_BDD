#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------------------------------------------
# Name:        convert_behave_json_cucumber..py
# Purpose:     convert the behave python generated json file into the cucumber style json file format
# ----------------------------------------------------------------------------------------------------------------

import json
import behave2cucumber
import io

with open('resultoutput.json') as behave_json:
    cucumber_json = behave2cucumber.convert(json.load(behave_json))

outfile = "cucumberoutput.json"
with open(outfile, 'w') as f:
    json.dump(cucumber_json, f, indent=4, separators=(',', ': '))


