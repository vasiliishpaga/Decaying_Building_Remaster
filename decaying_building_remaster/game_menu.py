import pygame
W, H = 600, 600
dict_setting_window = {
                "WIDTH": 600, 
                "HEIGHT": 600,
                "COLOR": (255, 120, 0),
                "CAPTION": "Decayin Building Remaster - Menu",
                "FPS": 60
}

dict_font = {
                "FONT_SIZE": 50,
                "COLOR_TEXT": (163, 161, 84)
}

dict_setting_button = {
                "WIDTH_button": 150, 
                "HEIGHT_button": 50,
}

class Button:
    def __init__(self, width = None, height = None, x = None, y = None, color = (50, 205, 65), text = None):
        self.WIDTH = dict_setting_button["WIDTH_button"] 
        self.HEIGHT = dict_setting_button["HEIGHT_button"]
        self.X = x
        self.Y = y
        self.COLOR = color
        self.TEXT = text
        self.FONT = pygame.font.Font("comicsansms", 32,)
        self.BUT_CAPTION = self.FONT.render(self.TEXT, True, dict_font["COLOR_TEXT"])
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)

    def blit_button(self, win):
        pygame.draw.rect(win, self.COLOR, self.RECT)
        win.blit(self.BUT_CAPTION, (self.X + self.WIDTH // 8, self.Y + self.HEIGHT // 3))






def show_menu():
    win = pygame.display.set_mode((dict_setting_window["WIDTH"], dict_setting_window["HEIGHT"]))
    pygame.display.set_caption(dict_setting_window["CAPTION"])

    clock = pygame.time.Clock()


    button_game = Button(
                    width= dict_setting_window["WIDTH"] //2,
                    height= dict_setting_window["HEIGHT"] // 2,
                    x = dict_setting_window["WIDTH"] // 2 - 60,
                    y = dict_setting_window["HEIGHT"] // 2 -dict_setting_window["HEIGHT"] // 4,
                    text = "GAME"
    )


    button_quit = Button(
                    width= dict_setting_window["WIDTH"] //2,
                    height= dict_setting_window["HEIGHT"] // 2,
                    x = dict_setting_window["WIDTH"] // 2 - 60,
                    y = dict_setting_window["HEIGHT"] // 2 -dict_setting_window["HEIGHT"] // 4 + dict_setting_button["HEIGHT_button"] + 5,
                    text = "QUIT" 
    )

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if button_game.RECT.collidepoint(x, y):
                    show = False
                    import decaying_building_remaster
                if button_quit.RECT.collidepoint(x, y):
                    show = False
                
        win.blit(menu_back, (0,0))
        button_game.blit_button(win) 
        button_quit.blit_button(win)
        
        clock.tick(dict_setting_window["FPS"])
        pygame.display.flip()



show_menu()