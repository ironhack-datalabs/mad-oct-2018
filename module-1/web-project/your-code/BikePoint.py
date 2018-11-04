import requests
import pandas as pd
import json
from pandas.io.json import json_normalize
from math import sin, cos, sqrt, atan2, radians
import numpy as np

def getStationNames():

    response= requests.get("https://api-radon.tfl.gov.uk/BikePoint")
    response.text
    content=response.json()
    cityBikes=pd.DataFrame(content)
    print(cityBikes["commonName"])
    #print([e for e in cityBikes["commonName"]])
    
    while True:
        try:
            refStation = input('Please enter the name of the station you are at: ')
            if (str(refStation) == cityBikes["commonName"]).any():
                print("Correct")
            else:
                raise ValueError ("Wrong")   
                    
        except:
            print ("Wrong name, check your spelling ")
        else:
            print ("success")
            break
    
    refStation=refStation.split(",")[0]
    return refStation, cityBikes

def getRefStationData(refStation):

    responseStation= requests.get("https://api.tfl.gov.uk/BikePoint/Search?query="+refStation)
    contentStation=responseStation.json()
    stationDf=pd.DataFrame(contentStation)
    stationId=stationDf.loc[0,'id']
    stationLat=stationDf.loc[0,'lat']
    stationLon=stationDf.loc[0,'lon']

    return stationId, stationLat, stationLon

def calculateDistance(lati1,long1,lati2,long2):
    
    R = 6373.0

    lat1 = radians(lati1)
    lon1 = radians(long1)
    lat2 = radians(lati2)
    lon2 = radians(long2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

def obtainDistances(stationLat, stationLon, cityBikes):
    distances=[]
    coords=cityBikes [["id", 'lat','lon']]                    

    for a in coords.itertuples():
        distances.append(calculateDistance(stationLat, stationLon, a[2], a[3]))
    return distances,coords

def sortedCoords(coords):
    coords["distance"]=np.array(distances)
    coordSort=coords.sort_values("distance")
    coordSortF=coordSort.iloc[1:]
    return coordSortF

def occupancy(coordSortF):
    counter=0
    for i in coordSortF["id"]:
        response3= requests.get("https://api.tfl.gov.uk/Occupancy/BikePoints/"+str(i))
        content3=response3.json()
        occupDf=pd.DataFrame(content3)
        if int(occupDf["bikesCount"])>0:
            break
        counter+=1
    result=occupDf
    outPart1= result.loc[:,["id", "name", "bikesCount", "emptyDocks", "totalDocks"]]
    outPart1["distance"]=coordSortF.iloc[counter,3]
    finalOutput=outPart1.loc[:,["id", "name","distance","bikesCount", "emptyDocks", "totalDocks"]]
    return finalOutput


if __name__ == '__main__':
    refStation, cityBikes=getStationNames()
    stationId, stationLat, stationLon=getRefStationData(refStation)
    distances,coords=obtainDistances(stationLat, stationLon, cityBikes)
    coordSortF=sortedCoords(coords)
    print (coordSortF.head(5))
    finalOutput=occupancy(coordSortF)
    print(finalOutput)
