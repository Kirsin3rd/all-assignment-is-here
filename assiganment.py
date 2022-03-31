age=28
height=189.0
print(height)
print(age)
complexnum=1234.5678
base=input('pls enter base of triangle:')
height=input('pls enter height of triangle:')
square=0.5*int(base)*int(height)
print(square)
a=input('pls enter length of side a:')
b=input('pls enter length of side b:')
c=input('pls enter length of side c:')
n=(int(a)+int(b)>int(c))and(int(a)+int(c)>int(b))and(int(b)+int(c)>int(a))
if n==True:
    print(int(a)+int(b)+int(c))
else :
    print("invalid data for a triangle")
alpha=input('pls enter length of rectangle:')
bravo=input('pls enter width of rectangle:')
squareofrec=int(alpha)*int(bravo)
perimeter=(int(alpha)+int(bravo))*2
print(squareofrec)
print(perimeter)
import math
r=input('pls enter your radius')
area=int(r)**2*math.pi
perimetercircle=2*math.pi*int(r)
print('the square of circle is {abc} '.format(abc=area) )
print('the perimeter of circle is {edf} '.format(edf=perimetercircle) )
import numpy as np
np.random.seed(0)
charlie=np.random.rand(2)
x1=charlie[0]
x2=charlie[1]
y1=-2*x1
y2=-2*x2
slope=(y2-y1)/(x2-x1)
print(slope)
print("both intercept of x and y axis is 0")
delta=int(input('pls enter the coefficient of function'))
echo=int(input('pls enter the constant of function'))
np.random.seed(1)
fox=np.random.rand(2)
x3=fox[0]
x4=fox[1]
y3=delta*x2+echo
y4=delta*x2+echo
if x4-x3 == 0:
    print('you cant divide by zero')
else:
   slope2=(y4-y3)/(x4-x3)
   interceptx=-echo/2
   intercepty=echo
   print('the interceptx of the function is {zxc}'.format(zxc=interceptx))
   print('the intercepty of the function is {vbn}'.format(vbn=intercepty))
def slope(a,b,c,d):
    if b-a==0:
        return('invalid data')
    else:
       slp=(d-c)/(b-a)
       return slp
x5=int(input('pls enter your x1'))
x6=int(input('pls enter your x2'))
y5=int(input('pls enter your y1'))
y6=int(input('pls enter your y2'))
cosequence=slope(x5,x6,y5,y6)
print(cosequence)
import math
def euclidean(a,b,c,d):
    eul=math.sqrt((a-b)**2+(c-d)**2)
    return eul
x7=int(input('pls enter your x1 to calculate euclidean'))
x8=int(input('pls enter your x2 to calculate euclidean'))
y7=int(input('pls enter your y1 to calculate euclidean'))
y8=int(input('pls enter your y2 to calculate euclidean'))
euc=euclidean(x7,x8,y7,y8)
print(euc)
p=len('python')
data=len('datascience')
data>p
q='on' in 'python'
w='on' in 'cannon'
e='jargon' in 'I hope this course is not full of jargon.'
print(q)
print(w)
print(e)
r=len('python')
t=float(r)
y=str(t)
print(y)
def check(a):
    if a%2==0:
        return "this is a even number"
    else:
        return"this is a odd number"
u=int(input('pls enter a number to check wether it s even or odd'))
i=check(u)
print(i)
z=7//3
x=int(2.7)
j=z==x
print(j)
k='10'==10
print(k)