# Important notes:
# - Counties do not occur at the same density across the US?
# - I might begin to look into normalizing the density, aswell
# - Really dense in the south
# - Less dense in the west coast
# - very sparse in Alaska
# - After normalizing instead of dropping, much more topographic looking data

import pandas as pd
import vtk
import numpy as np
data = pd.read_csv('data/cleaned/energy_usage.csv')
data = pd.read_csv('data/cleaned/energy_usage.csv')

# Group by 'State' and 'County' and calculate mean of 'Consumption MMBtu'
consumption_mean = data.groupby(['State', 'County'])['Consumption MMBtu'].mean().reset_index()

# Merge the mean consumption back with the original data to keep the latitude and longitude
merged_data = pd.merge(data, consumption_mean, on=['State', 'County'], suffixes=('', '_mean'))

# Drop duplicates to keep unique rows for visualization (in case of multiple lat/long for same state and county)
unique_data = merged_data.drop_duplicates(subset=['State', 'County'])

# Select relevant columns
filtered_data = unique_data[['State', 'County', 'Latitude', 'Longitude', 'Consumption MMBtu_mean']]
filtered_data.rename(columns={'Consumption MMBtu_mean': 'Consumption MMBtu'}, inplace=True)

latitudes = filtered_data['Latitude'].to_list()
longitudes = filtered_data['Longitude'].to_list()
consumptions = filtered_data['Consumption MMBtu'].to_list()

# 10 is good for visualization
# 1 might be better for compatability
scale_factor = 10 

# scale down points, this was the problem
consumptions_scaled = np.array(consumptions) / np.max(consumptions) * scale_factor
for val in consumptions_scaled:
    print(val)


points = vtk.vtkPoints()
for lat, lon, consumption in zip(latitudes, longitudes, consumptions_scaled):
    print(lon, lat, consumption)
    points.InsertNextPoint(lon, lat, consumption)

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)


vertex_filter = vtk.vtkVertexGlyphFilter()
vertex_filter.SetInputData(polydata)
vertex_filter.Update()


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(vertex_filter.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetPointSize(1)  


renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

black = (0, 0, 0)
renderer.AddActor(actor)
renderer.SetBackground(black)  
renderer.ResetCamera()

render_window.Render()
render_window_interactor.Start()
