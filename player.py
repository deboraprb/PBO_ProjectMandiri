from game_object import GameObject

class PlayerCharacter(GameObject):
    SPEED = 10

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - self.height:
            self.y_pos = max_height - self.height

    def detection_collision(self, other):
        offset = (int(other.x_pos - self.x_pos), int(other.y_pos - self.y_pos))
        return self.mask.overlap(other.mask, offset) is not None
    