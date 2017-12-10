import numpy as np
import pandas as pd
airdata = pd.read_excel('airdata.xlsx')
#Data are measurements of air pollution levels from thousands of
#regions throughout the world recorded on WHO. This loop will count how many of
#these regions either do or do not meet guidelines - limit is 20
under_count = 0
over_count = 0
for i in airdata['PM10 Annual mean, ug/m3']:
    if i <= 20:
        under_count = under_count + 1
    elif i > 20:
        over_count = over_count + 1
print('%d recorded regions do not meet WHO air quality guidelines.' %(over_count))
print('%d recorded regions meet WHO air quality guidelines.' %(under_count))
