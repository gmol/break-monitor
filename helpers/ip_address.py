import logging
import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception as e:
        logging.exception(e)
        return None
    finally:
        s.close()
    return ip_address


def int_to_bin_list(number: int):
    return list(reversed([int(x) for x in list('{0:0b}'.format(number))]))


def get_last_ip_number_in_bin_array():
    logger = logging.getLogger("ip_address")
    ip_address = get_ip_address()
    if ip_address is None:
        logger.error("Failed to get IP address")
        return []
    logger.info("IP ADDRESS: {}".format(ip_address))
    last_ip_address_number = ip_address.split('.')[-1]
    return int_to_bin_list(int(last_ip_address_number))
