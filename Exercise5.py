import pandas
left="IncomeByStateByYearNoDupl.csv"
right="Geoids and States.csv"
output="IncomeByStateByYearNoDuplFinal.csv"
leftDf=pandas.read_csv(left)
rightDf=pandas.read_csv(right)
mergedDf=pandas.merge(leftDf,rightDf,left_on="GEOID",right_on="GEOID")
mergedDf.set_index(["GEOID" , "State"],inplace=True)
mergedDf.to_csv(output)