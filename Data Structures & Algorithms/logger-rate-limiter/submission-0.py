class Logger:

    def __init__(self):
        # self.logger = []
        self.logger = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.logger.keys():
            if timestamp - self.logger[message] < 10:
                return False
            else:
                self.logger[message] = timestamp 
                return True

        self.logger[message] = timestamp
        print(self.logger)
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
