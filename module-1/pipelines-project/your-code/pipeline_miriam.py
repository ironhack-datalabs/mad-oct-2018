import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def acquire():
    data = pd.read_csv('data/blackfriday.csv')
    return data

def wrangle(data, year):
    filtered = data[data['year']==year]
    return filtered

def renamed(data):
    column_name = filtered.rename(columns={'Purchase':'Expenditure', 'City_Category': 'City'})
    return column_name

def drop_columns (data):
    new_data = column_name.drop(column_name.columns[[6]], axis=1)
    return new_data

def column_order (data):
    col_order = ['User_ID', 'Product_ID', 'year', 'Gender', 'Age', 'City', 'Occupation', 'Marital_Status', 'Expenditure', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3']
    new_order = new_data[col_order]
    return new_order

def create_bins (data):
    expend_labels = ['Low', 'Moderate', 'High', 'Very High']
    cutoffs = [0,6000, 12000, 18000, 24000]
    bins = pd.cut(new_order['Expenditure'],cutoffs, labels=expend_labels)
    new_order['Expend']=bins
    return new_order

def analyze(data):
    grouped = new_order.groupby('Age').agg({'Expenditure':'mean'}).reset_index()
    results = grouped.sort_values('Expenditure', ascending=False).head(10)
    return results

def save_visualize(data, title):
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=results, x='Age', y='Expenditure')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')

if __name__ == '__main__':
    title = 'Average expenditure by age'
    year = int(input('Please enter the year: '))
    data = acquire()
    filtered = wrangle(data,year)
    column_name = renamed(filtered)
    new_data = drop_columns(column_name)
    new_order = column_order(new_data)
    new_order = create_bins (new_order)
    results = analyze(new_order)
    save_visualize(results, title)