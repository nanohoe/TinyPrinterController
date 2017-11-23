#!/usr/bin/python

import tinyprinter as tp
import ihingerhof as ih
import cgitb
import cgi
import w1temp

cgitb.enable()

tp.init()

try:
    args = cgi.FieldStorage()
    action = args["action"].value
except:
    action = "none"

if action == "on":
    tp.switchOn()
if action == "off":
    tp.switchOff()

with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
    text = f.read()

print "Content-type: text/html"
print

print "<html>"
print "<head>"
print '<title>Drucker</title>'
print '<meta name="viewport" content="width=device-width"'
print "</head>"
print "<body>"
print "<h1>Officejet 6000</h1>"
print "<p>"
if tp.getState():
    print "Drucker ist an."
else:
    print "Drucker ist aus."
print "</p>"
print '<p><a href="index.py?action=on">Einschalten</a>&nbsp;<a href="index.py?action=off">Ausschalten</a></p>'
print '<p>Raspberry: ' + text[:-4] + ' &#176;C</p>'
print '<p>Schlafzimmer: ' + '{:.1f}'.format(float(w1temp.printstring())) + ' &#176;C</p>'
tempdata = ih.gettemp('/home/hoe/ih')
print '<p>Ihinger Hof: ' + tempdata[1] + ' &#176;C (gemessen ' + tempdata[0] + ')</p>'
print "</body>"
print "</html>"
