a = ["1", 1, "1", 2]
print(list(set(a)))

# to preserve the order of items
from collections import OrderedDict
a = list(OrderedDict.fromkeys(a, "cycki"))
print(a)
