class Hero:
    """class to create Hero for game"""
    def __init__(self,name, level,race):
        '''initiate our hero'''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        '''Print all parameters of this hero'''
        discription = (self.name + " Level is " + str(self.level) + " Race is " + self.race + " Health is " + str(self.health)).title()
        print (discription)

    def level_up (self):
        """upgrade level of hero"""
        self.level += 1
    
    def move(self):
        """start moving hero"""
        print ("Hero " + self.name + " started mooooving...")

    def set_health(self,new_health):
        self.health = new_health
#---------------------------------------------------------------------------------------------------#



class SuperHero(Hero):
    """Class to create superhero"""
    def __init__(self, name, level, race, magiclevel):
        """initiate supahero"""
        super().__init__(name, level,race)
        self.magiclevel = magiclevel
        self.magic = 100
    def makemagic(self):
        '''use magic'''
        self.magic -= 10

    def show_hero(self):
            '''Print all parameters of this hero'''
            discription = (self.name + " Level is " + str(self.level) + " Race is " + self.race + " Health is " + str(self.health) + " Magic is " + str(self.magic)).title()
            print (discription)

