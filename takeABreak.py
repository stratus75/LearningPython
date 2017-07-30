# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:30:45 2017

@author: spook
"""
import time
import webbrowser

total_break = 3
break_count = 0

print('This program started on '+time.ctime())
while (break_count < total_break):
    time.sleep(2*60*60)
    webbrowser.open('https://www.youtube.com/watch?v=gOrnLU8LyAU')
    break_count = break_count + 1
