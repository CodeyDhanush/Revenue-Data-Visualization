import pandas as pd
import matplotlib.pyplot as plt

#CSV File
df = pd.read_csv("McDonalds_Financial_Statements.csv")

#X & Y values
y_axis= df['Revenue ($B)']
x_axis = df['Year']

#Bar chart
plt.bar(x_axis,y_axis)
plt.title('McDonalds Revenue Growth')
plt.xlabel('Year')
plt.ylabel('Revenue ($B)')
plt.show()
