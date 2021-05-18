# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a transformix script file.

Example : transformix -in B1_2.nii.gz -out B1_2 -tp Transformparameters.1.txt
"""
import os


# Creating B1 files for registration
list_B1 = []
src = './B1'
for root, dirs, files in os.walk(src):
    for file in files: 
        if not '_1.' in file:
            list_B1.append(os.path.join(root,file))
 
# Creating T1 files for registration  
list_T1 = []
src = './T1'
for root, dirs, files in os.walk(src):
    for file in files: 
        if not '_1.' in file:
            list_T1.append(os.path.join(root,file))

# Importing transformation parameters from B1_1 folder for subsequent registration

for fileB in list_B1:
    print(fileB)
    output = fileB.split('/')[-1].split('.')[0]
    tparam = 'Reg/B1_1/TransformParameters.1.txt'
    dst = 'Reg/'+output
    os.makedirs(dst,exist_ok=True)
    regCommand = 'transformix -in ' + fileB + ' -out ' + dst + ' -tp '+ tparam + ' > ' + dst +'/run_'+output+'.log'
    print(regCommand)
    os.system(regCommand)

# Importing transformation parameters from respective T1 folders for subsequent registration

for fileT in list_T1:
    print(fileT)
    output = fileT.split('/')[-1].split('.')[0]
    output2 = fileT.replace('_2.','_1.').split('/')[-1].split('.')[0]
    tparam = 'Reg/' + output2+'/TransformParameters.1.txt'
    print(tparam)
    dst = 'Reg/'+output
    os.makedirs(dst,exist_ok=True)
    regCommand = 'transformix -in ' + fileT + ' -out ' + dst + ' -tp '+ tparam + ' > ' + dst + '/run_'+output+'.log'
    print(regCommand)
    os.system(regCommand)