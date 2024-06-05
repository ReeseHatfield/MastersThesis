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
    
    renderer.AddActor(actor)
    renderer.SetBackground(0.0, 0.0, 0.0) 

    interacter = vtk.vtkRenderWindowInteractor()
    interacter.SetRenderWindow(window)

    window.Render()
    interacter.Initialize()
    interacter.Start()
    
if __name__ == '__main__':
    main()
