import logging

logerius = logging.getLogger(__name__)
logerius.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler('logerius.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)
logerius.addHandler(file_handler)

terminal_formatter = logging.Formatter(
    '%(levelname)s: %(message)s')
terminal_handler = logging.StreamHandler()
terminal_handler.setLevel(logging.DEBUG)
terminal_handler.setFormatter(terminal_formatter)
logerius.addHandler(terminal_handler)
