'''
        SR3 Obj Models

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Engine 3D

'''

from gl import *
from texture import Texture

bmp = Bitmap(1000, 1000)

def glInit():
    return bmp


if __name__ == '__main__':
    '''Main Program'''

    #Initialize bmp Object
    bmp = glInit()

    bmp.glCreateWindow(1000, 1000)

    #Set all pixels to same color
    bmp.glClear()

    #Set pixel Colors
    bmp.glColor(1, 1, 1)

    bmp.lookAt(V3(-0.2,0,5),V3(0,0,0),norm(V3(0,1,0)))
    bmp.loadViewportMatrix(0, 0)
    bmp.glLoadObjModel("sphere3.obj", translate=(-1.0,-0.9,0), scale=(0.04,0.04,0.04), rotate=(0,0.2,0))
    
    #Output BMP
    bmp.glWrite("PlanetaJupiterShader.bmp")