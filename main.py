# Simple data visualisation using the default functionalities offered in the seaborn tutorial
# https://seaborn.pydata.org/tutorial/introduction.html

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('indian_liver_patient.csv', delimiter=',')

nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')
print ("columns data type \n" + str(df1.dtypes))

print ("Conver Gender to numeric \n")
df1['Gender'] = df1['Gender'].map({'Male': 1, 'Female': 0})
print ("Rename colum Dataset in Target \n")
df1.rename(columns={"Dataset": "Target"}, inplace=True)

## TARGET
# Target --> "Dataset" : patient with liver disease = 2, or no disease = 1
sns.displot(data=df1.Target)
## FEATURES vs TARGET
sns.pairplot(data=df1,  hue="Target")
# FEATURES vs AGE
g = sns.PairGrid(df1, hue="Age", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))
#plt.show()

#Simple Correlation Plot
corr = df1.corr()
plt.figure()
g = sns.heatmap(corr,  vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt='.2f', cmap='coolwarm')
#plt.show()

# Swarm Plots
plt.figure()
g = sns.swarmplot(y = "Direct_Bilirubin", x = 'Target', data = df1, size = 7)
sns.despine()
g.figure.set_size_inches(14,10)
#plt.show()

# Box Plots
plt.figure()
g = sns.boxplot(y = "Albumin_and_Globulin_Ratio", x = 'Target', data = df1)
sns.despine()
g.figure.set_size_inches(12,8)
plt.show()

