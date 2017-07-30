# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:09:00 2017

@author: spook
"""

import os
def rename_file():
    '''(1) get tile names  fromm a folder'''
    file_list = os.listdir(r'C:\Users\spook\Downloads\prank\prank')
    print(file_list)
    saved_path = os.getcwd()
    print('Current working Directory is '+saved_path)
    os.chdir(r'C:\Users\spook\Downloads\prank\prank')
    # (2) for eaxh file, rename filename
    for file_name in file_list:
        print('Old Name - '+file_name)
        print('New name - '+file_name.translate(file_name, None,'0123456789'))
        os.rename(file_name, file_name.translate('0123456789'))
    os.chdir(saved_path)
    
rename_file()