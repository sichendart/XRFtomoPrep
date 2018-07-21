#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Friday July 20 2018

@author: sichen
"""

import os
import h5py
import shutil

#folder = '/home/beams/SICHEN/src/HDF_rename/test_data 2'
#folder = '.'
#path_name = '/home/x220/Dropbox/Si_Yifeng/work/test/'
path_name = '/Users/sichen/src/XRFtomoPrep/test/'
#path_name = '/home/x220/Dropbox/Si_Yifeng/work/'

def h5_rename(path_name):
    new_path = path_name + 'h5.tomo/'
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    for fname in os.listdir(path_name):
        if fname[-2:] == 'h5':
            print(fname)
            f = h5py.File(path_name + fname, 'r')
            smplT = f['MAPS']['extra_pvs_as_csv'][8]
            ang = int(round(float(smplT.decode('UTF-8').split(',')[-1].strip())))
            index = str(100+ang)
            try:
                shutil.copy(path_name + fname,
                            new_path + index + '_' + str(ang) + '_' + fname)
            except:
                print('cannot copy', fname)
            
            #f.close()
                   
    
if __name__ == '__main__':
    h5_rename(path_name)
    
"""
new_directory = folder+'h5.tomo/'

for fname in os.listdir(folder):
    if fname[-2:] == 'h5':
       print(fname)
       f = h5py.File(fname, 'r')
       smplT = f['MAPS']['extra_pvs_as_csv'][8]
       print(smplT)
       print(type(smplT))
       #pos = smplT.rfind(',')
       #ang = round(float(smplT[pos+1:]))
       ang = round(float(smplT.decode('UTF-8').split(',')[-1].strip()))
       index = str(100+ang)
       print(index)
       #os.rename(fname, index+'_'+str(ang)+'_'+fname)
       if not os.path.exists(new_directory):
           os.mkdir(new_directory)
       shutil.copy(fname, new_directory + index + '_' + str(ang) + fname)
       
       
"""