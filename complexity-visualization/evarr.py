import numpy as np
import os
from scipy import signal

def compressed_size(arr, tmp_name = "tmp.npz"):
    np.savez_compressed(tmp_name,arr)
    sz = os.path.getsize(tmp_name)
    os.remove(tmp_name)

    return sz

def x2(arr):
    shape = arr.shape
    new_arr = np.zeros((shape[0] * 2, shape[1] * 2))
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            new_arr[i*2,j*2] = arr[i,j]
            new_arr[i*2 + 1,j*2] = arr[i,j]
            new_arr[i*2,j*2+1] = arr[i,j]
            new_arr[i*2+1,j*2+1] = arr[i,j]
    
    return new_arr

def zoom(arr):
    z_arr = signal.convolve2d(arr,
                              np.array([[.11,.11,.11],
                                        [.11,.12,.11],
                                        [.11,.11,.11]]),
                              mode="same",
                              boundary="wrap"
    )
    return z_arr

def zoomstack(arr, k = 50):
    arrs = [arr]
    
    for i in range(k):
        arrs.append(zoom(arrs[-1]))
        
    zstack = np.stack(arrs,axis=2)
    
    return zstack
