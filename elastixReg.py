#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:01:27 2021

@author: Jiyo
"""
import os

# Creating B1 files for registration
list_B1 = []
src = './B1'
for root, dirs, files in os.walk(src):
    for file in files: 
        if '_1.' in file:
            list_B1.append(os.path.join(root,file))

    
# Creating MT files for registration          
list_MT = []
src = './MT'
for root, dirs, files in os.walk(src):
    for file in files: 
            list_MT.append(os.path.join(root,file))

# Creating T1 files for registration  
# Example :    list_T1 = ['T1_150_1.nii.gz','T1_20_1.nii.gz',T1_80_1.nii.gz',]       
list_T1 = []
src = './T1'
for root, dirs, files in os.walk(src):
    for file in files: 
        if '_1.' in file:
            list_T1.append(os.path.join(root,file))

# Complete set of files for registration

full_list = list_B1+list_MT+list_T1       

# Elastix Registration command generation for compilation     
# Example : elastix -f ./T1_20_1.nii -m ./MT_500_2K.nii -p ../params/pa.txt -p ../params/bs.txt -out output

for fileM in full_list: 
    print(fileM)
    regOut = fileM.split('/')[-1].split('.')[0]
    dst = 'Reg/'+regOut
    os.makedirs(dst,exist_ok=True)
    regCommand = 'elastix -f ./T1/T1_20_1.nii.gz -m ' + fileM + ' -p ./params/pa.txt -p ./params/bs.txt -out ' + dst +' > '+dst +'/run_'+regOut+'.log'
    print(regCommand)
    os.system(regCommand)
