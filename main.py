from constant import *
from space_shooting import SpaceShooting

if __name__ == '__main__':
  space_shooting = SpaceShooting(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, fps=FPS)
  space_shooting.loop_game()
