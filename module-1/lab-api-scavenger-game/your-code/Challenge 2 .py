url_inic = "https://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/commits"
response2 = requests.get(url_inic + "?since=2018-10-20T00:00:00Z&until=2018-10-25T23:59:59Z&per_page=100")
results2 = response2.json()
flattened2 = json_normalize(results2)
data2 = pd.DataFrame(flattened2)
count = (data2["commit.committer.date"]).count()
print(count)