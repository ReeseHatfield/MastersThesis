import pandas as pd


def main():
    
    filename = "data/generation/generation_by_county.csv"
    
    df = pd.read_csv(filename)
    
    # groupy must pass array if preserving state and county
    grouped_df = df.groupby(['State Name', 'County Name'])['Technical Generation Potential - MWh MWh'].sum().reset_index()
    
    output_file = "data/cleaned/generation.csv"
    
    grouped_df.to_csv(output_file, index=False)
    
    # print(df)
    
    


if __name__ == "__main__":
    main()