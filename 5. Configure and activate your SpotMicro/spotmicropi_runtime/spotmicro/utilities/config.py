import json
import sys
from spotmicro.utilities.log import Logger

log = Logger().setup_logger('Configuration')


class Config:
    values = {}

    def __init__(self):

        try:
            log.debug('Loading configuration...')

            self.load_config()
            self.list_modules()

        except Exception as e:
            log.error('Problem while loading the configuration file', e)

    def load_config(self):
        try:
            with open('config.json') as json_file:
                self.values = json.load(json_file)
                log.debug(json.dumps(self.values, indent=4, sort_keys=True))

        except Exception as e:
            log.error("Configuration file don't exist or is not a valid json, aborting.")
            sys.exit(1)

    def list_modules(self):
        log.info('Detected configuration for the modules: ' + ', '.join(self.values.keys()))

    def save_config(self):
        try:
            with open('config.json', 'w') as outfile:
                json.dump(self.values, outfile)
        except Exception as e:
            log.error("Problem saving the configuration file", e)
