import rhinoscriptsyntax as rs
import math as ma

rs.AddPoint(0,0,0)

for x in rs.frange(0,20,1):
    rs.AddPoint(x,0,5)


for x in rs.frange(0,20,1):
    y = 5 * ma.sin(ma.pi * x/10)
    rs.AddPoint(x,y,10)
