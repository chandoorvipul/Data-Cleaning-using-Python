import pandas
concatDf=pandas.read_csv("C:\\Exercise\\IncomeByStateByYear.csv")
nodupl=concatDf.T.drop_duplicates().T
nodupl.to_csv("C:\\Exercise\\IncomeByStateByYearNoDupl.csv",index=0)
