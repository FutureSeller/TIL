#### dictionary sorting based on values
``` python
from collections import OrderedDict

d = {
  "a": 1,
  "b": 0
}

# [('b', 0), ('a', 1)]
sorted_d = sorted(d.items(), key=lambda x: x[1])

# OrderedDict([('b', 0), ('a', 1)])
ascending_dict = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

# OrderedDict([('a', 1), ('b', 0)])
decending_dict = OrderedDict(sorted(ascending_dict.items(), key=lambda x: x[1], reverse=True))
```