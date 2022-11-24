import random
import time
import numpy as np
def scalar_product(n):
    list1 = []
    list2 = []
    product = []
    start = time.time_ns()
    for i in range(n+1):
        list1.append(random.randint(0, 100))
        list2.append(random.randint(0, 100))
    for i, o, in zip(list1, list2):
        product.append(i*o)    
    end = time.time_ns()
    regular_time = end-start
    start = time.time_ns()
    n_list1 = np.random.randint(100, size = n)
    n_list2 = np.random.randint(100, size = n)
    n_product = np.multiply(n_list1, n_list2)
    end = time.time_ns()
    numpy_time = end-start
    return regular_time, numpy_time

print(scalar_product(1000000))
## Numpy method is a lot faster 
    

