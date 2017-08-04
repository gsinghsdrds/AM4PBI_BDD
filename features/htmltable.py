# --------------------------------------------------------------------------------------------------------------
# Name:        htmltable.py
# Purpose:     count no# of passed and failed steps. And write passed and failed steps result to html file
# ----------------------------------------------------------------------------------------------------------------

import json, sys

'Read the cucumber json file'
with open('cucumberoutput.json') as json_data:
    readjson = json.load(json_data)

jsonfilelength = len(readjson)
'count number of passed steps'
passsteps = 0
'count number of failed steps'
failsteps = 0
skipsteps = 0
featurenames = []


for jsonln in range(jsonfilelength):
    for elemlen in range(len(readjson[jsonln]['elements'])):
        for stepslen in range(len((readjson[jsonln]['elements'][elemlen]['steps']))):
            if (readjson[jsonln]['elements'][elemlen]['steps'][stepslen]['result']['status'] == "passed"):
                passsteps += 1
            if (readjson[jsonln]['elements'][elemlen]['steps'][stepslen]['result']['status'] == "failed"):
                failsteps += 1
            if (readjson[jsonln]['elements'][elemlen]['steps'][stepslen]['result']['status'] == "skipped"):
                skipsteps += 1

'Storing feature names to featurenames list'
for jsonln in range(jsonfilelength):
    featurenames.append(readjson[jsonln]['name'])


'Write passed and failed steps result to the html file'
f = open('testresulttable.html', 'w')

message = """
<table style="height: 191px; width: 540px;" border="3">
<tbody>
<tr style="height: 69.8px;">
<td style="width: 180px; height: 119.8px;" rowspan="2">&nbsp; &nbsp; Build no# {0}</td>
<td style="width: 179px; background-color: #90ee90; height: 69.8px;">
<p>&nbsp; &nbsp; &nbsp; &nbsp;Total no#</p>
<p>&nbsp; &nbsp; &nbsp;Passed Steps&nbsp;</p>
</td>
<td style="width: 204.6px; background-color: #ffa07a; height: 69.8px;">
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Total no#</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Failed Steps</p>
</td>
<td style="width: 150.4px; height: 69.8px; background-color: #ccccff;">
<p>&nbsp; &nbsp; &nbsp;Total no#</p>
<p>&nbsp; Skipped Steps</p>
</td>
</tr>
<tr style="height: 50px;">
<td style="width: 179px; height: 50px;">&nbsp; &nbsp; &nbsp;{1}</td>
<td style="width: 204.6px; height: 50px;">&nbsp; {2}</td>
<td style="width: 150.4px; height: 50px;">&nbsp; {3}</td>
</tr>
</tbody>
</table>""".format(sys.argv[1], passsteps, failsteps, skipsteps)

f.write(message)
f.close()
