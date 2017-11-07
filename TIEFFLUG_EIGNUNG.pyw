from matplotlib.pyplot import *
from numpy import *

k=1      #k=0.5(AR=klein);k=1(AR=groß)
a=radians(27)
w=radians(67)
vboe=10
G_F=7000

def f(fi,Ma ):
    
    return Ma*(cos(fi))**k*vboe/G_F

fi = linspace(a ,w ,50)

Ma=[0.5,0.75,1,1.25]


c=['r','b','g','c']


for i in range(len(Ma)):
    y=f(fi,Ma[i])
    plot(degrees(fi) , y*1000,color=c[i], label='Ma=%s'%Ma[i],lw='2')
        
legend(loc='upper right')
title('Böenresponse im Tiefflug')
xlabel('Pfeilung fiv[deg]')
ylabel('rel.Härte f')
text(30,0.3,'G/F=%s'%G_F)
grid(True)
show ()

M=0.9
def f(fi,G_F ):
    
    return M*(cos(fi))**k*vboe/G_F

fi = linspace(a ,w ,50)

G_F=[2000,3000,4000,6000,8000]


c=['r','b','m','g','c']


for i in range(len(G_F)):
    y=f(fi,G_F[i])
    plot(degrees(fi) , y*1000,color=c[i], label='G/F=%s'%G_F[i],lw='2')


legend(loc='upper right')
title('Böenresponse im Tiefflug')
xlabel('Pfeilung fiv[deg]')
ylabel('rel.Härte f')
text(30,0.3,'M=%s'%M)
grid(True)
show ()









        
