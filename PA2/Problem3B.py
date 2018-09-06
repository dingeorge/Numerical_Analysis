temp = 0
listx = list()
listy = list()

listx = [.9,1.3,1.9,2.1,2.6,3,3.9,4.4,4.7,5,6,7,8,9.2,10.5,11.3,11.6,12,12.6,13,13.3] #insert for x0 – xn
listy = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,.9,.7,.6,.5,.4,.25] #insert for f(x0) – f(xn)

inputNum = listx.__len__()

temp = 0
tempvar = inputNum - 1
temp1 = 0
firstvar = 0
start = 1 
finish = 0
functemp = 0
something = inputNum-2

print("F(" + str(temp) + "):" + str(listy[0]))

while(temp != (inputNum-1)):
  firstvar = (listy[1] - listy[0]) / (listx[functemp + 1] - listx[0])
  print("F(" + str(temp + 1) + "):" + str(firstvar))
  while(temp1 != tempvar):
     tempY1 = listy[temp1 + 1]
     tempY2 = listy[temp1]
     listy[temp1] = ((tempY1 - tempY2) / (listx[start] - listx[finish]))
     temp1 = temp1 + 1 
     start = start + 1 
     finish = finish + 1
  finish = 0
  start = start - something
  something = something - 1 
  functemp = functemp + 1
  temp1 = 0
  tempvar = tempvar - 1
  temp = temp + 1
