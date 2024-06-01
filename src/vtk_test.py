import vtk
from util.location_parser import county_to_coord

from vtk import vtkGeoJSONReader
# missing https://vtk.org/doc/nightly/html/classvtkReebGraph.html

a = vtk.vtkAppendFilter()

print(vtk.__version__) # -> 9.3.0


# https://examples.vtk.org/site/PythonicAPIComments/ -> 

# https://vtk.org/download/ -> 9.3.2


#9.1.0

def main():
    print(county_to_coord("Ohio","Ross"))

if __name__ == "__main__":
    main()