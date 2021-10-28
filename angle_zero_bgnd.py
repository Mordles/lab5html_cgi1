#!/usr/bin/python37all

import json


while True:
  with open('selected_led.txt', 'r') as f:
    data = json.load(f)
  
  print(data['slider'])
  print(data['zero'])

  