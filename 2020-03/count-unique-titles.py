#!/anaconda3/bin/python
#author Yuan Wu 2020-03
import pandas as pd
mydataframe = pd.read_csv('earth-dump.csv', encoding='latin1')
dt = mydataframe.title.unique()
print("Number of unique titles in earth-dump.csv", len(dt))
