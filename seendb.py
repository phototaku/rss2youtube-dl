from pathlib import Path

class SeenDB:
    def __init__(self):
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
