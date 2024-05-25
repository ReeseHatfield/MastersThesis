import dask.dataframe as dd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box

SHAPE_FILE_PATH ='shapes/ne_10m_admin_1_states_provinces.shp'
DATA_PATH = 'data/consumption/energy_consumption_by_country.csv'


# vtk geovisualization

def main():
    # https://towardsdatascience.com/plotting-maps-with-geopandas-428c97295a73
    # https://medium.com/@jl_ruiz/plot-maps-from-the-us-census-bureau-using-geopandas-and-contextily-in-python-df787647ef77
    
    # Load the data using dask
    full_df = dd.read_csv(DATA_PATH)

    # get just useful columns from df
    numeric_df = full_df[['State Name', 'Consumption MMBtu', 'Expenditure US Dollars']]
    
    # group them by state for geomapping
    df = numeric_df.groupby('State Name').mean().compute().reset_index()
    
    us_states = getContinentalUnitedStates()
    
    
    

    # us states is just a pd dataframe, name is the column we wnat
    merged = us_states.set_index('name').join(df.set_index('State Name'))

    # Plot the data on a map
    plot(merged)
    


def getContinentalUnitedStates():
    num_rows = 4596
    xmin = -200
    ymin = 20
    xmax = 50
    ymax = 100
    crs_bounding_box = (xmin, ymin, xmax, ymax)
    # num_rows = 4000
    us_states = gpd.read_file(SHAPE_FILE_PATH, rows=num_rows, bbox=crs_bounding_box)
    # us_states = gpd.read_file(SHAPE_FILE_PATH, rows)
    print(us_states)
    return us_states
    
    # non_continental_states = ['HI','VI','MP','GU','AK','AS','PR']
    
    

def plot(merged):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged.plot(column='Consumption MMBtu', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    plt.title('Average Energy Consumption by State')
    plt.show()

    # 1 row, 1 col plot of map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged.plot(column='Expenditure US Dollars', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    plt.title('Average Expenditure by State')
    plt.show()
    

if __name__ == '__main__':
    main()

