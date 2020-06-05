import rhinoscriptsyntax as rs

curve = rs.GetObject("Select a Curve",4)

domain = rs.CurveDomain(curve)
start  = domain[0]
end = domain[1]
increment = (domain[1]-domain[0])/20
for t in rs.frange(start ,end ,increment):
    point1 = rs.EvaluateCurve(curve,t)
    rs.AddPoint(point1)

    tangent=rs.CurveTangent(curve,t)
    if tangent:
        tangent = rs.VectorUnitize(tangent)
        tangent = rs.VectorScale(tangent,5)
        point2 = rs.PointAdd(point1,tangent)
        rs.AddLine(point1,point2)
    normal = rs.CurveNormal(curve,t)
    if normal:
        normal = rs.VectorUnitize(normal)
        normal = rs.VectorScale(normal,5)
        point3 = rs.PointAdd(point1,normal)
        rs.AddLine(point1,point3)
    if normal:
        normal2 = rs.VectorCrossProduct(tangent,normal)
        normal2 = rs.VectorUnitize(normal2)
        normal2 = rs.VectorScale(normal2,5)
        point4 = rs.PointAdd(point1,normal2)
        rs.AddLine(point1,point4)
