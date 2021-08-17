class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.filehandler = None

    
    def __enter__(self):
        self.filehandler = open(self.filename, self.mode)
        return self.filehandler

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.filehandler.close()



    
if __name__ == "__main__":
    with OpenFile("11-6.py", "r") as f:
        pass