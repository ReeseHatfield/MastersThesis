import pandas as pd

# cache file IO
df_cache = None

def county_to_coord(state: str, county: str) -> tuple[int, int]:
    global df_cache
    if df_cache is None:
        df_cache = load_counties()
        
    
    result = df_cache[(df_cache['State'] == state) & (df_cache['County [2]'] == county)]
    
    if result.empty:
        return None, None
    
    lat = result.iloc[0]['Latitude']
    lon = result.iloc[0]['Longitude']
    
    # fix sign error, US only
    lon = float(f"-{lon}")
    
    return lat, lon
    


def load_counties():
    filepath = "data/wikipedia/counties.csv"
    df = pd.read_csv(filepath)
    
    cleaned_df = df[['State', 'County [2]', 'Latitude', 'Longitude']]
    
    return cleaned_df
    


# if __name__ == "__main__"():
#     load_counties()