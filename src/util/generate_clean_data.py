import pandas as pd
from location_parser import county_to_coord

def main() -> None:
    consumption_filepath: str = "data/consumption/energy_consumption_by_county.csv"
    generation_filepath: str = "data/cleaned/generation.csv"
    
    # Read the consumption and generation CSV files
    consumption_df = pd.read_csv(consumption_filepath)
    generation_df = pd.read_csv(generation_filepath)
    
    # Merge the two DataFrames on State Name and County Name
    merged_df = pd.merge(consumption_df, generation_df, on=['State Name', 'County Name'], how='left')
    
    cleaned_file = open('data/cleaned/energy_usage.csv', 'w')
    
    # Write the header row
    first_row = "State,County,Latitude,Longitude,Consumption MMBtu,Expenditure US Dollars,Technical Generation Potential MWh\n"
    cleaned_file.write(first_row)
    
    for _, row in merged_df.iterrows():
        cur_state = row['State Name']
        cur_county = row['County Name']
        
        lat, lon = county_to_coord(cur_state, cur_county)
        
        if lat is None or lon is None:
            print(f"Could not find coords for {cur_state}, {cur_county}")
            continue
        
        consumption = row['Consumption MMBtu']
        expenditure = row['Expenditure US Dollars']
        generation = row['Technical Generation Potential - MWh MWh']
        
        new_row = f"{cur_state},{cur_county},{lat},{lon},{consumption},{expenditure},{generation}\n"
        cleaned_file.write(new_row)
    
    cleaned_file.close()

if __name__ == "__main__":
    main()
