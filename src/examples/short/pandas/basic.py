#!/usr/bin/python3

"""
A basic demo of pandas
"""

from pandas import DataFrame
import numpy
import random
import string


df = DataFrame(["a", "b", "c"], index=[0,1,2])
print(df.get_values())
print(df.loc[0])
print(df.loc[1])
print(df.loc[2])
print(df.ix[0])
print(df.ix[1])
print(df.ix[2])
print(df.xs(0))
print(df.xs(1))
print(df.xs(2))
