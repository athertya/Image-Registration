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
# Function : cleanText
# Notes: This function cleans the string and removes junk characters 
#-------------------------------------------------------------------------------------

def cleanText(string_val):
    # clean and standardize text descriptions, which makes searching files easier
    forbiddenSymbols = ["*", ".", "\"", "\\", "/", "|", "[", "]", ":", ";", " ",',',"`"]
    
    for symbol in forbiddenSymbols:
        string_val = string_val.replace(symbol, "_") # replace everything with an underscore
    string_val = ''.join(filter(lambda x:x in string.printable, string_val))
    s = ascii(string_val)
    return s.replace("'",'')

#-------------------------------------------------------------------------------------
# Function : sortDicom
# Notes: This function sorts the diom files 
#-------------------------------------------------------------------------------------

def sortDicom(unsortedList,dst):
    for dicom_loc in unsortedList:
        ds = pydicom.read_file(dicom_loc,force=True)
        # get instance number, series description and series information
        seriesDescription = cleanText(ds.get("SeriesDescription", "NA"))
        instanceNumber = ds.get("InstanceNumber","NA")
        seriesNumber = ds.get("SeriesNumber","NA")
        instanceNumber = str('%04d' % instanceNumber)
        seriesNumber = str('%04d' % seriesNumber)
        fileName = 'Image' + instanceNumber + '.dcm'
        #print(fileName)
        
        dstFolder = dst + "/" + seriesDescription + "_Series" + seriesNumber
        if not os.path.exists(dstFolder):
            os.makedirs(dstFolder)
        ds.save_as(os.path.join(dstFolder,  fileName))
    
#-------------------------------------------------------------------------------------
# Function : main
# Notes : This is main function of this program
#-------------------------------------------------------------------------------------

def main():
    # Reading source path and creating destination path for sorted files
    src = input('Enter the source image path : ')
    #src = "./DCM_unsorted"
    dst = "./DCM_sorted"
    
    if(os.path.isdir(dst)):
        # If the destination directory already exists, remove or clear the files within it
        shutil.rmtree(dst)
    
    # Creates the destination directory    
    os.makedirs(dst,exist_ok=True)
    
    print('Reading dicom images from unsorted data:',src)
    unsortedList = []
    for root, dirs, files in os.walk(src):
        for file in files: 
                unsortedList.append(os.path.join(root, file))
    
    print('%s files found.' % len(unsortedList))
        
    # Calling the sortDicom function
    sortDicom(unsortedList,dst) 
    print('Dicom sorting completed....\nSorted files available at:',dst)    
    
if __name__ == "__main__":
    main()
