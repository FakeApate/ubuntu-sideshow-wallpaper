#! /bin/python3

import os
import argparse
#parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d","--duration", type=float, help="defines duration in seconds for wallpaper until transition", default=900.0)
parser.add_argument("-t", "--transition", type=float, help="defines duration in seconds for transistion", default=2.0)
parser.add_argument("images", nargs='*')
args = parser.parse_args()

#getting absolut path from selected images
images = []
for img in args.images:
    path = os.path.abspath(img)
    images.append(path)

#define helper function for less gibberish
def print_helper(img, img2):
    print('''  <static>
    <duration>''',args.duration,'''</duration>
    <file>'''+img+'''</file>
  </static>
  <transition>
    <duration>''',args.transition,'''</duration>
    <from>'''+img+'''</from>
    <to>'''+img2+'''</to>
  </transition>''')

#print all static and transination except last one
length = len(images)
print('<?xml version="1.0" ?>\r\n<background>')
for x in range(0,length-1):
    print_helper(images[x], images[x+1])

#print last
print_helper(images[length-1],images[0])
print('</background>')  
    
