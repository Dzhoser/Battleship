
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, _len):
        self.points = []
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
            p = self.convert_coord_to_point(inp_str)
            if isinstance(p, Point):
                self.points.append(p)
                i += 1
        self.len = _len

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
                self.pole[point.y - 1][point.x - 1] = "■"
        else:
            print("Данный корабль нельзя разместить в данной точке")


    def is_available(self, _s):
        self.tr = []
        self.tr.clear()
        for _point in _s.points:
            if self.forbidden_zone[_point.y - 1][_point.x - 1] == "O":
                self.tr.append(True)
            else:
                self.tr.append(False)
        return all(self.tr)

    def change_forbidden_zone(self, ship):
        if self.is_available(ship):
            for point in ship.points:
                _L = self.forbiden_points(point)
                for f_point in _L:
                    if 0 <= f_point.x - 1 < 6 and 0 <= f_point.y - 1 < 6:
                        self.forbidden_zone[f_point.y - 1][f_point.x - 1] = "f"


    @staticmethod
    def forbiden_points(_point):
        L = []
        L.append(_point)
        L.append(Point(_point.x + 1, _point.y))
        L.append(Point(_point.x, _point.y + 1))
        L.append(Point(_point.x - 1, _point.y))
        L.append(Point(_point.x, _point.y - 1))
        return L

    def fdraw(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i in range(6):
            line = str(i+1) + " | "
            for j in range(6):
                line += self.forbidden_zone[i][j] + " | "
            print(line)


# m1 = Pole()
# m1.draw()


class Gamelogic:
    def __init__(self):
        self.intro()
        self.put_ship_to_gamer_pole()

    def intro(self):
        print("Игра морской бой")
        print("поле 6х6")

    def put_ships_to_gamer_pole(self):
        pass
        self.gamer_pole = Pole()
        i = 0
        ships = []
        while i < 4:
            print("Введите координаты одноклеточного корабля x y")
            inp_str = input()
            s = Ship([self.convert_coord_to_point(inp_str)])
            if self.gamer_pole.is_available(s):
                ships.append(s)
                self.gamer_pole.add_ship(s)
            i += 1









gl = Gamelogic()
gl.put_ships_to_gamer_pole()
gl.gamer_pole.draw()

# s1 = Ship(3)
# s2 = Ship(1)

# print(s1.points)

# p = Pole()
# p.add_ship(s1)
# p.change_forbidden_zone(s1)
# p.add_ship(s2)
# p.change_forbidden_zone(s2)
# p.draw()
# print("")
# p.fdraw()

