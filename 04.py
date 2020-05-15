import rhinoscriptsyntax as rs
import math as ma


id = rs.GetObject("Select a point",1)
point0 = rs.PointCoordinates(id)

for z in rs.frange(0,100,1):
    for theta in rs.frange(0,ma.pi*2,ma.pi/120):
        vec = [z* ma.cos(theta),z * ma.sin(theta),5*theta]
        point = rs.PointAdd(point0,vec)
        rs.AddPoint(point)
