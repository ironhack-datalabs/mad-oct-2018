def mean_by(df,col_group,col_func):
    df1 = df.pivot_table(index=[col_group],aggfunc={col_func:"mean"}).reset_index() 
    diccio = dict(zip(df1[col_group],df1[col_func]))
    return diccio

def win_medals(df,medalla):
    filt = df.pivot_table(index="NOC",columns="Medal",aggfunc={"Medal":"count"}).fillna(0)
    return filt["Medal"][medalla].sort_values(ascending=False).head(3)