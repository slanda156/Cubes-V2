itemNum = 1

items = []

def initItem():
    for i in range(itemNum):
        items.append(item(i))

class item:
    def __init__(self, index):
        self.name = "None"
        self.displayName = "None"
        self.healing = 0
        self.cost = 0

        if index == 0:
            self.medKit()


    def medKit(self):
        self.name = "medKit"
        self.displayName = "Med Kit"
        self.healing = 20
        self.cost = 20
