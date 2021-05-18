#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:36:42 2021

@author: Jiyo
"""
import os
from shutil import copyfile
src = 'Reg'
dst = 'RegResults/'
os.makedirs(dst,exist_ok=True)

print('Renaming files ....')
for root, dirs, files in os.walk(src):
    for file in files: 
        
        #For renaming files stored as result.1.nii
            if 'result.1.nii' in file:
                temp = os.path.join(root,file)
                # temp contains the full path for result file : Example 'Reg/MT_500_10K/result.1.nii'
                
                newName = temp.split('/')[1]+'.nii'
                #newName containes the renamed version of result file : Example 'MT_500_10K.nii'
                
                copyfile(temp,dst+newName)
                #copies file from source to desination
                print('Copying : "'+temp+'" To : "'+dst+newName+'"')
                
                #os.remove(dst)
                #To remove files
                
              
            if 'result.nii' in file:
                temp = os.path.join(root,file)
                # temp contains the full path for result file : Example 'Reg/MT_500_10K/result.1.nii'
                
                newName = temp.split('/')[1]+'.nii'
                #newName containes the renamed version of result file : Example 'MT_500_10K.nii'
                
                copyfile(temp,dst+newName)
                #copies file from source to desination
                print('Copying : "'+temp+'" To : "'+dst+newName+'"')
                #print('Copying : ',temp,' To : ',dst+newName)
                
print('The result files have been renamed and copied to RegResults....')               
  
