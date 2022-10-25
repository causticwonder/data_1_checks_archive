import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('assets/eurovision.csv')
print(df.head)

my_list = list(df)
print(my_list)

plt.plot(df['year'], df['total_points'])
plt.title('Eurovision')
plt.xlabel('year')
plt.ylabel('points')
plt.show()
