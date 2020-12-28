from pathlib import Path
import os

class SeenDB:
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.db = '.seen.db'
        Path(self.db).touch()

    def add(self,item:str) -> bool:
        try:
            with open(self.db, 'a') as database:
                database.write(item + "\n")
            return True
        except:
            return False

    def exists(self,item: str) -> bool:
        try:
            with open(self.db, 'r') as database:
                for line in database:
                    if line.strip() == item:
                        return True
            return False
        except:
            return False            

