import os
import yaml

class AppConf:
    def __init__(self):
        rawConf = load_config()        
        self.appPort =  rawConf['app']['port']
        self.todoListBaseUrl  =  rawConf['app']['todo-list-service']['base-url']

def load_config(path='conf.yml'):
    base_dir = os.path.dirname(__file__) 
    file_path = os.path.join(base_dir, path)
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)
