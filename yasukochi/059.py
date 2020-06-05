import rhinoscriptsyntax as rs
import random as rd

curve = rs.GetObject("Select a Curve",4)

if curve:
    points = rs.CurvePoints(curve)
    knots = rs.CurveKnots(curve)
    degree = rs.CurveDegree(curve)

    newpoints=[]
    for p in points:
        dx = rd.randrange(0,10)
        dy = rd.randrange(0,10)
        dz = rd.randrange(0,10)
        d = [dx,dy,dz]
        q = rs.PointAdd(p,d)
        newpoints.append(q)

    newcurve = rs.AddNurbsCurve(newpoints,knots,degree)
