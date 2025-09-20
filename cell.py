#cell.py is an object that represents each cell in the grid of life
import pygame

class Cell:
    
    #initialize new cell
    def __init__(self, x, y, size):
        #Setting cell coordinates and size on grid
        self.x_pos = x
        self.y_pos = y
        self.size = size

        #Setting is_alive
        self.is_alive = False

        #Setting color (initialized cells should be white)
        self.color = (255, 255, 255)

        #Setting team (initialized cells should be none - possible Green, Red, Blue)
        self.team = None

    def set_alive(self, team):
        #Sets cell to alive
        self.is_alive == True

        #Sets correct team
        self.team = team
        match self.team:
            case 'green':
                self.color = (255, 0, 0)
            case 'red':
                self.color = (0, 255, 0)
            case 'blue':
                self.color = (0, 0, 255)

    def get_alive(self):
        #Returns alive status
        return self.is_alive
    
    def set_dead(self):
        #Sets cell to dead
        self.is_alive = False

        #Remove team reference
        self.team = None

        #Set color to white
        self.color = (255, 255, 255)
    
    def get_color(self):
        #Returns cell's color
        return self.color
    
    def get_team(self):
        #Returns cell's team
        return self.team

    def get_position(self):
        #Returns cell's position
        return (self.x, self.y)

    
