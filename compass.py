def direction(facing: str, turn: int) -> str:
    directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    try:
        if not isinstance(facing, str) or not isinstance(turn, int):
            raise TypeError

        if (turn % 45 != 0) or (facing not in directions) or abs(turn) > 1080:
            raise ValueError

        azimuth_steps = turn // 45
        start = directions.index(facing)
        direction_index = (start + azimuth_steps) % len(directions)
        return directions[direction_index]
    except TypeError:
        print('Invalid argument data type')
    except ValueError:
        print('Incorrect argument values')
