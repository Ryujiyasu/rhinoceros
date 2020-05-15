import rhinoscriptsyntax as rs



curve = rs.GetObject("Select a curve",4)
length = rs.CurveLength(curve)
domain = rs.CurveDomain(curve)
t = (domain[1]- domain[0])/2

midpoint = rs.EvaluateCurve(curve,t)
tangent = rs.CurveTangent(curve,t)
normal = rs.CurveNormal(curve,t)

print("length:"+str(length))
print("domain ="+str(domain[0])+str(domain[1]))
print("co-ordinates of midpoint = "+str(midpoint))
print("tangent vector = " +str(tangent))
print("normal vector = "+str(normal))
