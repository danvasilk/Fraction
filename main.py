class Fraction:

    def __nod(self, data):
        _a, _b = data[0], data[1]
        while _b:
            _a, _b = _b, _a % _b
        return data[0] // _a, data[1] // _a

    def __init__(self, *args):
        if isinstance(args[0], str):
            if '/' in args[0]:
                self.numy, self.denomy = self.__nod(tuple(map(int, args[0].split('/'))))
            else:
                self.numy, self.denomy = (int(args[0]), 1)
        else:
            if len(args) == 2:
                self.numy, self.denomy = self.__nod(args)
            else:
                self.numy, self.denomy = (args[0], 1)

    def numerator(self, num=0):
        if num:
            if self.numy > 0:
                self.numy, self.denomy = self.__nod((abs(num), self.denomy))
                self.numy = -self.numy if num < 0 else self.numy
            elif self.numy < 0:
                self.numy, self.denomy = self.__nod((abs(num), self.denomy))
                self.numy = -self.numy if num > 0 else self.numy
        return abs(self.numy)

    def denominator(self, num=0):
        if num:
            if self.numy > 0:
                self.numy, self.denomy = self.__nod((self.numy, abs(num)))
                self.numy = -self.numy if num < 0 else self.numy
            elif self.numy < 0:
                self.numy, self.denomy = self.__nod((abs(self.numy), abs(num)))
                self.numy = -self.numy if num > 0 else self.numy
        return self.denomy

    def reverse(self):
        self.numy, self.denomy = self.__nod((self.denomy, self.numy))
        return self

    def __str__(self):
        return f'{self.numy}/{self.denomy}'

    def __repr__(self):
        return f"Fraction('{self.numy}/{self.denomy}')"

    def __neg__(self):
        return Fraction(-self.numy, self.denomy)

    def __add__(self, other):
        if isinstance(other, int):
            new_num = self.numy + other * self.denomy
            return Fraction(new_num, self.denomy)
        else:
            if self.denomy == other.denomy:
                new_num = self.numy + other.numy
                return Fraction(new_num, self.denomy)
            else:
                new_num = self.numy * other.denomy + other.numy * self.denomy
                new_denomy = self.denomy * other.denomy
                return Fraction(new_num, new_denomy)

    def __sub__(self, other):
        if isinstance(other, int):
            new_num = self.numy - other * self.denomy
            return Fraction(new_num, self.denomy)
        else:
            if self.denomy == other.denomy:
                new_num = self.numy - other.numy
                return Fraction(new_num, self.denomy)
            else:
                new_num = self.numy * other.denomy - other.numy * self.denomy
                new_denomy = self.denomy * other.denomy
                return Fraction(new_num, new_denomy)

    def __mul__(self, other):
        if isinstance(other, int):
            new_num = self.numy * other
            return Fraction(new_num, self.denomy)
        else:
            new_num = self.numy * other.numy
            new_denomy = self.denomy * other.denomy
            return Fraction(new_num, new_denomy)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_denomy = self.denomy * other
            return Fraction(self.numy, new_denomy)
        else:
            new_num = other.denomy * self.numy
            new_denomy = other.numy * self.denomy
            return Fraction(new_num, new_denomy)

    def __radd__(self, other):
        if isinstance(other, int):
            new_num = other * self.denomy + self.numy
            return Fraction(new_num, self.denomy)
        else:
            if self.denomy == other.denomy:
                new_num = other.numy + self.numy
                return Fraction(new_num, self.denomy)
            else:
                new_num = other.numy * self.denomy + self.numy * other.denomy
                new_denomy = self.denomy * other.denomy
                return Fraction(new_num, new_denomy)

    def __rsub__(self, other):
        if isinstance(other, int):
            new_num = other * self.denomy - self.numy
            return Fraction(new_num, self.denomy)
        else:
            if self.denomy == other.denomy:
                new_num = other.numy - self.numy
                return Fraction(new_num, self.denomy)
            else:
                new_num = other.numy * self.denomy - self.numy * other.denomy
                new_denomy = self.denomy * other.denomy
                return Fraction(new_num, new_denomy)

    def __rmul__(self, other):
        if isinstance(other, int):
            new_num = other * self.numy
            return Fraction(new_num, self.denomy)
        else:
            new_num = other.numy * self.numy
            new_denomy = other.denomy * self.denomy
            return Fraction(new_num, new_denomy)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            new_numy = other * self.denomy
            new_denomy = self.numy
            return Fraction(new_numy, new_denomy)
        else:
            new_num = other.denomy * self.numy
            new_denomy = other.numy * self.denomy
            return Fraction(new_num, new_denomy)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.numy += other * self.denomy
        else:
            if self.denomy == other.denomy:
                self.numy += other.numy
            else:
                self.numy = self.numy * other.denomy + other.numy * self.denomy
                self.denomy *= other.denomy
        self.numy, self.denomy = self.__nod((self.numy, self.denomy))
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            self.numy -= other * self.denomy
        else:
            if self.denomy == other.denomy:
                self.numy -= other.numy
            else:
                self.numy = self.numy * other.denomy - other.numy * self.denomy
                self.denomy *= other.denomy
        self.numy, self.denomy = self.__nod((self.numy, self.denomy))
        return self

    def __imul__(self, other):
        if isinstance(other, int):
            self.numy *= other
        else:
            self.numy *= other.numy
            self.denomy *= other.denomy
        self.numy, self.denomy = self.__nod((self.numy, self.denomy))
        return self

    def __itruediv__(self, other):
        if isinstance(other, int):
            self.denomy *= other
        else:
            self.numy *= other.denomy
            self.denomy *= other.numy
        self.numy, self.denomy = self.__nod((self.numy, self.denomy))
        return self

    def __gt__(self, other):
        if isinstance(other, int):
            if self.numy > other * self.denomy:
                return True
            return False
        else:
            if self.numy / self.denomy > other.numy / other.denomy:
                return True
            return False

    def __lt__(self, other):
        if isinstance(other, int):
            if self.numy < other * self.denomy:
                return True
            return False
        else:
            if self.numy / self.denomy < other.numy / other.denomy:
                return True
            return False

    def __ge__(self, other):
        if isinstance(other, int):
            if self.numy >= other * self.denomy:
                return True
            return False
        else:
            if self.numy / self.denomy >= other.numy / other.denomy:
                return True
            return False

    def __le__(self, other):
        if isinstance(other, int):
            if self.numy <= other * self.denomy:
                return True
            return False
        else:
            if self.numy / self.denomy <= other.numy / other.denomy:
                return True
            return False

    def __eq__(self, other):
        if isinstance(other, int):
            if self.numy == other * self.denomy:
                return True
            return False
        else:
            if self.numy / self.denomy == other.numy / other.denomy:
                return True
            return False

    def __ne__(self, other):
        if isinstance(other, int):
            if self.numy != other * self.denomy:
                return True
            return False
        else:
            if self.numy / self.denomy != other.numy / other.denomy:
                return True
            return False


a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (3 - a, 2 / b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)












