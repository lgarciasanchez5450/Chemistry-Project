black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_red = (255,100,100)
light_green = (100,255,100)
light_blue = (100,100,255)
dark_grey = (40,40,40)
grey = (120,120,120)
light_grey = (210,210,210)
dark_red = (150,0,0)
dark_green = (0,150,0)
dark_blue = (0,0,150)
light_dark_grey = (70,70,70)
dark_light_grey = (180,180,180)
purple = (100,0,100)
royal_purple = (60,10,100)
theme_purple = (95,59,229)
theme_yellow = (248,196,0)
theme_light_yellow = (254,229,147)
theme_red_purple = (125,64,146)
theme_light_purple = (100,62,235)
theme_dark_purple = (80,50,150)
class Color:
    white:"Color" = 0 #type: ignore
    black:"Color" = 0 #type: ignore
    red:"Color" = 0 #type: ignore
    green:"Color" = 0 #type: ignore
    blue:"Color" = 0 #type: ignore
    __slots__ = 'r','g','b','a'
    def __init__(self,r:float,g:float,b:float,a:float=255):
        self.r = max(min(r,255),0)
        self.g = max(min(g,255),0)
        self.b = max(min(b,255),0)
        self.a = max(min(a,255),0)
    def mix(self,__obj:"Color",t:float = 0.5):
        return Color(*[a+t*(b-a) for a,b in zip(self,__obj)])   
    def __mul__(self,__obj:float):
        return Color(self.r*__obj,self.g*__obj,self.b*__obj,self.a)
    def __add__(self,__obj:"Color"):
        return Color(*[a+b for a,b in zip(__obj,self)])
    def __eq__(self,__obj:"Color"): 
        return all(a==b for a,b in zip(__obj,self))
    
    @property
    def rgb(self) -> tuple[int,int,int]: return (self.r.__round__(), self.g.__round__(), self.b.__round__())  
    @property
    def rgba(self) -> tuple: return (self.r.__round__(), self.g.__round__(), self.b.__round__(), self.a.__round__())  
    
    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b
        yield self.a

    def copy(self): return Color(*self)

    def __str__(self) -> str:
        return f"Color ({self.r},{self.g},{self.b},{self.a})"
    
Color.white = Color(255,255,255)
Color.black = Color(0,0,0)
Color.red = Color(255,0,0)
Color.green = Color(0,255,0)
Color.blue = Color(0,0,255)

def getColors():
    g = globals()
    return {name:g[name] for name in filter(lambda x : not x.startswith('__') and x not in {"Colors","getColors"}, g)}
