import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

year = int(input("En que año: "))
weight = str(input("Altura máxima [cm]: "))
position = str(input("Posición en el campo (PG, SG, SF, PF o C): "))
title = "Más veces mejores jugadores de la semana " + str(year)

def acquire():
    data = pd.read_csv("NBA_player_of_the_week.csv")
    return data

def wrangle(data, year, weight, position):
    filtered = data[(data["Season short"]==year) & (data["Weight"]<="weight") & (data["Position"]=="position")]
    return filtered

def analyze(filtered):
    results = filtered
    return results

def visualize(results):
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=results, x="Player", y="Age")
    plt.title(title + "\n", fontsize=16)
    return barchart

def save_viz(barchart):
    fig = barchart.get_figure()
    fig.savefig(title + '.png')

if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data, year, weight, position)
    results = analyze(filtered)
    barchart = visualize(results)
    save_viz(barchart)