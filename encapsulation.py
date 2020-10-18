class Hide:
    def __init__(self):
        self._hiddenItm= ""
        
    def __init__(self):
        self.__privateVar = "is"

    def findItm(self):
        print(self.__privateVar)

    def placeItm(self, private):
        self.__privateVar = private
        
obj = Hide()
obj._hiddenItm = "Python"
print(obj._hiddenItm)

obj = Hide()
obj.findItm()
obj.placeItm("fun")
obj.findItm()
