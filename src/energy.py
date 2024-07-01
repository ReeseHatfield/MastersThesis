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



def main():
    
    data = pd.read_csv('data/cleaned/cleaned_energy_usage_continental.csv')
    
    # get a col of just the mean
    consumption_mean = data.groupby(['State', 'County'])['Consumption MMBtu'].mean().reset_index()

    # then merge that into the main dataset
    merged_data = pd.merge(data, consumption_mean, on=['State', 'County'], suffixes=('', '_mean'))

    consumptions = merged_data['Consumption MMBtu_mean'].to_list()

    # 10 is good for vis, 1 may be better for other stuff
    scale_factor = 50
    consumptions_scaled = np.array(consumptions) / np.max(consumptions) * scale_factor

    # consumptions_scaled = drop_non_continental(consumptions_scaled)


    latitudes = merged_data['Latitude'].to_list()
    longitudes = merged_data['Longitude'].to_list()

    points = vtk.vtkPoints()
    for lat, lon, consumption in zip(latitudes, longitudes, consumptions_scaled):
        # print(lon, lat, consumption)
        points.InsertNextPoint(lon, lat, consumption)

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)


    # vertex_filter = vtk.vtkVertexGlyphFilter()
    # vertex_filter.SetInputData(polydata)
    # vertex_filter.Update()


    # mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(vertex_filter.GetOutputPort())

    # using 2d works better, find out why before wednesday
    delaunay = vtk.vtkDelaunay2D()
    delaunay.SetInputData(polydata)
    delaunay.Update()

    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputConnection(delaunay.GetOutputPort())

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


if __name__ == "__main__":
    main()