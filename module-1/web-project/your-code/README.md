# WEB-PROJECT 1-2 November 2018
______
______
## PART 1 - SPACE X API
This program consists on using a notebook or script (with Python) to retrieve Data with an API. In my case I was looking for a free API with some space data. Suddenly I found the **SPACE X API**. Rocket Science is alway cool so I choose this API. It has many data about SPACEX boosters, capsules, upcoming launches and even updated **Starman** position data .

___
### 1.1 - Necessary modules:
```
import requests
from pandas.io.json import json_normalize
import pandas as pd
import os,datetime
import numpy as np
```
<br>

___
### 1.2 - API
**SpaceX** API is totally free, so any user can access to it and retrieve interesting information like lanches (Past and Future)...<br>
API url as follows:
```
https://api.spacexdata.com
```
The [SpaceX-repository](https://github.com/r-spacex) in GitHub<br><br>
**Rate Limiting**<br>
The API has a rate limit of 50 req/sec per IP address, if exceeded, a response of 429 will be given until the rate drops back below 50 req/sec.<br><br>

**More API info**<br>
In this [API info link](https://documenter.getpostman.com/view/2025350/RWaEzAiG) all info above and how to access to other kind of information and its organization<br><br>

___
### 1.3 - SpaceX Company Info
Using this url https://api.spacexdata.com/v3/info we can get the info about the company, CEO, CEE, employees, ... using python to retrieve the data and saving it as a CSV<br><br>
Once retrieved, if we try to do the request again it will be stopped or ignored if the CSV file for SpaceX info already exists.<br>

___
### 1.4 - SpaceX Upcoming Launchs
Using this url https://api.spacexdata.com/v3/launches/upcoming we can get all types of info for upcoming launchs. With this request we can follow SpaceX tracks and its re-usage of its boosters using python to retrieve the data and saving it as a CSV<br><br>
Once retrieved, if we try to do the request again it will be stopped or ignored if the CSV file for SpaceX info already exists.<br><br>
We could also retrieve the info about past launches to compare the evolution of re-usable boosters and refubrisment. It is important to remark that there is a los of types of optional querystrings available.<br><br>
In this retrieved data I have found 2 attributes with multiple nested lists and dictionaries. To solve this problem I have use several loops to simplify the data and added it to the data frame<br>

___
### 1.5 - Starman Live Information
It might be interesting to retrieve information about Actual Starman Orbit. We can request this info using the following link https://api.spacexdata.com/v3/roadster. Once retrieved we check if the existing starman csv file halready has the retrieved info, might be possible to retrieve the same info from 10 mins ago, depending on your sincronization with refreshing date of SpaceX.<br><br>
The SpaceX refreshing date is 10 mins per iteration. With this info you could track its position and might avoid a interestellar crash with your imaginary spaceship and Starman Roadster.<br><br>
I have plans to create a script to automatize this whole process with **crontab**. Follow my repository updates to get the status of this project :wink:

![Starman](https://farm5.staticflickr.com/4702/40110298232_91b32d0cc0_b.jpg)