
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, points):
        self.points = []
        self.points = points
        self.len = len(points)
        self.isalife = True

    def set_state(self, isalife):
        self.isalife = isalife

    def convert_coord_to_point(self, inp_str):
        coord = inp_str.split()
        if not (coord[0].isdigit()) or not (coord[0].isdigit()):
            print("Введите числа")
            return False
        L = list(map(int, coord))
        if len(L) != 2:
            print("Введите 2 координаты")
            return False
        if L[0] <= 0 or L[0] > 6:
            print("Координата х вне допустимых значений")
            return False
        if L[1] <= 0 or L[1] > 6:
            print("Координата y вне допустимых значений")
            return False

        return Point(L[0], L[1])

    def create_ship(self, _len):

        if _len == 1:
            _str = "Введите координаты одноклеточного корабля x y"
        elif _len == 2:
            _str = "Введите координаты двухклеточного корабля x y"
        elif _len == 3:
            _str = "Введите координаты трехклеточного корабля x y"
        else:
            print("Введено неверно значение длинны корабля")
            return
        print(_str)
        i = 0
        while i < _len:
            inp_str = input()
            p = self.convert_coord_to_point(self, inp_str)
            if isinstance(p, Point):
                self.points.append(p)
                i += 1
        self.len = _len


class Pole:
    def __init__(self):
        self.pole = []
        for i in range(6):
            self.pole.append(['O' for j in range(6)])
        self.forbidden_zone = []
        for i in range(6):
            self.forbidden_zone.append(['O' for j in range(6)])


    def draw(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i in range(6):
            line = str(i+1) + " | "
            for j in range(6):
                line += self.pole[i][j] + " | "
            print(line)

    def add_ship(self, _s):
        if self.is_available(_s):
            for point in _s.points:
                self.pole[point.y-1][point.x-1] = "■"


    def is_available(self, _s):

        return True





# m1 = Pole()
# m1.draw()


class Gamelogic:
    def __init__(self):
        self.intro()
        # self.put_ship_to_gamer_pole()

    def intro(self):
        print("Игра морской бой")
        print("поле 6х6")

    def put_ships_to_gamer_pole(self):
        pass
        # self.gamer_pole = Pole()
        # i = 0
        # ships = []
        # while i < 4:
        #     print("Введите координаты одноклеточного корабля x y")
        #     inp_str = input()
        #     s = Ship([self.convert_coord_to_point(inp_str)])
        #     if self.gamer_pole.is_available(s):
        #         ships.append(s)
        #         self.gamer_pole.add_ship(s)
        #     i += 1









# gl = Gamelogic()
# gl.put_ships_to_gamer_pole()
# gl.gamer_pole.draw()

s1 = Ship.create_ship(Ship, 3)
print(s1.points)

# p = Pole()
# p.add_ship(s1)
# p.draw()
