# sources:
# https://medium.com/@kudlamolka/scrap-data-from-wikipedia-table-to-csv-file-using-python-b5af7a6c858f

from bs4 import BeautifulSoup
import requests
import pandas as pd



def main():
    table_url = "https://en.wikipedia.org/wiki/User:Michael_J/County_table"
    
    res = requests.get(table_url)
    
    html = BeautifulSoup(res.text, 'html.parser')
    
    classes = "wikitable sortable"
    table_html = html.find('table', attrs={'class':classes})
    
    # lose sign of lat/long here because wikipedia 
    # uses the unicode plus not the normal"+"
    table_html_string = remove_unicode(str(table_html))
    
    # read_html gives list of dfs, only want 0
    df = pd.read_html(table_html_string)[0]
    
    
    df.to_csv("data/wikipedia/counties.csv")
    print(df)
    
    # print(table_html)
    


def remove_unicode(s: str):
    
    ascii_max = 123
    ascii_s = ""
    
    for char in s:
        if ord(char) < ascii_max:
            ascii_s += char
            
    
    return ascii_s



if __name__ == "__main__":
    main()