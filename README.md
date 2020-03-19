# nd-array-index-finder
Functions that return the minimum/maximum value of indices to nd-arrays

## setup
```
  # setup
  
  import numpy as np
  
  rand_seed = 1999
  np.random.seed(rand_seed)
```
## 2d array
```
  # find index to smallest and largest values in a 2d array
  arr = np.random.randint(1,20,(3,4))
  print(arr,'\n')

  idx_min = finder.get_idx_2d(arr,'min')
  print('index to smallest value:', idx_min)
  idx_max = finder.get_idx_2d(arr,'max')
  print('index to largest value:', idx_max)

  n_idx_min = finder.get_idx_nd(arr,'min')
  print('index to smallest value:', n_idx_min)        
  n_idx_max = finder.get_idx_nd(arr,'max')
  print('index to largest value:', n_idx_max) 
```
## nd array
```
  # find index to smallest and largest values in an nd array
  arr = np.random.randint(1,100,(2,3,4,5))
  print(arr,'\n')

  n_idx_min = finder.get_idx_nd(arr,'min')
  print('index to smallest value:', n_idx_min)        
  n_idx_max = finder.get_idx_nd(arr,'max')
  print('index to largest value:', n_idx_max) 
```
