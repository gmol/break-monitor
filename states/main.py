from time import sleep

from states.Constants import Activity
from states.Context import Context
from states.Light import Light
from states.TimeProvider import TimeProvider

if __name__ == '__main__':
    ctxt = Context(Light(), TimeProvider())
    # ctxt = Context(Light())
    ctxt.update_action(Activity.WORKING)
    ctxt.update_action(Activity.IDLE)
    ctxt.update_action(Activity.WORKING)
    sleep(5)
    ctxt.update_action(Activity.WORKING)
    sleep(1)
    ctxt.update_action(Activity.WORKING)
    sleep(1)
    ctxt.update_action(Activity.IDLE)
    sleep(2)
    ctxt.update_action(Activity.IDLE)
    sleep(3)
    ctxt.update_action(Activity.IDLE)
    sleep(1)
    ctxt.update_action(Activity.WORKING)
    sleep(1)
    ctxt.update_action(Activity.WORKING)

