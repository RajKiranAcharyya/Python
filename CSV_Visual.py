import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(r"Sample_CSV_file.csv")
data.head()
df = pd.DataFrame(data)
Region = df["Region"].head(4)
Sales = df["Sales"].head(4)
fig = plt.figure(figsize=(10, 7))
plt.bar(Region[0:10], Sales[0:10])
plt.show()  # Bar graph
plt.pie(Sales, labels=Region)  # Pie graph
plt.legend()
plt.show()
