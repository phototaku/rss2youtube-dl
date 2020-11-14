import yaml
from pathlib import Path

class Channel:
    def __init__(self,*args):
        if args:
            config_file = args[0]
        else:
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
