import pandas as pd
import json
import requests
import webbrowser

IP = input("Enter the IP: ")

response = requests.get("https://ipinfo.io/"+IP+"/geo")
results = response.json()
df = pd.DataFrame(results, index=[""])
loc = df["loc"]
a = loc.to_string()
webbrowser.open("https://www.google.com/maps/search/?api=1&query=" + a)