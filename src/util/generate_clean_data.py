import pandas as pd
from location_parser import county_to_coord

def main() -> None:
    filepath: str = "data/consumption/energy_consumption_by_county.csv"
    
    full_df = pd.read_csv(filepath)
    
    cleaned_file = open('data/cleaned/energy_usage.csv', 'w')
    
    
    first_row = "State,County,Latitude,Longitude,Consumption MMBtu,Expenditure US Dollars\n"
    cleaned_file.write(first_row)
    
    for _, row in full_df.iterrows():
        
        cur_state = row['State Name']
        cur_county = row['County Name']
        
        lat, lon = county_to_coord(cur_state, cur_county)
        
        if lat == None or lon == None:
            print(f"Could not find coords for {cur_state}, {cur_county}")
        
        consumption = row['Consumption MMBtu']
        
        expenditure = row['Expenditure US Dollars']
        
        new_row = f"{cur_state},{cur_county},{lat},{lon},{consumption},{expenditure}\n"
        
        cleaned_file.write(new_row)
        
        
    


if __name__ == "__main__":
    main()