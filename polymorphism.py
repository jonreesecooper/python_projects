class Musician():
    def __init__(self,user_name,clasically_trained,instrument):
        self.user_name = user_name
        self.classically_trained = clasically_trained
        self.instrument = instrument

    def musicianStatement(self):
        if (self.classically_trained == True):
            print("{} is a musician who plays the {} and is classically trained.".format(self.user_name,self.instrument))
        else:
            print("{} is a musician who plays the {} and is not classically trained.".format(self.user_name,self.instrument))

class Live(Musician):
    def __init__(self,user_name,classically_trained,instrument,pro_amateur,monthly_performances):
        Musician.__init__(self,user_name,classically_trained,instrument)
        self.pro_amateur = pro_amateur
        self.monthly_performances = monthly_performances
        

    def musicianStatement(self):
        if (self.classically_trained == True):
            print("{} is a live musician who plays the {}, is clasically trained, and performs {} times a month.".format(self.user_name,self.instrument,self.monthly_performances))
        else:
            print("{} is a {} live musician who plays the {},\nis not clasically trained, and performs {} times a month.".format(self.user_name,self.pro_amateur,self.instrument,self.monthly_performances))
            
class Studio(Musician):
    def __init__(self,user_name,classically_trained,instrument,studio_albums,can_hire):
        Musician.__init__(self,user_name,classically_trained,instrument)
        self.studio_albums = studio_albums
        self.can_hire = can_hire

    def musicianStatement(self):
        if(self.classically_trained == True and self.can_hire == True):
            print("{} is a studio musician who plays the {}, is classically trained,\nhas recorded {} studio albums and is available for hire!".format(self.user_name,self.instrument,self.studio_albums))
        elif(self.classically_trained == False and self.can_hire == True):
            print("{} is a studio musician who plays the {}, is not classically trained,\nhas recorded {} studio albums and is available for hire!".format(self.user_name,self.instrument,self.studio_albums))
        elif(self.classically_trained == True and self.can_hire == False):
            print("{} is a studio musician who plays the {}, is classically trained,\nhas recorded {} studio albums and is not available for hire!".format(self.user_name,self.instrument,self.studio_albums))
        else:
            print("{} is a studio musician who plays the {}, is not classically trained,\nhas recorded {} studio albums and is not available for hire!".format(self.user_name,self.instrument,self.studio_albums))



if __name__ == "__main__":
    drummer = Musician("Bob",True,"drums")
    drummer.musicianStatement()
    guitarist = Live("Sam",False,"guitar","amateur",5)
    guitarist.musicianStatement()
    bass = Studio("Max",False,"bass",9,False)
    bass.musicianStatement()
    
