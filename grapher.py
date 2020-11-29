import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from rectangle import Rectangle
import random


def create_rectangle(rectangle: Rectangle):
    # get the right map, and get the color from the map
    color = matplotlib.cm.jet(rectangle.width + rectangle.height + random.randint(0,100))
    rec = plt.Rectangle((rectangle.x, rectangle.y), rectangle.width,
                        rectangle.height, color=color, zorder=1, alpha=0.25)
    add_shape(rec)


def add_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')


def draw(filename):
    plt.savefig(filename)

def addRectangles(drawlist):
  #  matplotlib.use( 'tkagg' )
    for item in drawlist:
        create_rectangle(item)
def addHline(y):
    plt.axhline(y=y,alpha=0.1,color='tab:orange')

def addVline(x):
    plt.axvline(x=x,alpha=0.1,color='tab:orange')

    


# plt.imsave('demo')
