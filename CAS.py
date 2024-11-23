import pygame as p
import numpy as np
from pygame import color as Col 
from tkinter import filedialog as fileBox
import csv,time,sys

WINDOW_TITLE = "Camper Activity Sheet"
HEIGHT = 400
WIDTH = 500

class main:
    #start function
    def __init__ (self):
        p.init()
        p.display.set_icon(p.image.load('setupFiles/CAS.png'))
        p.display.set_caption(WINDOW_TITLE)

        #variables 
        self.camperFile = "NULL"
        self.counselorFile = "NULL"
        self.Width = WIDTH
        self.Height = HEIGHT
        self.running = True
        self.buttons = {}

        #setup pygame functions
        self.setupPygame()

        #setup buttons
        self.buttons["childFileCsv"] = Button(pos=((self.Width * 1/2),(self.Height * 1/3 ) - 60),size= (50,40), col= Col.Color("brown2"), function = (self.setupChildFile), text= "select camper file")
        self.buttons["counselorFileCsv"] = Button(pos=(self.Width * 1/2,self.Height * 1/3),size= (50,40), col= Col.Color("brown2"), function = (self.setupCounselorFile), text= "select counselor file")
        self.buttons["outputFileCsv"] = Button(pos=(self.Width/2,self.Height* 2/3),size= (50,40), col= Col.Color("brown2"), function = (self.outputToCsvFile), text= "make activity sheet")
        
        #start program
        self.menuLoop()

        #close files
        if (self.camperFile != "NULL"):
            self.camperFile.close()
        if (self.counselorFile != "NULL"):
            self.counselorFile.close()
        


       

    #main functions for running
    def menuLoop(self):
       
        while self.running:
            for e in p.event.get():
                self.eventHandler(e)
                
            self.screen.fill(p.Color("white")) #repaints the bottom layer of the screen before things are put ontop of it
            self.drawRects() # draws all rectangles onto the screen
            
            p.display.update()
            p.display.flip()
    
    def eventHandler(self,e):
        if e.type == p.QUIT:
            self.running = False
        if e.type == p.MOUSEBUTTONDOWN and p.mouse.get_pressed()[0]: # clicked mouse left
           self.checkIfClicked(p.mouse.get_pos())
                 
    def checkIfClicked(self,clickPosition):
        for key in self.buttons:
            if self.buttons[key].is_clicked(clickPosition):
                self.buttons[key].funct()
    
    def drawRects(self): #loops over all rects and prints them out
        for key in self.buttons:
            p.draw.rect(self.screen,self.buttons[key].col,self.buttons[key].rect())
            self.screen.blit(self.buttons[key].text_surface,self.buttons[key].pos)
            
   
    #setup functions
    def setupChildFile(self):
        filename = fileBox.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("CSV Files","*.csv*"),("all files","*.*")))
        if(filename != ""):
            self.camperFile = open(filename,"r")

    def setupCounselorFile(self):
        filename = fileBox.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("CSV Files","*.csv*"),("all files","*.*")))
        if(filename != ""):
            self.counselorFile = open(filename,"r")    

    def outputToCsvFile(self):
        print("CALLED outputToCsvFile")

    def setupPygame(self):  
        self.screen = p.display.set_mode(size = (self.Width,self.Height))
        clock = p.time.Clock()

class Button():
    def __init__(self,pos,size,function,col,text = ""):
        self.funct = function
        self.pos = pos
        self.size = size
        self.col = col
        self.text = text
        my_font = p.font.Font(p.font.get_default_font(), self.size[1] - 5)
        self.text_surface = my_font.render(self.text, False, (0, 0, 0))
        self.size = self.text_surface.get_size()
        self.pos = (self.pos[0] - (self.size[0] / 2) , self.pos[1] - (self.size[1] / 2))

    def rect(self):
        rect = p.Rect(self.pos,self.size)
        return rect
     
    def is_clicked(self,pos):
        if self.rect().collidepoint(pos):
            return True
        return False
		

if __name__ =="__main__":
	main()


