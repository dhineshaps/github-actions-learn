import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time



def scrap(sector,urls,df):
    url = urls
    #df[sector] = []
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
          soup = BeautifulSoup(response.text, "html.parser")
    else:
        print(response.status_code)

    #print(response.status_code)

    #print(soup)
    table = soup.find("table", {"id": "refineriesTable"})
    if table:
        tbody = table.find("tbody") 
        if tbody:
            values = []
            for row in tbody.find_all("tr"):
                columns = row.find_all('td')
                if(columns!= []):
                    sec_val = columns[0].text.strip()
                    sec_val_handle = sec_val.split(" ")[-1]
                    if(sec_val_handle == "LTD."):
                        new_sec_val = sec_val.replace(sec_val_handle,"LTD")
                        values.append(new_sec_val)
                    else:
                    #print(sec_val)
                        values.append(sec_val)
            max_rows = max(len(df), len(values))
            df = df.reindex(range(max_rows)) 

            if sector not in df.columns:
                df[sector] = None

            df.loc[:len(values)-1, sector] = values

                    # if sector not in df.columns:
                    #     df = df.assign(**{sector: None})                      
                    # new_row = pd.DataFrame([{sector: sec_val}])
                    # df = pd.concat([df, new_row], ignore_index=True)
 

                    #df = df._append({sector:sec_val},ignore_index=True)
                    #df = pd.concat([df, pd.DataFrame([{sector: sec_val}])], ignore_index=True)
    #print(df)
    return df


df = pd.DataFrame()

f = open("url_links_sector.txt", "r")

for line in f:
    time.sleep(6)
    sector = line.strip().split("/")[5].capitalize()
    df = scrap(sector,line.strip(),df)
    # print(line.strip().split("/")[5])

print(df)

df.to_csv('ops.csv')
