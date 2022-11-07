import random as rnd

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"x={self.x}  y={self.y}")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Ship:
    def __init__(self, points):
        self.points = points
        self.isalive = True
        self.hitpoints = []

    def set_state(self, isalive):
        self.isalive = isalive

    def get_state(self):
        return self.isalive

    def hit(self, _point):
        if _point in self.points:
            self.hitpoints.append(_point)
            return True
        else:
            return False

    def check_state(self):
        if set(self.points) == set(self.hitpoints):
            self.set_state(False)

    @staticmethod
    def convert_coord_to_point( inp_str):
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
            return True
        else:
            #print("Данный корабль нельзя разместить в данной точке")
            return False


    def is_available(self, _s):
        tr = []
        # self.tr.clear()
        for _point in _s.points:
            if self.forbidden_zone[_point.y - 1][_point.x - 1] == "O":
                tr.append(True)
            else:
                tr.append(False)
        a = all(tr)
        del(tr)
        return a

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
        # self.put_ships_to_gamer_pole()
        self.put_ships_to_computer_pole()

    def intro(self):
        print("Игра морской бой")
        print("поле 6х6")

    def put_ships_to_gamer_pole(self):
        self.gamer_pole = Pole()
        i = 0
        self.gships = []
        points = []

        _len = 3
        print("Введите координаты трехклеточного корабля x y")
        while i < _len:
            inp_str = input()
            p = Ship.convert_coord_to_point(inp_str)
            if isinstance(p, Point):
                points.append(p)
                i += 1

        self.gamer_pole.add_ship(Ship(points))
        self.gamer_pole.change_forbidden_zone(Ship(points))
        self.gships.append(Ship(points))
        i = 0
        k = 0
        points = []

        _len = 2
        while k < 2:
            points = []
            print("Введите координаты двухклеточного корабля x y")
            while i < _len:
                inp_str = input()
                p = Ship.convert_coord_to_point(inp_str)
                if isinstance(p, Point):
                    points.append(p)
                    i += 1
            i = 0
            if self.gamer_pole.add_ship(Ship(points)):
                self.gamer_pole.change_forbidden_zone(Ship(points))
                self.gships.append(Ship(points))
                k += 1

        points = []
        i = 0
        k = 0
        _len = 1
        while k < 4:
            points = []
            print("Введите координаты одноклеточного корабля x y")
            while i < _len:
                inp_str = input()
                p = Ship.convert_coord_to_point(inp_str)
                if isinstance(p, Point):
                    points.append(p)
                    i += 1
            i = 0
            if self.gamer_pole.add_ship(Ship(points)):
                self.gamer_pole.change_forbidden_zone(Ship(points))
                self.gships.append(Ship(points))
                k += 1


    def put_ships_to_computer_pole(self):
        self.comp_pole = Pole()
        self.cships = []
        #разместим трехклеточный корабль
        start_point = Point(rnd.randint(1, 4), rnd.randint(1, 4))
        # print(start_point)
        direction = rnd.randint(0, 1) #направление размещения 0 - горизонталь 1 - вертикаль
        _points=[]
        _points.append(start_point)
        for i in range(3):
            if direction == 0:
                _points.append(Point(start_point.x+i, start_point.y))
            if direction == 1:
                _points.append(Point(start_point.x, start_point.y+i))

        self.comp_pole.add_ship(Ship(_points))
        self.comp_pole.change_forbidden_zone(Ship(_points))
        self.cships.append(Ship(_points))

        # разместим двухклеточные корабли
        itt = 0
        while True:
            start_point = Point(rnd.randint(1, 5), rnd.randint(1, 5))
            # print(start_point)
            direction = rnd.randint(0, 1)  # направление размещения 0 - горизонталь 1 - вертикаль
            _points = []
            _points.append(start_point)
            for i in range(2):
                if direction == 0:
                    _points.append(Point(start_point.x + i, start_point.y))
                if direction == 1:
                    _points.append(Point(start_point.x, start_point.y + i))

            if self.comp_pole.add_ship(Ship(_points)):
                self.comp_pole.change_forbidden_zone(Ship(_points))
                self.cships.append(Ship(_points))
                itt += 1
            if itt == 2:
                break

        # разместим одноклеточные корабли
        itt = 0
        while True:
            start_point = Point(rnd.randint(1, 6), rnd.randint(1, 6))
            # print(start_point)
            direction = rnd.randint(0, 1)  # направление размещения 0 - горизонталь 1 - вертикаль
            _points = []
            _points.append(start_point)
            for i in range(1):
                if direction == 0:
                    _points.append(Point(start_point.x + i, start_point.y))
                if direction == 1:
                    _points.append(Point(start_point.x, start_point.y + i))

            if self.comp_pole.add_ship(Ship(_points)):
                self.comp_pole.change_forbidden_zone(Ship(_points))
                self.cships.append(Ship(_points))
                itt += 1
            if itt == 4:
                break

        self.comp_pole.draw()
        print("")
        self.comp_pole.fdraw()
        print(self.cships)











# gl = Gamelogic()
# gl.put_ships_to_gamer_pole()
# gl.gamer_pole.draw()



s1 = Ship([Point(1, 1), Point(1, 2)])
s1.hit(Point(2, 2))
s1.check_state()
print(s1.get_state())
s1.hit(Point(1, 1))
s1.check_state()
print(s1.get_state())
s1.hit(Point(1, 2))
s1.check_state()
print(s1.get_state())
