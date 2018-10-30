import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

year_l = [2016,2017]
months = [1,2,3,4,5,6,7,8,9,10,11]

while True:
    try:
        year = int(input('Enter the year: '))

    except:
        print("Oops!  That was no valid number.  Try again...")

    else: 
        if year in year_l:
            break
        else: 
            print("Oops!  That was no valid number.  Try again...")

while True:
    try:
        month = int(input("Enter the month from january till september (1-11) if you dont want to filter by month insert, 0: "))

    except:
        print("Oops!  That was no valid number.  Try again...")

    else: 
        if month in months:
            break
        else: 
            print("Oops!  That was no valid number.  Try again...")
            

title = "Winned matches in the {}th month of the year number {}".format(month,year)


### Adquisition 
def acquire():
    file = "./data/tenis_{}.csv".format(year)
    df = pd.read_csv(file)
    return df 

data = acquire()

### Wrangling
def wrangle(data): 
    data = data.dropna(thresh=10)
    data["tourney_date"] = data.tourney_date.astype("str") # cambio
    data["tourney_date"] = data["tourney_date"].str.split(".",expand=True) # cambio
    data["tourney_month"] = pd.to_datetime(data["tourney_date"]).dt.month
    if month == 0:
        filtered = data
    else: 
        filtered = data[data["tourney_month"] == month] # Filtro el dataframe por el mes que me interesa
    return filtered
    
filtered = wrangle(data)

### Analyzing
def analize(filtered):
    grouped = filtered["winner_name"].value_counts().head(5) # cantidad de partidos ganados en el mes 

    """ media de partidos ganados al mes por jugador"""
    monthly_mean = round(data.groupby("winner_name")["winner_name"].count()/(len(set(data['tourney_date']))),1) 
    pd_grouped = (pd.DataFrame(grouped)).reset_index(level=0)
    pd_grouped = pd_grouped.rename(columns={"winner_name":"winned_matches","index":"winner_name"})
    df_mm = pd.DataFrame(monthly_mean)
    df_mm.index.names = ["winner"]
    df_mm = (df_mm.reset_index(level=0))
    df_mm = df_mm.rename(columns={"winner_name":"avg_winned_matches_per_month","winner":"winner_name"})
    df_merge = pd.merge(pd_grouped,df_mm,on="winner_name")
    return df_merge

df_merge = analize(filtered)

### Reporting
def visualize(df_merge):  
    player = df_merge["winner_name"].head(5)
    winned_matches = df_merge["winned_matches"].head(5)
    avg_winned_matches = df_merge["avg_winned_matches_per_month"].head(10)
    sns.set()
    
    _= fig, ax = plt.subplots(figsize=(10,5))
    _ = plt.bar(player,winned_matches)
    _ = plt.bar(player,avg_winned_matches)
    _ = plt.xlabel("name of the player",fontsize=15)
    _= plt.ylabel("number of games",fontsize=15)
    _= plt.legend(labels=["Winned matches","Avg winned matches per month"])
    _= plt.title(title.format(month) + "\n", fontsize=16)
    plt.xticks(fontsize=10)
    plt.savefig(title + '.png')
    
visualize(df_merge)
    