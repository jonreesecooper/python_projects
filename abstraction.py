from abc import ABC, abstractmethod

class bass(ABC):
    def totalStrings(self, strings):
        print("Your bass has a total of {} strings.".format(strings))

    @abstractmethod
    def available(self,strings):
        pass

class fourstringBass(bass):
    def available(self,strings):
        print("You require a pack of {} strings, and we have those available!".format(strings))

class fivestringBass(bass):
    def available(self,strings):
        print("You require a pack of {} strings, but we only sell packs of 4.".format(strings))



obj = fourstringBass()
obj.totalStrings("4")
obj.available("4")
obj1 = fivestringBass()
obj1.totalStrings("5")
obj1.available("5")
