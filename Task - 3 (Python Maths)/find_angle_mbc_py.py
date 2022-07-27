import math

#Hypotenuse**2 = Base**2 + Perpendicular**2
#AC2 =BC**2 +AB**2
AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2+BC**2)

theta = math.acos(BC/AC )

print(str(round(math.degrees(theta)))+'\u00B0')