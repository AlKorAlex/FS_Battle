import pygame

class Check_Events():
    def __init__(self, game_stats):
        self.game_stats = game_stats
    def check_events(self, move):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if move == "choose_bk":
                    for j in range(0, 2):  # Нажатие на карты в руке у обоих игроков
                        for i in range(0, len(self.game_stats.players[j].battle_cards)):
                            button_clicked = self.game_stats.players[j].battle_cards[i].rect.collidepoint(
                                mouse_pos)
                            if button_clicked:
                                bk = self.game_stats.players[j].battle_cards[i]
                                print(bk.name)
                                return bk
