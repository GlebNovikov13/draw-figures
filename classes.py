class figure():
    x = 0
    y = 0

    def plos(self):
        return 0


class square(figure):
    a = 0

    def __init__(self, x, y, a):
        self.a = a
        self.x = x
        self.y = y
        # print(self.a, self.x, self.y)

    def plos(self):
        return self.a * self.a

    def info(self):
        print('square', 'center , x: ', self.x, self.y, 'a: ', self.a)

    def draw(self, screen):
        draw = screen.arr
        for i in range(self.x, self.a + self.x):
            for j in range(self.y, self.a + self.y):
                s = draw[i][0:j] + 'k' + draw[i][j + 1:len(draw[i])]
                draw[i] = s


class rectangle(square):
    b = 0

    def __init__(self, x, y, b, a):
        self.a = a
        self.x = x
        self.y = y
        self.b = b

    def plos(self):
        return self.a * self.b

    def info(self):
        print('square', 'center , x: ', self.x, self.y, 'a: ', self.a, 'b:', self.b)

    def draw(self, screen):
        draw = screen.arr
        for i in range(self.x, self.a + self.x):
            for j in range(self.y, self.b + self.y):
                s = draw[i][0:j] + 'p' + draw[i][j + 1:len(draw[i])]
                draw[i] = s


class screen():
    arr = list()
    wight = 0
    height = 0

    def __init__(self, wight, height):
        self.height = height
        self.wight = wight
        for w in range(0, self.wight):
            str = '*'
            for h in range(0, self.height):
                str += '*'
            self.arr.append(str)

    def show(self):
        for w in range(0, len(self.arr)):
            print(self.arr[w])

    def set_arr(self, arr):
        self.arr = arr

    def show_in_file(self):
        with open('screen.txt', 'w') as s:
            for w in range(0, len(self.arr)):
                s.write(str(self.arr[w]) + '\n')


class dot(figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        draw = screen.arr
        s = draw[self.x][0:self.y] + '+' + draw[self.x][self.y + 1:len(draw[self.x])]
        draw[self.x] = s


class round(dot):
    def __init__(self, r1, r2, r):
        self.r1 = r1
        self.r2 = r2
        self.r = r

    def draw(self, screen):
        draw = screen.arr
        for i in range(0, len(draw)):
            for j in range(0, len(draw[i])):
                if ((i - self.r1) ** 2 + (j - self.r2) ** 2 <= self.r ** 2):
                    s = draw[i][0:j] + '#' + draw[i][j + 1:len(draw[i])]
                    draw[i] = s


class triangle(figure):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self, screen):
        draw = screen.arr

        k12 = (self.y2 - self.y1) / (self.x2 - self.x1)
        b12 = self.y1 - k12 * self.x1

        k13 = (self.y1 - self.y3) / (self.x1 - self.x3)
        b13 = self.y3 - k13 * self.x3

        k23 = (self.y2 - self.y3) / (self.x2 - self.x3)
        b23 = self.y2 - k23 * self.x2
        z1 = 0
        z2 = 0
        z3 = 0
        if self.y1 >= (k23 * self.x1 + b23):
            z1 = 1
        if self.y2 >= (k13 * self.x2 + b13):
            z2 = 1
        if self.y3 >= (k12 * self.x3 + b12):
            z3 = 1
        for i in range(0, len(draw)):
            for j in range(0, len(draw[i])):
                u1 = 0
                u2 = 0
                u3 = 0
                if j >= (k23 * i + b23):
                    u1=1
                if j >= (k13 * i + b13):
                    u2=1
                if j >= (k12 * i + b12):
                    u3=1
                if (z1==u1) and (z2==u2) and (z3==u3):

                    s = draw[i][0:j] + 'T' + draw[i][j + 1:len(draw[i])]
                    draw[i] = s
