import pandas
import seaborn as sns
import matplotlib.pyplot as plt
infile="C:\\Exercise\\US States Median Income Data.csv"
df=pandas.read_csv(infile)
df=df.set_index(['GEOID','State'])
fig, axes = plt.subplots()
axes.tick_params(labelsize=8)
sns.heatmap(df, ax=axes)
fig.savefig("C:\\Exercise\\Income Heatmap.png",dpi=200)

