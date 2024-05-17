from framework import *
import framework
import colors as color
from colors import Color
import dataLoader
init((1000,600),0,"Interactive Periodic Table")

description_font = makeFont("Arial",20)
symbol_font = makeFont("Arial",30,True)
small_symbol_font = makeFont("Arial",27,True)
name_font = makeFont("comicsansms",23,False,True)
mass_font = makeFont("impact",18)

MAX_INFO_WIDTH = 500
MIN_MINIWINDOW_WIDTH = 300
MIN_MINIWINDOW_HEIGHT = 300
SQUARE_SIZE = 50

window_space = Window_Space()
window_space.addBorder("left",50,color.grey)
#window_space.addMiniWindow("Information On",(0,0),(500,500),color.black)
credits = window_space.mainSpace = ScrollingMS()
credits.text = TextBox((5,5),makeFont('Arial',20),  'Credits:','white')
credits.text1 = TextBox((5,30),makeFont('Arial',20),'   Application Designer/Developer - Leonardo Garcia Sanchez','white')
credits.text2 = TextBox((5,55),makeFont('Arial',20),'   Researcher - Zackary Cantu','white')
ms1 = window_space.mainSpace = ScrollingMS()
ms1.set_background_color((90,90,90))
ms1.periodic_table = ptable = GridComponent((10,10),(18,9),(SQUARE_SIZE,SQUARE_SIZE)).setSpacing(2)
for element in dataLoader.getAllElementsData():
    bg_color = Color(*element.getBGColor())
    txt_color = Color(*element.getTextColor())

    m_window_name = "Information On "+element.fullName()

    description_surf = description_font.render(element.description(),True,'white',wraplength=MAX_INFO_WIDTH)
    symbol_surf = symbol_font.render(element.symbol(),True,'white')
    name_surf = name_font.render(element.fullName(),True,'white')
    mass_surf = mass_font.render(f"Atomic Mass: {element.atomicMass()}",True,'white')
    number_surf = mass_font.render(f"Atomic Number: {element.atomicNumber()}",True,'white')

    MINIWINDOW_WIDTH = max(max(description_surf.get_width()+10,name_surf.get_width()+number_surf.get_width()+10),MIN_MINIWINDOW_WIDTH)
    MINIWINDOW_HEIGHT = max(description_surf.get_height()+
                            symbol_surf.get_height()+
                            name_surf.get_height()+50,MIN_MINIWINDOW_HEIGHT)
    window_space.addMiniWindow(m_window_name,((framework.WIDTH-MINIWINDOW_WIDTH)/2,(framework.HEIGHT-MINIWINDOW_HEIGHT)/2),(MINIWINDOW_WIDTH,MINIWINDOW_HEIGHT),color.black)
    
    window_space.miniWindow(m_window_name).symbol = Image((10,25),symbol_surf)
    window_space.miniWindow(m_window_name).name = Image((5,60),name_surf)
    window_space.miniWindow(m_window_name).description = Image((5,110),description_surf)
    window_space.miniWindow(m_window_name).number = Image((MINIWINDOW_WIDTH-number_surf.get_width()-10,25),number_surf)
    window_space.miniWindow(m_window_name).mass = Image((MINIWINDOW_WIDTH-mass_surf.get_width()-10,50),mass_surf)

    small_symbol_surf = small_symbol_font.render(element.symbol(),True,txt_color.rgb)
    b = Button((0,0),0,0,lambda :0,bg_color.mix(Color.black,0.2).rgb,bg_color.rgb,bg_color.mix(Color.white,0.2).rgb,small_symbol_surf,(SQUARE_SIZE-small_symbol_surf.get_width())//2,(SQUARE_SIZE-small_symbol_surf.get_height())//2,OnUpCommand=window_space.activateMiniWindow(m_window_name,True))
    col = element.group()
    row = element.period()
    if isinstance(col,str):
        col = col.strip().casefold()
        row += 2
        if col == "Lanthanides".casefold():
            col = element.atomicNumber() - 54
        elif col == "Actinides".casefold():
            col = element.atomicNumber() - 86
        else:
            col = 0
            raise RuntimeError()
    ptable.addButton((col-1,row-1),b)

c = resizeSurfaceSmooth(loadImg('./Assets/Images/info-button.png',True,False),(40,40))
window_space.left.credits = RoundButton((25,framework.HEIGHT-25),18,lambda :0,color.dark_light_grey,color.dark_light_grey,color.light_grey,c,-20,-20,OnUpCommand=lambda :(window_space.setActiveMainSpace(1-window_space._activeMainSpace)))

window_space.initialize()
while True:
    myInput = getAllInput()
    if myInput.quitEvent:
        break;
    window_space.update(myInput)
    window_space.draw()
    #print(b.x,b.y,b.offSetPos)

