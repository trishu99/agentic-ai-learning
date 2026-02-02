class ShortTermMemory:
    def __init__(self, limit=5):
        self.messages = []
        self.limit = limit

    def add(self, message):
        self.messages.append(message)
        self.messages = self.messages[-self.limit:]

    def get(self):
        return self.messages


'''
This mirrors how:
context windows work
older messages get dropped



'''