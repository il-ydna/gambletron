import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataFrame = pd.read_csv("data.csv")
print(dataFrame)

df_sorted = dataFrame.sort_values(by='Age')

cats_to_add = ['PTS', 'TRB', 'AST', 'STL', 'BLK']

age_avg_pts = df_sorted.groupby('Age')['PTS'].mean()
age_avg_trb = df_sorted.groupby('Age')['TRB'].mean()
age_avg_ast = df_sorted.groupby('Age')['AST'].mean()
age_avg_stl = df_sorted.groupby('Age')['STL'].mean()
age_avg_blk = df_sorted.groupby('Age')['BLK'].mean()

print(age_avg_pts)

plt.figure(figsize=(10,6))
plt.plot(age_avg_pts.index, age_avg_pts.values, color='red')
plt.plot(age_avg_trb.index, age_avg_trb.values, color='blue')
plt.plot(age_avg_ast.index, age_avg_ast.values, color='green')
plt.plot(age_avg_stl.index, age_avg_stl.values, color='black')
plt.plot(age_avg_blk.index, age_avg_blk.values, color='orange')

plt.legend(["Points", "Rebounds", "Assists", "Steals", "Blocks"], loc="best")
# plt.legend(["Rebounds", "Assists", "Steals", "Blocks"], loc="lower left")

plt.ylim(0, 27)
plt.xlabel('Age')
plt.ylabel('Points Per Game')
plt.title('Mean Stats vs. Age of NBA All-Stars since 2000')
plt.xticks(age_avg_pts.index)
plt.grid(True)

# Show the plot
plt.show()