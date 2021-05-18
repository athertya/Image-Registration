#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:24:25 2021

@author: Jiyo

"""

#Complete image registration pipeline

import os

print('\nRunning sortDicom.....\n')
os.system('python3 sortDicom.py')

print('\nRunning dcm2Niix......\n')
os.system('python3 dcm2Niix.py')

print('\nRunning Elastix....\n')
os.system('python3 elastixReg.py')

print('\nRunning Transformix....\n')
os.system('python3 transformixReg.py')

print('\nRunning results for registration....\n')
os.system('python3 resultReg.py')

print('\n REGISTRATION COMPLETED....\n')