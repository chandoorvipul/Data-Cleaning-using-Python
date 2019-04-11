
import pandas
df=pandas.read_csv("C:\\Exercise\\IncomeByState1984.csv")
df["1984 Euros"]=df["1984"]*0.88
df["1984 Pounds"]=df["1984"]*0.64
df.to_csv("C:\\Exercise\\IncomeByState1984Currency.csv",index=0)
