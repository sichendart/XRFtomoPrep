# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:06:26 2018

To pad all 32-bit tiff images in a directory to the largest dimensions

@author: sichen
"""

import os
import sys
from skimage import io
import numpy as np


def MaxDim(path):
    """
    To find the max dimensions of 32-tif images in a directory
    arg:
    directory, type: string
    example:
    /Users/sichen/Box\ Sync/data/BNP/2018-2/Wang_tomo/Cu/

    """   
    max_x_dim = 1
    max_y_dim = 1
    
    files = os.listdir(path)
    for fname in files:
        if fname[-3:] == 'tif':    
            im = io.imread(path+fname)
            x_dim = im.shape[0]
            y_dim = im.shape[1]
            if x_dim > max_x_dim:
                max_x_dim = x_dim
            if y_dim > max_y_dim:
                max_y_dim = y_dim
    MaxDim = (max_x_dim, max_y_dim)
    
    return MaxDim
    
    
    
def pad(arr, dim, constant):
    """
    arr: a 2D numpy array
    dim: tuple, dimensions in x and y
    constant: pad value
    
    """
    x = dim[1]-arr.shape[1]
    y = dim[0]-arr.shape[0]
    arr_pad = np.pad(arr,((0,y),(0,x)), 'constant', 
                     constant_values = constant)
    return arr_pad
    
    
    
def main(argv):
    """
    argv: directory, type: string 
          example:  /Users/sichen/Box\ Sync/data/BNP/2018-2/Wang_tomo/Cu/
    To pad all the 32-tif images in a directory to the largest dimensions.
    
    """
    path = argv[1]
    if path[-1] != '/':
        path = path + '/'
        
    new_path = path + 'pad/'
    if not os.path.exists(new_path):
        os.mkdir(new_path)
        
    dim = MaxDim(path)
    constant = 0
    
    for fname in os.listdir(path):
        if fname[-3:] == 'tif': 
            arr = io.imread(path+fname)
            arr_pad = pad(arr, dim, constant)
            io.imsave(new_path+fname.split('.')[0]+'_pad.tif', arr_pad)
         
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))