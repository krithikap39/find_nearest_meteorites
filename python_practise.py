import requests
import math

response=requests.get('https://data.nasa.gov/resource/y77d-th95.json')
data=response.json()
print(type(data))

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_key(item):
    return(item["proximity"])
#return(item.get('proximity',math.inf))

for item in data:
    if "reclat" in item and "reclong" in item:
        lat=float(item.get("reclat"))
        longt=float(item.get("reclong"))
        distance=calc_dist(13.08268,80.270718,lat,longt)
        item["proximity"]=distance
    else:
        item["proximity"]=math.inf
    
for item in data:
    data.sort(key=get_key)  
        
print(data[0])
print(data[0]['reclat'])
print(data[0:10])
data[0].get('proximity',math.inf)
data[-1:-11:-1]
len(data)
# iterate over the list and compute length of list whose items dont have a key named proximity
len([m for m in data if 'proximity' not in m])
data_inf=data[-1:-11:-1]
print(len(data_inf))


        
#TO access a particular key value from the dictionary directly using data which is a list that contains dictionary values, use data[0]['reclat']
        

