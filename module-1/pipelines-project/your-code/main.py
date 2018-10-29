# imports
from funciones import select_year, rename_columns, remove_cols, remove_nan_rows

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def acquire(path='./data/GSAF5.csv', encoding='ISO-8859-1'):
    dfac = pd.read_csv(path)
    return dfac

def wrangle(dfw):
    year = select_year()
    dfw1 = rename_columns(dfw)    
    dfw2 = remove_cols(dfw1) 
    dfw3 = remove_nan_rows(dfw2)    
    filtered = dfw3[dfw3['Year'] == year]
    return filtered

def analyze(dfan):
    res = activities = dfan.Activity.value_counts()[0:10]
    return res

def report(dfr, title='Sharks!!'): 
    # visualize
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(x=dfr.index, y=dfr.values) 
    plt.xticks(rotation=75)
    plt.title(title + "\n", fontsize=16)

    # save barchar
    fig = barchart.get_figure()
    fig.savefig(title + '.png')    
    
    

if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data)
    results = analyze(filtered)
    report(results)
