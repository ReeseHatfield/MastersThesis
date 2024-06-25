import numpy as np
import pandas as pd

def main():
    
    path = "data/cleaned/energy_usage.csv"
    df = pd.read_csv(path)
    # df.columns = [c.replace(' ', '_') for c in df.columns]
    
    df.groupby(['State', 'County']).mean(numeric_only=True)  
    
    
    print(df)
    

if __name__ == "__main__":
    main()