import rhinoscriptsyntax as rs

point1 = rs.GetObject("Select first point",1)
point2 = rs.GetObject("Select Second point",1)

p1 = rs.PointCoordinates(point1)
p2 = rs.PointCoordinates(point2)
dist = rs.Distance(p1,p2)

print(p1)
print(p2)
print(dist)
