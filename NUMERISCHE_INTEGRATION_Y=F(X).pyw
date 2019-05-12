"""
==================================
Funktion und Fläche unter Funktion
(Bestimmtes Integral)
==================================

Der Code zeichnet die Funktion und führt numerisch
eine Integration zwischen x1 und x2 durch. Die Funktion
von f_(x,y) muss nach y auflösbar sein: y=f(x)

===========================
VvT / 1.5.2019 / Version:1
===========================
"""
print(__doc__)

import matplotlib.pyplot as plt
from numpy import*
import scipy.integrate

import seaborn as sns
sns.set(color_codes=True)

import warnings
warnings.filterwarnings("ignore")

# zu untersuchende Funktion als String eingeben
# =============================================
# y='f(x)'
# ==========
#y='exp(-x)*(x**2+10*sin(x**2))'
#y='exp(-x)*5*sin(3*x)'
#y='1+0*x'                  #Näherung für Parallele zur x-Achse
#y='(exp(x)+exp(-x))/2'     #Cosinus-Hyperbolicus(Kettenkurve)
#y='sin(x)'                 #Check: über 2*pi = 0
#y='log(x)+exp(x)'
#y='x**3/(exp(x)-1)'        #Plancksches Integral
#y='exp(-x**2)'             #Gauß--->-inf...+inf = pi**0.5
#y='1/(1+x**2)'             #Versiera di Agnesi    -inf...+inf = pi
#y='(1-x**2)**0.5'          #Viertelkreis 0...1 = pi/4
#y='exp(x)'                 #e-Funktion -inf...0: y=1.0
#y='1/(1+exp(-5*x+5))'      #S-Kurve
#y='1+x-x**2'               #Fibo/Goldener Schnitt: x=1.61803;y=0
y='1/(1-x**2)**0.5'        #-1...1 = pi
#y='1/(1-x**4)**0.5'        #Bogenlänge der Lemniskate/elliptisches Integral
# ================================================================
def f(x,y):
    ''' Funktion y=f(x) '''
    return lambda x:y

# bestimmtes Integral
# ===================
x1=-1
#x2=1
x2=1
#x2=inf
#x2=15

f=lambda x:eval(y)          # evaluiert als  String geschriebene Formel
i_= scipy.integrate.quad(f,x1,x2)[0]
print('x1:',x1,'x2:',x2,'Fläche/Integral:',i_)

# Plot und Ausgabe der Lösung des Integrals
# =========================================
x=linspace(x1,x2,1000)
plt.plot(x,f(x),'r-')
plt.plot(0,0,'None',label='x1 = %s'%x1)
plt.plot(0,0,'None',label='x2 = %s'%round(x2,4))
plt.plot(0,0,'None',label='$\int_{x1}^{x2} y\mathrm{d}x$ = %s'%round(i_,4))
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.legend()
plt.title('y ='+y)
plt.show()
# ************************************************
#print(pi**0.5) Gauß
# ************************






