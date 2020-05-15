import rhinoscriptsyntax as rs
import math as ma


id = rs.GetObject("Select a point",1)
point0 = rs.PointCoordinates(id)

z=0
for theta in rs.frange(0,ma.pi*2,ma.pi/12):
    vec = [5* ma.cos(theta),5 * ma.sin(theta),z]
    point = rs.PointAdd(point0,vec)
    rs.AddPoint(point)
    z=z+1
