import pygame, sys

class Button:
    def __init__(self,text,width,height,pos,elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        # Top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_colour = '#475F77'
        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_colour = '#354B5E'
        # Text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        pygame.draw.rect(screen,self.bottom_colour,self.bottom_rect,border_radius = 90)
        pygame.draw.rect(screen,self.top_colour,self.top_rect,border_radius = 90)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.text_rect.collidepoint(mouse_pos):
            self.top_colour = '#D74B4B'
            if pygame.mouse.get_pressed()[0] == True:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    quit = True
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = '#475F77'
pygame.init()
sw = 500
sh = 500
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption('Main Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)

background = pygame.transform.scale2x(pygame.image.load("./Assets/Levels_and_backgrounds/Main_menu_backgound.png"))

button1 = Button('Quit',200,40,(25,450),6)
button2 = Button('Credits',200,40,(25,350),6)
button3 = Button('How To Play',200,40,(275,450),6)
button4 = Button('Play',200,40,(275,350),6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background,(0,0))            

    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()

    pygame.display.flip()
    clock.tick(60)