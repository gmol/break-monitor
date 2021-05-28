# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
from time import sleep

from Constants import Activity
from Context import Context
from Light import Light
from TimeProvider import TimeProvider


# Press the green button in the gutter to run the script.
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
