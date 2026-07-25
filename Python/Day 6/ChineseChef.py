from chef import chef

class ChineseChef(chef):
    def make_fried_rice(self):
        print("The chef makes Fried Rice.")

    #Overriding 
    def make_special_dish(self):
        print("The chef makes orange chicken.")