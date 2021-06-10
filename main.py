import argparse
import logging
import sys
from time import sleep

from states.Constants import Activity
from states.Context import Context
from states.LightController import LightController
from states.TimeProvider import TimeProvider

if __name__ == '__main__':
    logger = logging.getLogger("Context")
    logger.info("Start")
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

    # logger.info("Argument values:")
    # logger.info(args.pos_arg)
    # logger.info(args.opt_pos_arg)
    # logger.info(args.opt_arg)
    # logger.info(args.production)
    if args.production:
        logger.info(">>>>> PRODUCTION environment <<<<<")
    else:
        logger.info(">>>>> DEVELOPMENT environment <<<<<")

    ctxt = Context(LightController(), TimeProvider())
    # ctxt = Context(LightController())
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

