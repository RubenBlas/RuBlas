import logging

LOG_FILE = 'myapp.log'
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_MODE = 'w'

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT, filename=LOG_FILE, filemode=LOG_MODE)

logging.debug("Message de débogage")
logging.info("Message informatif")
logging.error("Message d'erreur")
logging.warning('Problème de protocole: %s', 'réinitialisation de connexion')
