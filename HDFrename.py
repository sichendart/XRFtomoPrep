#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Friday July 20 2018

@author: sichen

To prep XRFtomo data collected at the BNP for tomo recon;
To rename the hdf files to include an index and angle information

to run:
python HDFrename.py arg
arg:
directory for the hdf5 files; example
/Users/sichen/src/XRFtomoPrep/test/

"""

import sys, os
import h5py
import shutil


#path_name = '/Users/sichen/src/XRFtomoPrep/test/'
#path_name = '/mnt/micdata1/bnp/2018-2/Nowakowski_tomo/img.dat/'



def h5_rename(argv):
    path_name = argv[1]
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
    sys.exit(h5_rename(sys.argv))
    
