from game_object import GameObject

class EnemyCharacter(GameObject):
    SPEED = 5

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - self.width:
            self.SPEED = -abs(self.SPEED)

        self.x_pos += self.SPEED