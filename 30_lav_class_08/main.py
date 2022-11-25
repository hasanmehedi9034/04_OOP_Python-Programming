import pandas as pd

data = pd.read_csv('./HR_comma_sep.csv')


# step 1: missing data for any row any column
# print(data.isnull().values.any())

# step 2: check data type 
# print(data.dtypes)

# step 3: check unique values
# print(data.salary.unique())
# print(data.Department.unique())

clean_up_values = {
    'salary': {
        'low': 1,
        'medium': 2,
        'high': 3
    }
}

data.replace(clean_up_values, inplace=True)
# print(data)

'''
pandas get dummeis(google)
'''

# step 4: get dummies for the Department

dummies = pd.get_dummies(data.Department)
# print(dummies)

# step 5: merge the dummies (dummy column) with original data
merged = pd.concat([data, dummies], axis='columns')
# print(merged)

# step 6: drop unnecessary columns
final_data = merged.drop(['Department', 'technical'], axis='columns')
print(final_data)


