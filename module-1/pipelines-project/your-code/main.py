import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def acquire():
    data = pd.read_csv('./2015_happiness.csv')
    return data

def wrangle(data):
    data['Happiness Score'] = data['Happiness Score']/1000
    return data

def anio(year):
    data['Year']= year
    return data

def analyze(data):
    grouped = data.groupby('Region').agg({'Economy (GDP per Capita)':'mean'}).reset_index()
    results = grouped.sort_values('Economy (GDP per Capita)', ascending=False).head(10)
    return results


## Data reporting
def save_visualize(data, title):
    title= 'Happiness'
    fig, ax = plt.subplots(figsize=(15,10))
    barchart = sns.barplot(data=data, x= 'Region', y='Economy (GDP per Capita)')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')
    


if __name__ == '__main__':
    year = int(input('Enter the year: '))
    title = 'Happiness' + str(year)
    data = acquire()
    results = analyze(data)
save_visualize(results, title)