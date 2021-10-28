#!/usr/bin/python37all

import json
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
slider_position = form.getvalue("slider")
check_clicked = form.getvalue("zero")

data = {"slider":slider_position, "zero":check_clicked}
with open('selected_led.txt', 'w') as f:
  json.dump(data,f)

print('Content-type:text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/angle_zero.py" method="POST">')
print('<input type="range" name="slider" min="0" max="360" value="%s"><br>' % slider_position)
print('<input type="submit" value="Select Angle">')
print('</form>')
print('Angle = %s' % slider_position)
print('</html>')  