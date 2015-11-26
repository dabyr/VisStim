import random
from psychopy import visual, core, event 

def init():
    return visual.Window([800,600],monitor="testMonitor", units="deg")

def function_1(win):
    grating = visual.GratingStim(win=win, mask='circle', size=20, pos=[0,0], sf=3)

    while True: 
        grating.setPhase(0.05, '+')
        grating.draw()
        win.flip()
        if len(event.getKeys())>0: break
        event.clearEvents()

def function_2(win):
    pass

def shutdown(win):
    win.close()
    core.quit()

def run(win):
    functions = [function_1, function_2]
    l = len(functions)-1
    while True:
        functions[random.randint(0, l)](win)


def main():
    win = init()
    run(win)
    shutdown(win)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
