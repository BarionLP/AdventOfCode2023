class Card:
    def __init__(self, id: int, wins: list[int], numbers: list[int]):
        self.id = id
        self.wins = wins
        self.numbers = numbers
        self.total_wins = self.calc_wins()

    def value(self) -> int:
        val = 0
        for n in self.numbers:
            if n in self.wins:
                if val == 0:
                    val = 1
                else:
                    val = val * 2
        return val
    
    def calc_wins(self):
        val = 0
        for n in self.numbers:
            if n in self.wins:
                val += 1
        return val

    def parse(txt: str):
        tmp = txt.strip().split(' ')
        wins = []
        idx = 0
        while ":" not in tmp[idx]:
            idx+=1

        id = int(tmp[idx][:-1])

        idx+=1
        while tmp[idx] != '|':
            if tmp[idx]: wins.append(int(tmp[idx]))
            idx+=1
        idx+=1
        nums = []
        while idx < len(tmp):
            if tmp[idx]: nums.append(int(tmp[idx]))
            idx+=1

        return Card(id, wins, nums)
        

if __name__ == '__main__':
    cards: list[Card] = []
    with open("input.txt") as file:
        for line in file:
            cards.append(Card.parse(line))

    
    #wins = [cards[0]]
    idx = 0

    while idx < len(cards):
        card = cards[idx]
        for i in range(0, card.total_wins):
            cards.append(cards[card.id+i])
        idx+=1

    print(len(cards))
