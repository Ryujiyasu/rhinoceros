import rhinoscriptsyntax as rs
import math as ma


r = 10.0
h = 20.0

points=[]
for k in rs.frange(0,1,0.01):
    theta = k * ma.pi * 4
    x = r * ma.cos(theta)
    y = r * ma.sin(theta)
    z = h * k
    points.append((x,y,z))

rs.AddCurve(points)
