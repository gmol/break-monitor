import logging

__version__='0.1.0'

# logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(name)s[%(levelname)s]: %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s[%(levelname)s]: %(message)s')
# logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
# root_logger= logging.getLogger()
# root_logger.setLevel(logging.DEBUG) # or whatever
# # handler = logging.FileHandler('test.log', 'w', 'utf-8') # or whatever
# # formatter = logging.Formatter('%(name)s %(message)s') # or whatever
# formatter = logging.Formatter('%(asctime)s %(name)s[%(levelname)s]: %(message)s') # or whatever
# handler.setFormatter(formatter) # Pass handler as a parameter, not assign
# root_logger.addHandler(handler)
#
