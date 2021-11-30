import time
import pygame
import numpy as np
import gym
import os
from gym.spaces import Box


WIDTH, HEIGHT = 1000, 500
ARM_WIDTH, ARM_HEIGHT = 150, 100
REIBUNG = 0.3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 200, 200)
RED = (255, 26, 0)
FPS = 30
BODEN = pygame.Rect(0, 270, WIDTH, 10)
ROBOTER_ARM_IMAGE = pygame.image.load(os.path.join('Bilder', 'Roboterarm.png'))
ROBOTER_ARM = pygame.transform.scale(ROBOTER_ARM_IMAGE, (ARM_WIDTH, ARM_HEIGHT))
arm = pygame.Rect(0, 190, ARM_WIDTH, ARM_HEIGHT)
c_times = 0
clicked_times = 0
position_goal_x = 600
position_goal_y = 220

class CustomEnv(gym.Env):
    def __init__(self, env_config={}):
        self.action_space = Box(low=np.array([0]), high=np.array([30]))
        self.observation_space = Box(low=np.array([0]), high=np.array([WIDTH]))
        self.x = 150
        self.y = 220
        self.vel_x = 0
        self.state = 150



    def init_render(self):
        import pygame
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.WIN.blit(ROBOTER_ARM, (0, 190))


    def reset(self):
        self.x = 150
        self.state = self.x
        return self.state
        # return observation


    def step(self, action):
        # action = initial force
        # apply Acceleration
        acceleration = -1 * REIBUNG
        self.vel_x = action
        # self.vel_x = 10
        while self.vel_x > 0:
            self.vel_x = self.vel_x - 0.3
            self.x = self.x + self.vel_x
            self.state = self.x
            done = False
        if self.vel_x < 0:
            self.state = self.x
            done = True
        if self.x > WIDTH:
            self.x = self.x - WIDTH
        elif self.x < 0:
            self.x = self.x + WIDTH


        difference = abs(self.state - position_goal_x)
        reward = -1 * difference
        info = {}
        return self.state, reward, done, info

    def render(self, arm, c_times=0):
        self.WIN.fill(WHITE)
        self.WIN.blit(ROBOTER_ARM, (arm.x, arm.y))
        pygame.draw.circle(self.WIN, RED, (position_goal_x, position_goal_y), 6)
        pygame.draw.circle(self.WIN, BLUE, (int(self.x), int(self.y)), 6)
        text_force = pygame.font.SysFont(None, 50)
        img = text_force.render("Set force: {}".format(str(round(c_times))), True, BLUE)
        self.WIN.blit(img, (200, 20))
        pygame.display.update()


'''env = CustomEnv()
env.init_render()
run = True'''

'''while run:
    env.clock.tick(FPS)
    get_event = pygame.event.get()
    for event in get_event:
        if event.type == pygame.QUIT:
            run = False
    for i in range(1):
        n_state, reward, done, info = env.step(16.6)
        env.render(arm, c_times=0)
pygame.quit()
print(n_state, reward, done, info)'''

'''env = CustomEnv()
for i in range(10):
    state = env.reset()
    done = False
    score = 0
    while not done:
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(i, score))'''
