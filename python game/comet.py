import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super(Comet, self).__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 8)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 300)
        self.comet_event = comet_event


    def remove(self):
         self.comet_event.all_comets.remove(self)

         if len(self.comet_event.all_comets) == 0:
             print("evenement fini")
             self.comet_event.reset_percent()
             self.comet_event.game.spawn_monster()
             self.comet_event.game.spawn_monster()
             self.comet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 510:
            print("Sol")
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                print("Fini")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
            self, 
            self.comet_event.game.all_players
            ):
            print("Joueur touche")
            self.remove()
            self.comet_event.game.player.damage(20)
            
