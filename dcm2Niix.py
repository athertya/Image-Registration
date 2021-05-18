#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:22:50 2021

@author: Jiyo
"""
# Importing dependcies

import pydicom
import nipype
from nipype.interfaces.dcm2nii import Dcm2niix
import os
import string
import shutil
from shutil import copyfile


#-------------------------------------------------------------------------------------
# Function : dcmToniix
# Notes: This function converts .dcm files into .nii 
#-------------------------------------------------------------------------------------

def dcmToniix(dst):
    for root,dirs,files in os.walk(dst):
      if len(files) == 0:
        continue
      sourceList = []
      for file in files:
          if '.dcm' in file:
              sourceList.append(os.path.join(root,file))
        
      print('Converting files in : '+root+ ' to .nii') 
      converter = Dcm2niix()
      #print(sourceList)
      converter.inputs.source_names = sourceList
      converter.inputs.compression = 5
      #print('root is ', root)
      converter.inputs.output_dir = root
      #print('\n\n\nconverter is :', converter.cmdline)
      #converter.run() # this does not yet work due to some unicode error ?? No idea why 
      #print('Converting files in : '+root+ ' to .nii')
      os.system('echo "'+converter.cmdline+'">>'+dst +'/runNiix.log')
      runNiix = converter.cmdline +' >> '+ dst +'/runNiix.log'
      os.system(runNiix) # use this code .. this works        

#-------------------------------------------------------------------------------------
# Function : renameB1, renameMT, renameT1
# Notes: This function renames B1, MT, T1 
#-------------------------------------------------------------------------------------
def renameB1(srcList):
    dst = 'B1'
    if(os.path.isdir(dst)):
        # If the destination directory already exists, remove or clear the files within it
        shutil.rmtree(dst)
    os.makedirs(dst,exist_ok=True)
    for src in srcList:
        file_B1 = []
        file_B1 += [each for each in os.listdir(src) if each.endswith ('.nii.gz')]
                 
        for name in file_B1:
            
            # Splitting names inside the B1 folder list with .nii and then taking last element number
            
            numberB1 = name.split('.nii')[0][-1]
            new_name = 'B1_'+numberB1+'.nii.gz'
            copyfile(src+'/'+name,dst+'/'+new_name)
    

def renameMT(srcList):
    #src ='/home/sri/Jwork/imgReg/pysorted_output2/NOT_DIAGNOSTIC__conesMT_FA=500_Off=2K_TR=100_eFA=8_Nsp=11_str=1_3_tau=6_un=1_1_Series0009/'
    dst = 'MT'
    if(os.path.isdir(dst)):
        # If the destination directory already exists, remove or clear the files within it
        shutil.rmtree(dst)
    os.makedirs(dst,exist_ok=True)
    for src in srcList:
       
        
        file_MT = []
        file_MT += [each for each in os.listdir(src) if each.endswith ('.nii.gz')]
        #print(file_MT)   
        
        for name in file_MT:
             name1 = ascii(name)
             name_list = name1.split('_')
             #print(name_list)
             for partFA in name_list:
                     if partFA.startswith('FA'):
                         #print(partFA)
                         partFA1=partFA.split('=')[1]
                         #print(partFA1)
             for partOff in name_list:
                     if partOff.startswith('Off'):
                         #print(partOff)
                         partOff1=partOff.split('=')[1]
                         #print(partOff1)         
             new_name = 'MT'+'_'+partFA1+'_'+partOff1+'.nii.gz'
             #print(new_name)
             copyfile(src+'/'+name,dst+'/'+new_name)

def renameT1(srcList):
    dst = 'T1'
    if(os.path.isdir(dst)):
        # If the destination directory already exists, remove or clear the files within it
        shutil.rmtree(dst)
    os.makedirs(dst,exist_ok=True)
    
    for src in srcList:
        
        file_T1 = []
        file_T1 += [each for each in os.listdir(src) if each.endswith ('.nii.gz')]
        #print(file_T1)
        
        for names in file_T1:
            
            name_list = names.split('_')
            #print(name_list)
            num = name_list[-1].split('.')[0][-1]
            #print('num = ',num)
            for partTR in name_list:
                     if partTR.startswith('TR'):
                         #print(partTR)
                         partTR1=partTR.split('=')[1]
                         #print(partTR1)
               
            new_name = 'T1'+'_'+partTR1+'_'+num+'.nii.gz'
            #print(new_name)
            copyfile(src+'/'+names,dst+'/'+new_name)
#-------------------------------------------------------------------------------------
# Function : renamePath
# Notes: This function provides the path of directores to be renamed B1, MT, T1 
#-------------------------------------------------------------------------------------


def renamePath(dst):
    B1list = []
    for path, dirs, filename in os.walk(dst): #omit files, loop through later
        for dirname in dirs:
            fullpath = os.path.join(path,dirname)
            if "B1" in dirname:
                B1list.append(fullpath)
    renameB1(B1list)          
                
    MTlist = []
    for path, dirs, filename in os.walk(dst): #omit files, loop through later
        for dirname in dirs:
            fullpath = os.path.join(path,dirname)
            if "MT" in dirname:
                MTlist.append(fullpath)
    #print('This is MT list', MTlist)
    renameMT(MTlist)     
    
    T1list = []
    for path, dirs, filename in os.walk(dst): #omit files, loop through later
        for dirname in dirs:
            fullpath = os.path.join(path,dirname)
            if "conesT1" in dirname:
                T1list.append(fullpath)
    renameT1(T1list)          
    
def main():  
    dst = "./DCM_sorted"
    print('Converting dicom files to .nii.gz ....')
    dcmToniix(dst)
    renamePath(dst)

if __name__ == "__main__":
    main()
