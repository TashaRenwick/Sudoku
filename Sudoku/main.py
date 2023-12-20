import random

import numpy as np

rand_list = [random.randint(1,9) for _ in range(0,81)]
array = np.array(rand_list)
array = np.reshape(array, (9, 9))

print(array)

print('-'*40)

print('|', end=' ')
for num in array[0,:]:
    print(num, '|', end=' ')

print('-'*40)