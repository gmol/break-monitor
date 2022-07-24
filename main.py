import sys
import argparse
import logging
from time import sleep

from detector.WorkDetector import WorkDetector
from utils.MqttNotifier import MqttNotifier
from sensors.FakeSonar import FakeSonar
from sensors.SensorMonitor import SensorMonitor

from states import Config
from states.Context import Context
from states.TimeProvider import TimeProvider
from light.LightController import LightController


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
    parser.add_argument('--debug', action='store_true',
                        help='Run project in DEBUG mode')
    args = parser.parse_args()
    if args.debug:
        logger.info(">>>>> DEBUG mode <<<<<")
        Config.IS_DEBUG = True
        Config.REST_TIME = 3
        Config.OVERTIME = 5

    ctxt = Context(LightController(), TimeProvider(), MqttNotifier())
    monitor = None

    if 'win32' in sys.platform:
        logger.info(">>>>> WINDOWS environment <<<<<")
        monitor = SensorMonitor(work_detector=WorkDetector(ctxt), sonar=FakeSonar())
    else:
        logger.info(">>>>> PI environment <<<<<")
        from sensors.GroveUltrasonicRanger import GroveUltrasonicRanger
        monitor = SensorMonitor(work_detector=WorkDetector(ctxt), sonar=GroveUltrasonicRanger())

    print(f"OVERTIME [${Config.OVERTIME}] seconds and REST time [${Config.REST_TIME}] seconds")

    monitor.start()
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

