import numpy as np
import sympy as sy

x = sy.S('x')

x0 = []
y0 = []

y2=[]
y3=[]
y4=[]
y5=[]

anz_x = int(input('Wie viele Messwerte hast du? '))




for i in range(anz_x):
    xx = int(input("\nx für k = "+str(i)+ ":  "))
    yy = int(input('y für k = '+ str(i)+ ':  '))
    x0.append(xx)
    y0.append(yy)


def berechne():
    for i in range(len(x0)-1):
        y2.append((y0[i+1]-y0[i]) / (x0[i+1]-x0[i]))
    if len(y2) == 1:
        return(sy.expand(y0[0]  +  y2[0]*(x-x0[0])))

    for i in range(len(y2)-1):
        ebene = 1
        y3.append((y2[i+1]-y2[i]) / (x0[i+1+ebene]-x0[i]))
    if len(y3) == 1:
        return(sy.expand(y0[0]  +  y2[0]*(x-x0[0])  +  y3[0]*(x-x0[0])*(x-x0[1])))

    for i in range(len(y3)-1):
        ebene = 2
        y4.append((y3[i+1]-y3[i]) / (x0[i+1+ebene]-x0[i]))
    if len(y4) == 1:
        return(sy.expand(y0[0]  +  y2[0]*(x-x0[0])  +  y3[0]*(x-x0[0])*(x-x0[1])  +  y4[0]*(x-x0[0])*(x-x0[1])*(x-x0[2])))
    
    for i in range(len(y4)-1):
        ebene = 3
        y5.append((y4[i+1]-y4[i]) / (x0[i+1+ebene]-x0[i]))
    if len(y5) == 1:
        return(sy.expand(y0[0]  +  y2[0]*(x-x0[0])  +  y3[0]*(x-x0[0])*(x-x0[1])  +  y4[0]*(x-x0[0])*(x-x0[1])*(x-x0[2])  +  y5[0]*(x-x0[0])*(x-x0[1])*(x-x0[2])*(x-x0[3])))

result = berechne()

print(y0, y2, y3, y4, y5)
print(result)