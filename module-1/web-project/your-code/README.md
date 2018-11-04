# WEB-PROJECT 1-2 November 2018
This project is divided in 2 parts:<br>
[1. SPACEX API](#part-1-\--spacex-api) <br>
<br>
[2. Webscraping Filmaffinity and IMDB](#PART-2-\--Webscraping-Filmaffinity-and-IMDB) <br>
<br>

____
## PART 1 - SPACEX API
This program consists on using a notebook or script (with Python) to retrieve Data with an API. In my case I was looking for a free API with some space data. Suddenly I found the **SPACE X API**. Rocket Science is alway cool so I choose this API. It has many data about SPACEX boosters, capsules, upcoming launches and even updated **Starman** position data .<br>
I have developed this programm in a **jupyter notebook** file called *SPACE-X API.ipynb* to easy handle the workflow in the initial stage and finally I have developed a script in python to automatize its tasks with crontab in section **1.6**
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

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

[Back to Header](#web\-project-1\-2-november-2018)
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
In this [API info link](https://documenter.getpostman.com/view/2025350/RWaEzAiG) all info above and how to access to other kind of information and its organization
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

___
### 1.3 - SpaceX Company Info
Using this url https://api.spacexdata.com/v3/info we can get the info about the company, CEO, CEE, employees, ... using python to retrieve the data and saving it as a CSV<br><br>
Once retrieved, if we try to do the request again it will be stopped or ignored if the CSV file for SpaceX info already exists.
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

___
### 1.4 - SpaceX Upcoming Launchs
Using this url https://api.spacexdata.com/v3/launches/upcoming we can get all types of info for upcoming launchs. With this request we can follow SpaceX tracks and its re-usage of its boosters using python to retrieve the data and saving it as a CSV<br><br>
Once retrieved, if we try to do the request again it will be stopped or ignored if the CSV file for SpaceX info already exists.<br><br>
We could also retrieve the info about past launches to compare the evolution of re-usable boosters and refubrisment. It is important to remark that there is a los of types of optional querystrings available.<br><br>
In this retrieved data I have found 2 attributes with multiple nested lists and dictionaries. To solve this problem I have use several loops to simplify the data and added it to the data frame
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

___
### 1.5 - Starman Live Information
It might be interesting to retrieve information about Actual Starman Orbit. We can request this info using the following link https://api.spacexdata.com/v3/roadster. Once retrieved we check if the existing starman csv file halready has the retrieved info, might be possible to retrieve the same info from 10 mins ago, depending on your sincronization with refreshing date of SpaceX.<br><br>
The SpaceX refreshing date is 10 mins per iteration. With this info you could track its position and might avoid a interestellar crash with your imaginary spaceship and Starman Roadster.<br><br>
I have plans to create a script to automatize this whole process with **crontab**.
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

![Starman](https://farm5.staticflickr.com/4702/40110298232_91b32d0cc0_b.jpg)
<br>

___
### 1.6 - DATA RETRIEVE AUTOMATIZATION FROM SPACEX API
**Not finished Yet**
For this purpouse I have created python script called SPACEX_data.py and open crontab to define the automatization of the process. <br><br>
To automatize the process in crontab we type the next command in our bash connsole:
```
$ crontab -e
```
And define the parameters for crontab:
```
*/20 * * * * python3 SPACEX_data.py
```
This command will execute the python3 script every 20 min. I have chosen this refresh frequency due to the SpaceX refresh frequency is of 10 minutes.
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

____
## PART 2 - Webscraping Filmaffinity and IMDB
For this part of the project I have decided that the main goal of mines is going to analyze the TOP 30 TV Series of all times for 2 ranking Webpages.<br><br>
These are going to be **Filmaffinity** and **IMDB**<br><br>
We are going to use the next modules:
```
import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml.html import fromstring
import re,os
import pandas as pd
import numpy as np
```
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

___
### 2.1 - Filmaffinity
We will make a request to the next webpage to retrieve the TOP 30 TV Series from Filmaffinity:
```
https://www.filmaffinity.com/es/topgen.php?genre=TV_SE&country=&fromyear=&toyear=&nodoc
```
<br>
Using Beautifulsoup tool I read the request and filter it to obtain the Title, Type, Year, Country, Average rating from users and total amount of votes. The result will be storaged into a DataFrame.<br><br>
Next step is to make an *on the fly* analysis to get a general summary of TV series by Country. Results will be storaged into a DataFrame.<br><br>
Finally I save both dataframes into CSV files.

<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

____
### 2.2 - IMDB
Same as for the case above, but in this case we obtain the TOP 100, so we limit that to 30 items to have the same length that in Filmaffinity Data Frame. URL for IMDB is:
```
https://www.imdb.com/list/ls004729995/
```
Once obtained the data for the TOP 30 TV Series for IMDB we proceed to concatenate it with the one obtained by columns.<br><br>
The final comparision is about merging both data frames, TOP 10 IMDB and TOP 10 Filmaffinity, by Title. Before this final step I have normalized all names to avoid duplicates.<br><br>
This last dataframes are also saved in local storage.
<br><br>
[Back to Header](#web\-project-1\-2-november-2018)
<br>

____

Follow my repository updates to get the status of this project :wink: and do not hesitate on leaving your comments, ideas and feedback :smile: !!