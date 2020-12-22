from pathlib import Path

class ProblemDB:
    def __init__(self):
        self.ignore_db_path = '.ignore.db'
        Path(self.ignore_db_path).touch()
        self.db = []
        self.db_links = {}
        with open(self.ignore_db_path, 'r') as database:
            self.ignore_db = database.readlines()
    
    def __len__(self):
        return len(self.db)
    
    def __str__(self):
        return "".join(self.db)
    
    def __getitem__(self,i):
        return self.db[i]

    def add(self,title:str,item:str) -> bool:
        self.db.append(title)
        self.db_links[title] = f"{item}\n"
        return True
    
    def ignore(self,title:str) -> bool:
        try:
            with open(self.ignore_db_path, 'a') as database:
                self.db.pop(self.db.index(title))
                database.write(self.db_links[title])
                self.db_links.pop(title)
            return True
        except:
            return False

    def is_ignored(self,item: str) -> bool:
        if item + "\n" in self.ignore_db:
            return True
        return False