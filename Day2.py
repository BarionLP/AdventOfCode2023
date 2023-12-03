import math

class Cubes:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def power(self) -> int:
        return self.red * self.green * self.blue

    def parse(txt: str):
        red = 0
        blue = 0
        green = 0
        for val in txt.split(", "):
            tmp = val.split(" ")
            if(tmp[1] == "red"):
                red += int(tmp[0])
            if(tmp[1] == "green"):
                green += int(tmp[0])
            if(tmp[1] == "blue"):
                blue += int(tmp[0])

        return Cubes(red, green, blue)


class Game:
    def __init__(self, id: int, hints: list[Cubes]) -> None:
        self.id = id
        self.hints = hints

    def parse(txt: str):
        tmp = txt.split(':')
        id = int(tmp[0].split(' ')[1])

        hints = []
        for raw_hint in tmp[1].strip().split("; "):
            hints.append(Cubes.parse(raw_hint))

        return Game(id, hints)
    
    def min_cubes(self) -> Cubes:
        red = max(self.hints, key= lambda h: h.red).red
        green = max(self.hints, key=lambda h: h.green).green
        blue = max(self.hints, key=lambda h: h.blue).blue
        
        return Cubes(red, green, blue)

max_cubes = Cubes(12, 13, 14)
def game_possible(game: Game) -> bool:
    for hint in game.hints:
        if max_cubes.red < hint.red or max_cubes.green < hint.green or max_cubes.blue < hint.blue:
            return False
    return True

if __name__ == '__main__':
    games: list[Game] = []
    with open("input.txt", "r") as file:
        for line in file:
            games.append(Game.parse(line.strip()))

    result1 = 0
    result2 = 0
    for game in games:
        result2 += game.min_cubes().power()
        if game_possible(game):
            result1 += game.id
    
    print(result1)
    print(result2)