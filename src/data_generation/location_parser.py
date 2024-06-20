import pandas as pd
# from constants.states import us_state_to_abbrev
from src.constants.states import us_state_to_abbrev

# cache file IO
df_cache = None

def county_to_coord(state: str, county: str) -> tuple[int, int]:
    
    abrv = us_state_to_abbrev[state]
    
    global df_cache
    if df_cache is None:
        df_cache = load_counties()
        
    
    # result = df_cache[(df_cache['State'] == abrv) & (df_cache['County [2]'] == county)]
    result = df_cache[
        df_cache['State'].str.replace(r'\s+', '', regex=True).str.contains(abrv.replace(' ', ''), case=False) &
        df_cache['County [2]'].str.replace(r'\s+', '', regex=True).str.contains(county.replace(' ', ''), case=False)
        ]
    
    
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