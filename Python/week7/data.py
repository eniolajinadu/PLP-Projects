import matplotlib as mat #for data visualization, i.e., 
import pandas as pd
import numpy as np
import chardet #to detect what encoding the '.csv' file is in.

with open('/home/eniolajinadu/GitHub/PLP-Projects/Python/week7/MathE dataset.csv', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
print(encoding)

df = pd.read_csv('/home/eniolajinadu/GitHub/PLP-Projects/Python/week7/MathE dataset.csv', encoding=encoding, delimiter=';')
print(df.head(6))

