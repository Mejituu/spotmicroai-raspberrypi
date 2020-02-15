import json
from spotmicro.utilities.log import Logger

log = Logger().setup_logger('Configuration')


class Config:
    config = {}

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
                self.config = json.load(json_file)

        except Exception as e:
            log.error("Configuration file don't exist, creating a new file with default values", e)
            # self.create_new_configuration()

    def list_modules(self):
        log.info('Detected configuration: ' + ', '.join(self.config.keys()))

    def print_config(self):
        print(json.dumps(self.config, indent=4, sort_keys=True))

    def create_new_configuration(self):

        self.config['spotmicro'] = []

        self.save_config()

    def save_config(self):
        try:
            with open('config.json', 'w') as outfile:
                json.dump(self.config, outfile)
        except Exception as e:
            log.error("Problem saving the configuration file", e)
