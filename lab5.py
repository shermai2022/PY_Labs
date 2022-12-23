

class Rocket:
    
    def __init__(self, mass, fuel, active):
        self.mass = mass
        self.fuel = fuel
        self.active = active
        self.mass = self.mass + fuel
       
   
    def spend_fuel(self, count): 
        
        if (self.fuel - count) >= 0:
            
            if self.fuel < count:
                self.fuel = 0 
                  
            self.mass = self.mass - count
            self.fuel = self.fuel - count
            return True
           
        else:
            self.active = False
            self.mass = self.mass - self.fuel
            return False

            
    def get_fuel_level(self):
        return self.fuel
        
        
 #определение общего веса в каждом экземпляре класса   
 
    def get_total_weight(self):
        return self.mass
    
#проверка того, находятся ли двигатели в активном режиме
    
    def get_is_engine_running(self):
        return self.active
        

main = Rocket(1000, 400, True)

while main.active == True:
    print(main.get_total_weight(), main.get_fuel_level(), main.active)
    
    main.spend_fuel(30)

    
    print(main.get_total_weight(), main.get_fuel_level(), main.active)


