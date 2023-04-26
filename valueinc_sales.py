import pandas as pd
# file_name = pd.read_csv('file.csv') <---- format of read_csv

data = pd.read_csv(r'D:\My office\Udemy\Python and Tableau-The complete Data Analytics Bootcamp!\Project 1\transaction.csv', sep=';')

#summary of the data
data.info()

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new column to a dataframe
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

data['Markup'] = (data['ProfitperTransaction'])/data['CostPerTransaction']

#Rounding Marking
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#combining data fields

my_name = 'Palm' + 'Wisanu'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#checking columns data type
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
print(day.dtype)

my_date = day+'-'+data['Month']+data['Year'].astype(str)
data['date'] = my_date

#using iloc to view specific columns/rows
data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column
data.iloc[4,2] #brings in 4th row, 2nd column

#using split to split the client_keywords field
#New_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv(r'D:\My office\Udemy\Python and Tableau-The complete Data Analytics Bootcamp!\Project 1\value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old,df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

#dropping columns

# df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Day','Month','Year'], axis = 1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)
