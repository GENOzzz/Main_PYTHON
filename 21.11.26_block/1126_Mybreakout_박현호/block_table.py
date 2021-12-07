from tkinter import*
#tablemodule
class table:
    def __init__(self,window,width,height,bg_color):
        self.width=width
        self.height=height
        self.bg_color=bg_color

        self.canvas=Canvas(window,width=self.width,height=self.height,bg=self.bg_color)
        self.canvas.pack()
        
        font = ("monaco", 60)
        self.textbox = self.canvas.create_text(315,150, font=font, fill = "coral")
        self.scoreboard = self.canvas.create_text(self.width/2, 400, font=font, fill = "plum")
        


    def draw_bat(self,bat):
        x1=bat.x_posn
        y1=bat.y_posn
        x2=x1+bat.width
        y2=y1+bat.height
        color=bat.color
        return self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    
    def draw_block(self,block):
        x1=block.x_posn
        y1=block.y_posn
        x2=x1+block.width
        y2=y1+block.height
        color=block.color
        return self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    
    def draw_ball(self,ball):
        x1=ball.x_posn
        y1=ball.y_posn
        width=x1+ball.width
        height=y1+ball.height
        color=ball.color
        return self.canvas.create_oval(x1,y1,width,height,fill=color,outline="snow")
    
    def move_item(self,item,x1,y1,x2,y2):
        self.canvas.coords(item,x1,y1,x2,y2)
        
    def remove_item(self,item):
        self.canvas.delete(item)
                
    def draw_score(self,left,right):
        scores = str(right) + "  " + str(left)
        self.canvas.itemconfigure(self.scoreboard,text=scores)

    def draw_text(self,text):
        text = str(text)
        self.canvas.itemconfigure(self.textbox,text=text)
        
    def change_color(self,item,c):
        self.canvas.itemconfigure(item,fill=c)
        
        
        
        
