import sys
import argparse
import logging
from time import sleep

from detector.WorkDetector import WorkDetector
from sensors.FakeSonar import FakeSonar
from sensors.SensorMonitor import SensorMonitor
from states import Constants
from states.Constants import Activity
from states.Context import Context
from light.LightController import LightController
from states.TimeProvider import TimeProvider



if __name__ == '__main__':
    logger = logging.getLogger("Context")
    logger.info("Start")

    logger.info("Platform [{}]".format(sys.platform))

    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Optional app description')

    # # Required positional argument
    # parser.add_argument('pos_arg', type=int,
    #                     help='A required integer positional argument')
    #
    # # Optional positional argument
    # parser.add_argument('opt_pos_arg', type=int, nargs='?',
    #                     help='An optional integer positional argument')
    #
    # # Optional argument
    # parser.add_argument('--opt_arg', type=int,
    #                     help='An optional integer argument')

    # Switch
    parser.add_argument('--production', action='store_true',
                        help='Run project in PI environment')
    args = parser.parse_args()

    ctxt = Context(LightController(), TimeProvider())
    monitor = None
    if args.production and 'win32' in sys.platform:
        raise RuntimeError("Unsupported operating system [{}] in [production] effect.".format(sys.platform))
    if 'win32' in sys.platform:
        logger.info(">>>>> DEVELOPMENT environment <<<<<")
        Constants.REST_TIME = 3
        Constants.OVERTIME = 5
        monitor = SensorMonitor(work_detector=WorkDetector(ctxt), ranger=FakeSonar())
    else:
        logger.info(">>>>> PRODUCTION environment <<<<<")
        from sensors.GroveUltrasonicRanger import GroveUltrasonicRanger
        monitor = SensorMonitor(work_dtector=WorkDetector(ctxt), ranger=GroveUltrasonicRanger())

    print(f"OVERTIME [${Constants.OVERTIME}] seconds and REST time [${Constants.REST_TIME}] seconds")

    monitor.monitor()
    # ctxt.update_action(Activity.WORKING)
    # ctxt.update_action(Activity.IDLE)
    # ctxt.update_action(Activity.WORKING)
    # sleep(5)
    # ctxt.update_action(Activity.WORKING)
    # sleep(1)
    # ctxt.update_action(Activity.WORKING)
    # sleep(1)
    # ctxt.update_action(Activity.IDLE)
    # sleep(2)
    # ctxt.update_action(Activity.IDLE)
    # sleep(3)
    # ctxt.update_action(Activity.IDLE)
    # sleep(1)
    # ctxt.update_action(Activity.WORKING)
    # sleep(1)
    # ctxt.update_action(Activity.WORKING)

