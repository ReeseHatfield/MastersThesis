import pandas as pd
import vtk
import numpy as np

data = pd.read_csv('data/cleaned/energy_usage.csv')

# drop duplicate county, will make this an average later
filtered_data = data.drop_duplicates(subset=['County'])


latitudes = filtered_data['Latitude'].to_list()
longitudes = filtered_data['Longitude'].to_list()
consumptions = filtered_data['Consumption MMBtu'].to_list()

# scale down points, this was the problem
consumptions_scaled = np.array(consumptions) / np.max(consumptions) * 10  


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
actor.GetProperty().SetPointSize(10)  # can change point size as needed


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
