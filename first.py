import numpy as np
import math as m
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\ANTARIKSHYA\OneDrive\Desktop\MYpython\sample2.csv')
print(df.shape)
# df.dropna(how='any',inplace=True)
print(df.isnull().sum())