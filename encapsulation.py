class ProtectedPrivate:
    def __init__(self):
        self._protectedVar = 2
        self.__privateVar = 12

    def getProtected(self):
        protected = self._protectedVar
        return protected

    def getPrivate(self):
        private = self.__privateVar
        return private

    def multProcPriv(self):
        try:
            X = self.getPrivate()
            Y = self.getProtected()
            mult = X * Y
            return mult
        except:
            pass
    

obj = ProtectedPrivate()
print(obj.getProtected())
print(obj.getPrivate())
print(obj.multProcPriv())



