import eel
import matplotlib.pyplot as plt
from trajpy import *
from mat import *
from math import atan2, pi


web_options = {'host':'localhost', 'port':6969}

@eel.expose
def pyget_data():
    data_points = eel.jsget_points()()
    q = []
    for p in data_points:
        qt = ik(p['x'], p['y']) # TODO: check this out -> how do I find the approach angle?
        q.append(qt)
        eel.jslog(str(p))
        eel.jslog(f'q: [{qt[0,0]}, {qt[1,0]}]')
        eel.jslog(f'p: [{0.25*cos(qt[0,0])+0.25*cos(qt[0,0]+qt[1,0])},{0.25*sin(qt[0,0])+0.25*sin(qt[0,0]+qt[1,0])}]')
    eel.jsdraw_pose(q[-1][:,0])
    # scrivi la funzione js che prenda direttamente la dk ?
    #eel.jsdraw_pose([pi/4, pi/4])
    pass



if __name__ == "__main__":
    eel.init("./layout")
    eel.start("./index.html", host=web_options['host'], port=web_options['port'])

'''
TODO:
- check if ik is correct, it gives sus values :/
'''