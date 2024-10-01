class CustomError(str):
    def __init(self, message: str = ""):
        super().__init__()
        if message != None:
                self.message =  message
    def __str__(self) -> str:
         if self.message != None:
            return self.message
         return super().__str__()