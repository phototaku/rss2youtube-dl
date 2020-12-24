class ytdlNoVideo(Exception):
    def __init__(self,message="YT-DL No video!",err=""):
        self.message = message
        self.err = err
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message} {self.err}\n'

class ytdlCopyright(Exception):
    def __init__(self,message="YT-DL Copyright Protected!",err=""):
        self.message = message
        self.err = err
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message} {self.err}\n'

class ytdlUnsupported(Exception):
    def __init__(self,message="YT-DL Unsupported Site!",err=""):
        self.message = message
        self.err = err
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message} {self.err}\n'

class ytdlPremiere(Exception):
    def __init__(self,message="YT-DL Waiting for Premiere!",err=""):
        self.message = message
        self.err = err
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message} {self.err}\n'