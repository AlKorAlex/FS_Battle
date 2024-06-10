from window import Main_Window
import pygame

main = Main_Window()
main2 = Main_Window()
while True:
    main.main_f()
    main2.main_f()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
