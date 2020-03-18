# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:04:34 2020

@author:    dccsim

Collection of utilities to find index to minimum/maximum values of an nd-array

Source of inspiration: https://stackoverflow.com/questions/30180241/numpy-get-the-column-and-row-index-of-the-minimum-value-of-a-2d-array

Libraries:  Numpy 

History:  20200318  v1 - get_idx_2d(), get_idx_nd() 

"""

"""
    purpose:   function to find row and col of 2d array with min/max value
    in:        2-d array, type=min/max
    out:       row and column of the minimum/maximum value, excluding NA
"""
import numpy as np

def get_idx_2d(arr, type):
    idx_r = np.nan
    idx_c = np.nan

    if type == 'min':
        ind = np.nanargmin(arr)
    elif type == 'max':
        ind = np.nanargmax(arr)
    else:
        print('usage: type = min/max')
        return idx_r, idx_c
        
    ncol = arr.shape[1]
    idx_r = int(np.floor(ind/ncol))
    idx_c = ind%ncol

    return idx_r, idx_c

"""
    purpose:   function to find index of n-d array with min/max value
    in:        n-d array, type=min/max
    out:       list of index to the min/max value, excluding NA
"""
def get_idx_nd(arr, type):
    
    # dimension of array
    num_dimension = len(arr.shape)
    result_idx = []
    
    if type == 'min':
        full_idx = np.nanargmin(arr)
    elif type == 'max':
        full_idx = np.nanargmax(arr)
    else:
        print('usage: type = min/max')
        return result_idx
        
    # find the indices from the first (0) dimension to the n dimension, for a n-dimension array
    for curr_dim in range(num_dimension):
        if curr_dim < (num_dimension-1):
            # 0 to n-1 dimension
            denominator = 1
            for m in range((num_dimension-1),curr_dim,-1):
                denominator = denominator * arr.shape[m]
            dim_idx = int(np.floor(full_idx/denominator) % arr.shape[curr_dim])
        else:
            # last dimension is treated differently
            multiplier = 1
            for m in range(curr_dim+1):
                multiplier = multiplier * arr.shape[m]
            dim_idx = (full_idx - multiplier) % arr.shape[num_dimension-1]
        
        result_idx.append(dim_idx)
        
    return np.array(result_idx)