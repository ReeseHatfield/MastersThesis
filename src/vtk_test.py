import vtkmodules.all as vtk

def geojson_to_polydata(filename):
    reader = vtk.vtkGeoJSONReader()
    reader.SetFileName(filename)
    reader.Update()
    return reader.GetOutput()

def main():
    filename = 'data/geo/USA_Counties_465634642118668778.geojson'

    polydata = geojson_to_polydata(filename)

    
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)

    
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    
    renderer = vtk.vtkRenderer()
    window = vtk.vtkRenderWindow()
    
    
    window.AddRenderer(renderer)
    window.SetWindowName('GEOJSON stuff')

    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(window)
    
    renderer.AddActor(actor)
    renderer.SetBackground(0.0, 0.0, 0.0) 

    window.Render()
    render_window_interactor.Initialize()
    render_window_interactor.Start()
    
if __name__ == '__main__':
    main()
