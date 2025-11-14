
class Position(object):
    """Directions are: (1,0) = east, (0,-1) = south, (-1,0) = west, (0,1) = north"""
    DIRECTIONS = [(1,0),(0,-1),(-1,0),(0,1)]

    def get_right(position, direction):
        """Get coordinate to the right of the position relative to direction"""
        d = Position.turn_right(direction)
        return Position.get_forward(position, d)

    def get_left(position, direction):
        """Get coordinate to the left of the position relative to direction"""
        d = Position.turn_left(direction)
        return Position.get_forward(position, d)

    def get_forward(position, direction):
        """Get coordinate in front of the position relative to direction"""
        return (position[0] + direction[0],
            position[1] + direction[1])

    def get_back(position, direction):
        """Get coordinate behind the current position relative to direction"""
        direction = Position.turn_right(direction)
        d = Position.turn_right(direction)
        return Position.get_forward(position, d)

    def turn_right(direction):
        """Returns the direction to the right"""
        index = (Position.DIRECTIONS.index(direction) + 1) % 4
        return Position.DIRECTIONS[index]

    def turn_left(direction):
        """Returns the direction to the left"""
        index = (Position.DIRECTIONS.index(direction) - 1) % 4
        return Position.DIRECTIONS[index]
