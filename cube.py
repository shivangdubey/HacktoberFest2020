def cube(a):
    area=6*(a**2)
    vol=a**3
    return(area,vol)
a=int(input("enter the size of the edge:"))
ar,v=cube(a)
print("surface area of the cube:=",ar)
print("volume of the cube:",v)
