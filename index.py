#!/usr/bin/python

import tinyprinter as tp
import cgitb
import cgi

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
print 'CPU-Temperatur (Raspberry Pi): ' + text[:-4] + ' &#176;C'
print "</body>"
print "</html>"
