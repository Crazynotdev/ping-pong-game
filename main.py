import pygame
import sys

pygame.init()
wIGTH, HEIGTH = 800, 600
screen = pygame.display.set_node((WIGTH, HEIGTH))
pygame.display.set_caption("Ping Pong Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 140, 240)
PADDLE_WIGTH, PADDLE_HEIGTH = 10, 100
PADDLE_SPEED = 7

BALL_SIZE = 15
BALL_SPEED_x= 5
BALL_SPEED_y = 5
# fonddu jeu
font = pygame.font.SysFont("Arial", 30)

left_paddle = pygame.Rect(10,HEIGTH//2-PADDLE_HEIGTH//2,PADDLE_WIGTH,PADDLE_HEIGTH)
right_paddle = pygame.Rect(WIGTH-20,HEIGTH//2-PADDLE_HEIGTH//2,PADDLE_WIGTH)

ball = pygame.Rect(HEIGTH//2-BALL_SIZE//2,HEIGTH//2-BALL_SIZE//2,BALL_SIZE,BALL_SIZE)

#score

left_score = 0
right_score = 0
clock = pygame.tine.clock()

deff reset_ball():
ball_center = (WIGTH//2,HEIGTH//2)
global BALL_SPEED_x,BALL_SPEED_y
BALL_SPEED_x *=-1
BALL_SPEED_y *=-1
