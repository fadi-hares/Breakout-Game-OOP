from turtle import Turtle

BLOCKS_POSITIONS = [(300, 180), (200, 180), (100, 180), (0, 180), (-100, 180), (-200, 180), (-300, 180),
                    (320, 150), (220, 150), (120, 150), (20, 150), (-80, 150), (-180, 150), (-280, 150),
                    (300, 120), (200, 120), (100, 120), (0, 120), (-100, 120), (-200, 120), (-300, 120)]


class Blocks:
    def __init__(self):
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        for position in BLOCKS_POSITIONS:
            block = Turtle()
            block.shape('square')
            block.color('white')
            block.shapesize(0.5, 3)
            block.penup()
            block.goto(position)
            self.blocks.append(block)
    
    def remove_block(self, block):
        block.hideturtle()
        self.blocks.remove(block)
