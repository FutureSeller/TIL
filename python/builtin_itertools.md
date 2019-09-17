#### combination and permutation

``` python
from itertools import combinations, permutations

inputs = [1,2,3]
"""
(1, 2)
(1, 3)
(2, 3)
"""
for c in combinations(inputs, 2):
    print c

print ('-----')

"""
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
"""
for p in permutations(inputs, 2):
    print p
```
