from window import Main_Window
import pygame


while True:
    main = Main_Window()
    main.main_f()
    pygame.display.update()
    main.clock.tick(main.FPS)