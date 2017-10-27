#Appfelmännchen ultrakurz und schnell dank numpy(genial!)

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot( h,w, maxit=25):
    
    """Gibt die Pixel für das Mandelbrot Fractal der Größe (h,w)zurück"""
    
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime =maxit+ np.zeros(z.shape, dtype=int)
    
    for i in range(maxit):
        z = z**2 + c
                 
        diverge = abs(z) > 2**2 
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2                      
    
    return divtime

#cProfiler
import cProfile
cProfile.run("mandelbrot(1000,1000,25)")


if __name__ == "__main__":
    
    plt.imshow(mandelbrot(1000,1000))
plt.title("Mandelbrot/Apfelmännchen")
plt.show()
