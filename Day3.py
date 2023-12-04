class Engine:
    def __init__(self, plan: list[str]) -> None:
        self.plan = plan
        self.rows = len(self.plan)
        self.columns = len(self.plan[0])-1 #ignore newline

    def parse():
        engine: list[str] = []
        with open("input.txt", "r") as file:
            for line in file:
                engine.append(line)
        return Engine(engine)
    
    def get(self, row: int, column: int) -> str:
        return self.plan[row][column]
    
    def is_symbol(self, row: int, column: int) -> bool:
        return self.get(row, column) != "." and not self.is_digit(row, column)
    
    def is_digit(self, row: int, column: int) -> bool:
        return self.get(row, column).isdigit()
    
    def has_around(self, row: int, column: int, predicate) -> bool:
        not_upper = row > 0
        not_lower = row < self.rows-1
        not_left = column > 0
        not_right = column < self.columns-1
        
        if not_left:
            if predicate(row, column-1):
                return True
            if not_upper:
                if predicate(row-1, column-1):
                    return True
            if not_lower:
                if predicate(row+1, column-1):
                    return True
                
        if not_right:
            if predicate(row, column+1):
                return True
            if not_upper:
                if predicate(row-1, column+1):
                    return True
            if not_lower:
                if predicate(row+1, column+1):
                    return True
        
        if not_upper:
            if predicate(row-1, column):
                return True
        if not_lower:
            if predicate(row+1, column):
                return True
            
    def get_number(self, row, column) -> int:
        if not self.is_digit(row, column): return None

        while column-1 >= 0 and self.is_digit(row, column-1):
            column -= 1

        val = ""
        while column < self.columns and self.is_digit(row, column):
            val += self.get(row, column)
            column += 1

        return int(val)

    def get_engine_sum(self) -> int:
        result = 0

        row = 0
        while row < engine.rows:
            column = 0
            while column < engine.columns:
                if not engine.is_digit(row, column): 
                    column+=1
                    continue
                has_symbol = False
                value = ""
                while engine.is_digit(row, column):
                    if not has_symbol:
                        has_symbol = engine.has_around(row, column, lambda row, column: engine.is_symbol(row, column))
                    value += engine.plan[row][column]
                    column += 1
                if(has_symbol): result += int(value)
                column+=1
            row += 1

        return result
            
    def is_gear_symbol(self, row: int, column: int) -> bool:
        return self.get(row, column) == "*"
    
    def get_gear_ratio(self, row: int, column: int) -> int:
        if not self.is_gear_symbol(row, column): return 0
        numbers = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for dr, dc in directions:
            number = self.get_number(row+dr, column+dc)
            if number is not None:
                numbers.add(number)

        if len(numbers) == 2:
            tmp = list(numbers)
            return tmp[0] * tmp[1]

        return 0



if __name__ == '__main__':
    engine = Engine.parse()
    res = 0
    for row in range(0, engine.rows):
        for column in range(0, engine.columns):
            res += engine.get_gear_ratio(row, column)

    print(res)
    
    print(engine.get_engine_sum())