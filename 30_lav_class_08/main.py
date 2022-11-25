import pandas

data = pandas.read_csv('./HR_comma_sep.csv')


# step 1: missing data for any row any column
# print(data.isnull().values.any())

# step 2: check data type 
print(data.dtypes)

