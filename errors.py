class ytdlNoVideo(Exception):
    def __init__(self,message="YT-DL ERROR!",err=""):
        self.message = message
        self.err = err
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message} {self.err}\n'

class ytdlCopyright(Exception):
    def __init__(self,message="YT-DL ERROR!",err=""):
        self.message = message
        self.err = err
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message} {self.err}\n'