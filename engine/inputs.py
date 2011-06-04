#! /usr/bin/python

import pygame,sys

from pygame.locals import *

#Real or fake inputs, for CPU and player
#To handle key up, keydown and joystick

class Inputs():
    def __init__(self, num_player=0):#num_player: to handle key configs (0=CPU)
        self.num_player=num_player
        self.R=False
        self.L=False
        self.U=False
        self.D=False
        self.A=False
        self.B=False
        self.C=False
        self.Esc=False
    def update(self):#read corresponding key for human player, of just release keys for CPU
        if (self.num_player==1):#it won't work this way... have to hanlde all events at the same time, instead they are lost (won't work with 2 players)
            # check for events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.Esc = True
                    if event.key == K_LEFT:
                        self.L = True
                    if event.key == K_RIGHT:
                        self.R = True
                    if event.key == K_UP:
                        self.U = True
                    if event.key == K_DOWN:
                        self.D = True
                    if event.key == ord('w'):
                        self.B = True
                    if event.key == ord('x'):
                        self.A = True
                    if event.key == ord('c'):
                        self.C = True
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.Esc = False
                    if event.key == K_LEFT:
                        self.L = False
                    if event.key == K_RIGHT:
                        self.R = False
                    if event.key == K_UP:
                        self.U = False
                    if event.key == K_DOWN:
                        self.D = False
                    if event.key == ord('w'):
                        self.B = False
                    if event.key == ord('x'):
                        self.A = False
                    if event.key == ord('c'):
                        self.C = False
        if (self.num_player==0):#CPU: the inputs are trigged in PlayerCPU code
            self.R=False
            self.L=False
            self.U=False
            self.D=False
            self.A=False
            self.B=False
            self.C=False
            self.Esc=False
                    

