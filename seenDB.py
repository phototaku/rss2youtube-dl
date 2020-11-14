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

    def a(self,item: str) -> bool:
        print(item)
        try:
            print("TRYING TO SEE")
            with open(self.db, 'r') as database:
                print("SEEING!")
                if item in database:
                    print("SEEN!!!!!!!!!")
                    return True
            return False
        except:
            print("SOMETHING FUCKING BROKE!")            
