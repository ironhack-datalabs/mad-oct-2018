# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


data = pd.read_csv('Final_paper.csv')
data.head(5)


# In[22]:


def acquire():
    data = pd.read_csv('Final_paper.csv')
    return data



# In[26]:


def wrangle(data):

    year=int(input('Please enter the year: '))
    filtered = data[data['year']==year]
    return filtered



# In[28]:


def analyze(filtered):
    grouped = filtered.groupby('BINS').agg({'Happiness Score':'mean'}).reset_index()
    results = grouped.sort_values('Happiness Score', ascending=False).head(10)
    return results




# In[32]:

'''
def visualize(df):
    title = "lo q sea "
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=results, x='BINS', y='Happiness Score')
    plt.title(title + "\n", fontsize=16)
    return barchart

# In[41]:


def save_viz(Happiness):
    title="chart"
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=data, x='BINS', y='Happiness Score')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')
'''

def report(df):
    title="chart"
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=df, x='BINS', y='Happiness Score')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')



# In[42]:


if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data)
    results = analyze(filtered)
    
    report(results)
    ##barchart = visualize(results)
    ##save_viz(results)