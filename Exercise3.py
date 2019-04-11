import pandas
import glob
filelist=glob.glob("C:\\Exercise\\*.xls")
dfList=[]
for filename in filelist:
df=pandas.read_excel(filename,skiprows=[0,1,2])
dfList.append(df)
concatDf=pandas.concat(dfList,axis=1)
concatDf.to_csv("C:\\Exercise\\IncomeByStateByYear.csv",index=0)