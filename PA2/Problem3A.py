temp = 0
listx = list()
listy = list()

listx #insert for x0 - xn
listy #insert for f(x0) - f(xn)

#listx = [.9,1.3,1.9,2.1,2.6,3,3.9,4.4,4.7,5,6,7,8,9.2,10.5,11.3,11.6,12,12.6,13,13.3]  #insert for x0 – xn
#listy = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,.9,.7,.6,.5,.4,.25]  #insert for f(x0) – f(xn)

inputNum = listx.__len__()

xlist = [0] * inputNum
alphalist = [0] * inputNum
Llist = [0] * inputNum
Llist[0] = 1
Llist[inputNum-1] = 1 
ulist = [0] * inputNum
ulist[0] = 0 
zlist = [0] * inputNum
zlist[0] = 0 
zlist[inputNum-1] = 0 

b = [0] * inputNum
c = [0] * inputNum
c[inputNum-1] = 0
d = [0] * inputNum

while(inputNum-1 != 0):
  xlist[temp] = listx[temp+1] - listx[temp]
  if(inputNum-2 != 0):
    xlist[temp+1] = listx[temp+2] - listx[temp+1]
    alphalist[temp+1] = ((3/xlist[temp+1])*(listy[temp+2] - listy[temp+1])) - ((3/xlist[temp])*(listy[temp+1] - listy[temp]))
  if(inputNum-2 != 0):
    Llist[temp+1] = 2*(listx[temp+2] - listx[temp]) - (xlist[temp] * ulist[temp])
    ulist[temp+1] = xlist[temp+1] / Llist[temp+1]
    zlist[temp+1] = (alphalist[temp+1] - (xlist[temp] * zlist[temp])) / Llist[temp+1]
  inputNum = inputNum - 1
  temp = temp + 1 
  
inputNum = listx.__len__()
temp = 0 

while (inputNum-1 != 0):
  c[inputNum-2] = zlist[inputNum-2] - (ulist[inputNum-2]*c[inputNum-1])
  b[inputNum-2] = ((listy[inputNum-1] - listy[inputNum-2])/(xlist[inputNum-2])) - ((xlist[inputNum-2]) * ((c[inputNum-1] + (2*c[inputNum-2]))/3))
  d[inputNum-2] = (c[inputNum-1] - c[inputNum-2]) / (3*xlist[inputNum-2])
  inputNum = inputNum-1
  temp = temp+1
  print("For n:" + str(inputNum-1) + ", our a" + str(inputNum-1) + ":" + str(listy[inputNum-1]))
  print("For n:" + str(inputNum-1) + ", our b" + str(inputNum-1) + ":" + str(b[inputNum-1]))
  print("For n:" + str(inputNum-1) + ", our c" + str(inputNum-1) + ":" + str(c[inputNum-1]))
  print("For n:" + str(inputNum-1) + ", our d" + str(inputNum-1) + ":" + str(d[inputNum-1]))