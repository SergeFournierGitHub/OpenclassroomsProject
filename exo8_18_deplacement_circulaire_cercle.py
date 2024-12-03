from math import *
from tkinter import *
 
def point_on_ellipse(t):  
    #return(screen_center_x + demiGrandAxe*cos(radians(t)), screen_center_y - (èmoins tourne à gauche + tourne à droiteè) demiPetitAxe*sin(radians(t)))
    #  elipse return(screen_center_x + demiGrandAxe*cos(radians(t)), screen_center_y + demiPetitAxe*sin(radians(t)))
    return(screen_center_x + demiGrandAxe*cos(radians(t)), screen_center_y + demiPetitAxe*sin(radians(t)))
    # lissajous return(screen_center_x + demiGrandAxe*cos(radians(t)), screen_center_y + demiPetitAxe*sin(4*radians(t))) #lissajous


def stop():
    global bouger
    bouger = False
    main_win.title('Course planète ' + str(t) + "  " + str(cos(radians(t))) + "   " + str(sin(radians(t))) + " " + str(demiGrandAxe) + " " + str(demiPetitAxe)
                   + "  " + str(screen_center_x)  + "  " + str(screen_center_y) + "  " + str(demiGrandAxe*cos(radians(t))) + "  " + str(0- demiPetitAxe*sin(radians(t))))

def start():
    global bouger
    bouger = True
    move_planet()
    
def move_planet():
    global t,x1,y1, bouger

    if bouger:
        graph_area.create_oval(x1-p_rad, y1-p_rad, x1+p_rad, y1+p_rad, width=1, outline='blue', fill='yellow')
        t += 2.0
        if(t > 360.0): t = 2.0
        x2, y2 = point_on_ellipse(t)
        dx, dy = x2-x1, y2-y1
        x1, y1 = x2, y2
 
        graph_area.move(planet,dx,dy)
        graph_area.after(50, move_planet)

def largeur_plus():
    global demiGrandAxe
    demiGrandAxe+=30

def largeur_moins():
    global demiGrandAxe
    demiGrandAxe-=30
    
#WIDTH, HEIGHT = 600, 400
WIDTH, HEIGHT = 1000, 1000
#demiPetitAxe, demiGrandAxe = 100.0, 200.0
demiPetitAxe, demiGrandAxe = 300.0, 400.0
p_rad = 15
screen_center_x, screen_center_y = (WIDTH-10)*0.5, (HEIGHT-10)*0.5-100

bouger = True

main_win = Tk()
main_win.title('Course planète')
main_win.geometry(str(WIDTH)+'x'+str(HEIGHT)+'+300+100')
 
graph_area = Canvas(main_win,bg='#000022',height=HEIGHT-10,width=WIDTH-10)
graph_area.place(x = 2,y = 2)

bouton_stop = Button(graph_area,text='Stop',command=stop).place(x=10 , y=10)
bouton_start = Button(graph_area,text='Start',command=start).place(x=50 , y=10)

bouton_largeur_plus = Button(graph_area,text='Largeur+',command=largeur_plus).place(x=100 , y=10)
bouton_largeur_moins = Button(graph_area,text='Largeur-',command=largeur_moins).place(x=150 , y=10)

#Ellipse
graph_area.create_oval(screen_center_x-demiGrandAxe, screen_center_y-demiPetitAxe, screen_center_x+demiGrandAxe, screen_center_y+demiPetitAxe, width=1, outline='white')
 
#Planet
t=0.0
x1, y1 = point_on_ellipse(t)
planet = graph_area.create_oval(x1-p_rad, y1-p_rad, x1+p_rad, y1+p_rad, width=1, outline='yellow', fill='yellow')
 
move_planet()
 
main_win.mainloop()
