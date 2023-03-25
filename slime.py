import pygame


class Slime(object):

    def __init__(self,pos):
        self.x=pos[0]
        self.y=pos[1]
        self.image = pygame.image.load('images/PurpleSlime/Purple_Idle1.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.d = 100
        self.jump_count = 10



    def update_pos(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
        self.rect=pygame.Rect(self.x,self.y,self.image_size[0],self.image_size[1])

    def move_right(self,dt):
        self.x+=self.d*dt


    def move_left(self,dt):
        self.x-=self.d*dt


    def jump(self):
        if self.jump_count >=-10:
            self.y-= (self.jump_count**2)*0.5
            self.jump_count-=1
            print(self.y)
        else:
            jump_count = 10
            self.y+=(self.jump_count**2)*0.5
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            return False

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        return True


    def move(self, direction,dt):
        if direction == 'left':
            self.move_left(dt)
        if direction == 'right':
            self.move_right(dt)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    # def jump(self):
    #     self.y = self.y - self.jump_v
    #     self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    #     self.jump_v = self.jump_v - .5
    #     if self.y >= self.INITIAL_Y:
    #         self.jump_v = 10
    #         return True
    #     return False
    #
    # def stop_jump(self):
    #     self.jump_v = 10
    #
    # def fall(self):
    #     self.y = self.y + 3
    #     self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def animate_idle(self,i):
        self.image = pygame.image.load('images/PurpleSlime/Purple_Idle'+str(i)+'.png')

    def animate_jump(self,i):
        self.image = pygame.image.load('images/PurpleSlime/Purple_HighJump'+str(i)+'.png')

    def animate(self,state,i):
        if state == 'idle':
            self.animate_idle(i)
        if state == 'jump':
            self.animate_jump(i)

        self.image = pygame.transform.scale(self.image, (80, 80))