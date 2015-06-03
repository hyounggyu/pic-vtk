import vtk

def readline_in_chunks(file_object, chunk_size=4096):
  buf = ''
  while True:
    data = file_object.read(chunk_size)
    if not data:
      break
    buf = buf + data
    while True:
      pos = buf.find('\n')
      if pos < 0:
        break
      yield buf[:pos]
      buf = buf[pos+1:]

def main():
  f = open('data/particle_sp3_rnk3_step4000', 'r')

  points = vtk.vtkPoints()
  vertices = vtk.vtkCellArray()
  depth = vtk.vtkDoubleArray()
  depth.SetName('DepthArray')

  pos_min = pos_max = 0
  for line in readline_in_chunks(f):
    pos = [ float(v) for v in line.strip().split()[:3] ]
    if pos[1] > pos_max:
      pos_max = pos[1]
    elif pos[1] < pos_min:
      pos_min = pos[1]
    pid = points.InsertNextPoint(pos)
    depth.InsertNextValue(pos[1])
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(pid)
  print (pos_min, pos_max)

  point = vtk.vtkPolyData()
  point.GetPointData().SetScalars(depth)
  point.GetPointData().SetActiveScalars('DepthArray')
  point.SetPoints(points)
  point.SetVerts(vertices)

  mapper = vtk.vtkPolyDataMapper()
  mapper.SetInput(point)
  mapper.SetColorModeToDefault()
  mapper.SetScalarRange(0.0, 0.00004)
  mapper.SetScalarVisibility(1)

  actor = vtk.vtkActor()
  actor.SetMapper(mapper)
  actor.GetProperty().SetPointSize(1)

  renderer = vtk.vtkRenderer()
  renderer.AddActor(actor)
  renderer.SetBackground(.2, .3, .4)
  renderer.ResetCamera()

  renderWindow = vtk.vtkRenderWindow()
  renderWindow.AddRenderer(renderer)
  renderWindowInteractor = vtk.vtkRenderWindowInteractor()
  renderWindowInteractor.SetRenderWindow(renderWindow)
  renderWindow.Render()
  renderWindowInteractor.Start()

if __name__ == '__main__':
  main()
