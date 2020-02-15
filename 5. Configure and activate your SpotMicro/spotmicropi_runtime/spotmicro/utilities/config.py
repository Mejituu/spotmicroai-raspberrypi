import json
from pathlib import Path
from spotmicro.utilities.log import Logger

log = Logger().setup_logger('Configuration')


class Config:
    config = {}

    def __init__(self):

        try:
            log.info('Loading configuration...')

            self.load_config()

        except Exception as e:
            log.error('Problem while loading the configuration file', e)

    def load_config(self):
        try:
            with open('config.json') as json_file:
                self.config = json.load(json_file)
                for p in self.config['people']:
                    print('Name: ' + p['name'])
                    print('Website: ' + p['website'])
                    print('From: ' + p['from'])
                    print('')
        except Exception as e:
            log.error("Configuration file don't exist, creating a new file with default values", e)
            self.create_new_configuration()

    def create_new_configuration(self):

        self.config['spotmicro'] = []


        self.save_config()

    def save_config(self):
        try:
            with open('config.json', 'w') as outfile:
                json.dump(self.config, outfile)
        except Exception as e:
            log.error("Problem saving the configuration file", e)
