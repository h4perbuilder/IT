class Plane: 
    def __init__(self, mark, model,year,max_speed, odometr,is_flying):
        self.mark = mark
        self.model = model 
        self.year = year 
        self.max_speed = max_speed 
        self.odometr = odometr 
        self.is_flying = False
    
    def info(self):
        return f"Info: {self.mark}, {self.model}, {self.year}, {self.max_speed}, \nсамолет летит: {self.is_flying}, Cкорость: {self.odometr}"
    
    def take_off(self):
        self.is_flying = True

    def fly(self,km):
        self.odometr += km

    def land(self):
        self.is_flying = False 
        self.odometr = 0

plane = Plane("Ил","103", 1994, "225 km", 0, False)
plane.take_off()
plane.fly(147)
plane.land()
print(plane.info())
