import vtk

# Print VTK version
print("VTK version:", vtk.vtkVersion.GetVTKVersion())

# Create a cube source
cubeSource = vtk.vtkCubeSource()
cubeSource.SetXLength(5.0)
cubeSource.SetYLength(5.0)
cubeSource.SetZLength(5.0)

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cubeSource.GetOutputPort())

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)  # Background color

# Create a render window
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(800, 600)

# Create a render window interactor
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Initialize and start the render window interactor
renderWindow.Render()
renderWindowInteractor.Initialize()
renderWindowInteractor.Start()
