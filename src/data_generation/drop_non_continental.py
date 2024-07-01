
import pandas as pd

def drop_non_continental(data: pd.DataFrame):
    
    state_idx = 0
    
    index_to_drop = []
    states_to_drop = [
        'Alaska',
        'Hawaii'
    ]
    
    
    for i, row in data.iterrows():
        if row[state_idx] in states_to_drop:
            index_to_drop.append(i)
    
    print("droping: ")
    print(index_to_drop)
    
    for index in index_to_drop:
        data = data.drop(index)
        
    return data



def main():
    data = pd.read_csv('data/cleaned/energy_usage.csv')
    
    print(data)
    data = drop_non_continental(data)
    
    data.to_csv('data/cleaned_energy_usage_continental.csv')
    
    
if __name__ == "__main__":
    main()