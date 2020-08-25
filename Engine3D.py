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

def mediumShot():
    bmp = glInit()
    bmp.glCreateWindow(1000, 1000)
    bmp.glClear()
    bmp.glColor(1, 1, 1)
    bmp.lookAt(V3(-0.2,0,5),V3(0,0,0),norm(V3(0,1,0)))
    bmp.loadViewportMatrix(0, 0)
    bmp.glLoadObjModel("gato.obj", mtl="gato.mtl", translate=(-1.0,-0.9,0), scale=(0.04,0.04,0.04), rotate=(0,0.2,0))
    bmp.glWrite("MediumShot.bmp")

def lowShot():
    bmp = glInit()
    bmp.glCreateWindow(1000, 1000)
    bmp.glClear()
    bmp.glColor(1, 1, 1)
    bmp.lookAt(V3(-0.2,-1.5,1.5),V3(0,0,0),norm(V3(0,1,0)))
    bmp.loadViewportMatrix(0, 0)
    bmp.glLoadObjModel("gato.obj", mtl="gato.mtl", translate=(-1,-1,0), scale=(0.04,0.04,0.04), rotate=(0,0.2,0))
    bmp.glWrite("LowShot.bmp")

def highShot():
    bmp = glInit()
    bmp.glCreateWindow(1000, 1000)
    bmp.glClear()
    bmp.glColor(1, 1, 1)
    bmp.lookAt(V3(-0.2,4.0,1.5),V3(0,0,0),norm(V3(0,1,0)))
    bmp.loadViewportMatrix(0, 0)
    bmp.glLoadObjModel("gato.obj", mtl="gato.mtl", translate=(-1.1,-0.1,0), scale=(0.04,0.04,0.04), rotate=(-0.2,0.05,0))
    bmp.glWrite("HighShot.bmp")

def dutchShot():
    bmp = glInit()
    bmp.glCreateWindow(1000, 1000)
    bmp.glClear()
    bmp.glColor(1, 1, 1)
    bmp.lookAt(V3(-0.2,0,20),V3(0,0,0),norm(V3(0,1,0)))
    bmp.loadViewportMatrix(0, 0)
    bmp.glLoadObjModel("gato.obj", mtl="gato.mtl", scale=(0.04,0.04,0.04),rotate=(0,0.2,0.36),translate=(-0.4,-1.36,0))
    bmp.glWrite("DutchShot.bmp")

if __name__ == '__main__':
    '''Main Program'''

    mediumShot()
    lowShot()
    highShot()
    dutchShot()