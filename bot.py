import requests
from time import sleep
from datetime import datetime
Interval = 5
Registered = {}

# Results currently = 10
URL = 'https://search.roblox.com/catalog/json?SortType=3&ResultsPerPage=10&CreatorID=1'
WBUrl = 'https://discord.com/api/webhooks/854620225445560320/x5TTZDFuEIFNcZVIqI54o8GG6fL26cok4wFGgXkJc0rDcQdjClsGHljwUh7NR_wBgfm_'
URL2 = 'https://search.roblox.com/catalog/json?CatalogContext=2&Category=6&SortType=3&ResultsPerPage=1'

while True :
    Response = requests.get(URL)
    if Response.status_code == 200:
        Response = Response.json()
        try:
            for Asset in Response:
                ID = Asset['AssetId']
                Name = Asset['Name']
                Desc = Asset['Description']
                URL = Asset['AbsoluteUrl']
                s = Asset['UpdatedDate']
                Date = s[s.find("(")+1:s.find(")")]
                Date = int(Date)
                if Registered.get(ID) != None and Registered[ID] == Date:
                    break
                StrData = Date/1000
                StrData = datetime.fromtimestamp(StrData).isoformat()

                Data = {
                    "content" : "An asset has been updated. @everyone",
                    "username" : "Update bot"
                }

                Data['embeds'] = [
                    {
                    "title" : Name,
                    "description" : "ID : " + str(ID),
                    "url" : URL,
                    "timestamp" : StrData
                    },
                ]
                
                requests.post(WBUrl,json=Data)
                Registered[ID] = Date
        except Exception as e:
            print(e)
    sleep(Interval)
