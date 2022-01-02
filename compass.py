def direction(facing: str, turn: int) -> str:
    directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    azimuth_steps = turn // 45
    start = directions.index(facing)
    direction_index = (start + azimuth_steps) % len(directions)
    return directions[direction_index]
