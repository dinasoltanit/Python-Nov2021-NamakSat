import numpy as np
import pandas as pd
"""
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
s.index
print(s.index)
print(s[0])
print(s[:3])
print('median: ' , s.median())
print('mean:' , s.mean())
print('max: ' , s.max())
print(s[s > s.median()])
"""
d = {"one": [1.0, 2.0, 3.0, np.nan], "two": [1.0, 2.0, 3.0, 4.0]}
# print(d)
dframe = pd.DataFrame(d, index=["a", "b", "c", "d"])
#print(dframe)
dframe["three"] = dframe["one"] * dframe["two"]
dframe["flag"] = dframe["one"] > 2

print(dframe)

del dframe["two"]

print(dframe)

three = dframe.pop("three")
print(dframe)

print(three)