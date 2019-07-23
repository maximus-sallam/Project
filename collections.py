from collections import OrderedDict

d = { 2:3, 1:9, 7:5, 4:0 }

od = OrderedDict(sorted(d.items()))
print(od)
