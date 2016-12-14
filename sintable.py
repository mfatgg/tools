#!/usr/bin/python

# Interpolationsformel fuer den sinus im Intervall 0-pi/2
#Zahl der nicht trivialen Stuetzstellen n-1
#Genauigkeit der abgespeicherten Stuetzwerte in bitlaenge=nbit
#es wird von rechts oder links von der Stuetzstelle mit dem Ausdruck
#sin(x0+dx)=sin(x0)*(1-dx**2/2)+cos(x0)*dx*(1-1/6*dx**2)
#genaehert.
#Die cosinuswerte stehen in der gleichen Tabelle rueckwaerts
#bei 4 nichttrivialen 16 bit Zahlen ist die Genauigkeit 3.3*10^-5

import math,sys

nbit=8
div=2**nbit
n=256
sin=n*[0]
triangle=n*[0]

#sinus
sys.stdout.write('sinus:\n')
for i in range(n):
  msin=math.sin(2.0*math.pi/n*i)
  sin[i]=int(msin*div/2.0)+128
  #print i,msin,hex(sin[i])
  #print '%02x' % sin[i] ,
  sys.stdout.write('%02x,' % sin[i])
  if (i % 16) == 15:
    sys.stdout.write('\n')
sys.stdout.write('\n')

#triangle
sys.stdout.write('triangle:\n')
for i in range(n):
  if (i < n/4):
    mtriangle=i/(n/4.0)
  elif (i < n*3.0/4.0):
    mtriangle=1.0-(i-(n/4.0))/(n/4.0)
  else:
    mtriangle=-1.0+(i-n*3.0/4.0)/(n/4.0)
  triangle[i]=int(mtriangle*div/2.0)+128
  sys.stdout.write('%02x,' % triangle[i])
  if (i % 16) == 15:
    sys.stdout.write('\n')
sys.stdout.write('\n')


#maxdif=0

#def sinp(x):
#  k=int(x*n+0.5)
#  DX=x*n-k
#  dx=DX*math.pi/2.0/n
#  dx2=dx**2
#  si=sin[k]*(1.0-0.5*dx2)
#  co=sin[n-k]*dx*(1.0-1.0/6.0*dx2)
#  return (si+co)/float(div)
 
#for i in range(1000000):
#  x=random.random()
#  xb=x*math.pi/2.0
#inline version ersetzt Funktionsaufruf sinp(x)
#  k=int(x*n+0.5)
#  DX=x*n-k
#  dx=DX*math.pi/2.0/n
#  dx2=dx**2
#  si=sin[k]*(1.0-0.5*dx2)      
#  co=sin[n-k]*dx*(1.0-1.0/6.0*dx2)
#  isin=(si+co)/float(div)
#  isin=sinp(x) #(si+co)/float(div)
#  masin=math.sin(xb)
#  if abs(isin-masin)>maxdif:
#    maxdif=abs(isin-masin)
#print "maxdif=",maxdif

