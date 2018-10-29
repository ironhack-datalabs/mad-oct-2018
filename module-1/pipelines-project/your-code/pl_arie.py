import pandas as pd
year = year = int(input('Enter the year: '))

### Adquisition 
def acquire():
    file = "./data/tenis_{}.csv".format(year)
    df = pd.read_csv(file)
    return df 

data = acquire()

### Wrangling
def wrangle(data): 
    data["tourney_date"] = pd.to_datetime(data.tourney_date.astype("str")) # le doy formato de fecha a tourney date
    data["tourney_month"] = data["tourney_date"].dt.month # creo una columna con el mes que figura en tourney date
    filtered = data[data["tourney_month"] == month] # Filtro el dataframe por el mes que me interesa
    return filtered

filtered = wrangle(data)

### Analyzing 
def analize(filtered):
    grouped = filtered["winner_name"].value_counts().head(10) # cantidad de partidos ganados en el mes 

""" media de partidos ganados al mes por jugador"""
    monthly_mean = round(data.groupby("winner_name")["winner_name"].count()/(len(set(data['tourney_month']))),1) 

# convierto las series en Dataframes para poderles hacer un merge eventualmente y ponerlas en la misma tabla. 
    pd_grouped = (pd.DataFrame(grouped)).reset_index(level=0)
    pd_grouped = pd_grouped.rename(columns={"winner_name":"winned matches","index":"winner_name"})
    df_mm = pd.DataFrame(monthly_mean)
    df_mm.index.names = ["winner"]
    df_mm = (df_mm.reset_index(level=0))
    df_mm = df_mm.rename(columns={"winner_name":"avg winned matches per month","winner":"winner_name"})
    df_merge = pd.merge(pd_grouped,df_mm,on="winner_name")
    return df_merge