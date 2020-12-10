import yaml
from pathlib import Path
import os

class Channel:
    def __init__(self,*args):
        if args:
            config_file = args[0]
        else:
            os.chdir(os.path.dirname(os.path.realpath(__file__)))
            config_file = '.channels.yaml'
        Path(config_file).touch()
        with open(config_file,'r') as file:
            self.config = yaml.full_load(file)

    def list(self):
        return [value for item,value in self.config.items()]

if __name__ == "__main__":
    configs = Channel()
    for item in configs.list():
        print('RSS:',item['rss'])
        print('Directory:',item['download_dir'])
        if 'filter' in item:
            if isinstance(item['filter'],list):
                print('Filters',end=": ")
                for filter in item['filter']:
                    print(filter)
            else:
                print('Filters:',item['filter'])
        else:
            print('Filters: NONE')
