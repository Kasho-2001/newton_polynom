import numpy as np
import sympy as sy

x = sy.S('x')

x0 = []
y = []

y2=[]
y3=[]
y4=[]
y5=[]

anz_x = int(input('Wie viele Messwerte hast du? '))


y0 =[]

for i in range(anz_x):
    xx = float(input("\nx für k = "+str(i)+ ":  "))
    yy = float(input('y für k = '+ str(i)+ ':  '))
    x0.append(xx)
    y0.append(yy)
y.append(y0)


def berechne():
    for ebene in range (anz_x):
        y_temp = []
        for i in range(len(y[ebene])-1):
            y_temp.append((y[ebene][i+1]-y[ebene][i]) / (x0[i+1+ebene]-x0[i]))
        y.append(y_temp)
        if len(y[ebene+1]) == 1:
            #print(y[1][0])
            result = y[0][0]
            mg = 1
            for i in range(ebene+1):
                mg = sy.expand(mg * (x-x0[i]))
                result = sy.expand(result + y[i+1][0] * mg)
            return(result)


result = berechne()

print("\nErgebnis: \n",result)