__version__ = '0.1.0'




# logging.basicConfig(
#         handlers=[RotatingFileHandler('./my_log.log', maxBytes=100000, backupCount=10)],
#         level=logging.DEBUG,
#         format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
#         datefmt='%Y-%m-%dT%H:%M:%S')


# "%(name)s: %(message)s [ %(filename)s %(lineno)d ]"
# logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
# root_logger= logging.getLogger()
# root_logger.setLevel(logging.DEBUG) # or whatever
# # handler = logging.FileHandler('test.log', 'w', 'utf-8') # or whatever
# # formatter = logging.Formatter('%(name)s %(message)s') # or whatever
# formatter = logging.Formatter('%(asctime)s %(name)s[%(levelname)s]: %(message)s') # or whatever
# handler.setFormatter(formatter) # Pass handler as a parameter, not assign
# root_logger.addHandler(handler)
#
