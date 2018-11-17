from numbers import Number

class Vector:

    def __init__(self, *elements):
        if len(elements) < 2:
            raise ValueError('At least two elements are required')
        # if not all([isinstance(x, Number) for x in elements]):
        #     return NotImplemented
        self.elements = elements

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.elements, other.elements)])

    def __repr__(self):
        return '[' + ', '.join([str(x) for x in self.elements]) + ']'

    def __len__(self):
        return sum([1 for _ in self.elements])

    def __neg__(self):
        return Vector(*[-val for val in self.elements])

    def __add__(self, other):
        self._ventor_len_check(other)
        return Vector(*[x + y for x, y in zip(self.elements, other.elements)])

    def __sub__(self, other):
        self._ventor_len_check(other)
        return Vector(*[x - y for x, y in zip(self.elements, other.elements)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._ventor_len_check(other)
            return sum([x * y for x, y in zip(self.elements, other.elements)])
        return Vector(*[other * x for x in self.elements])

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Vector(*[x / other for x in self.elements])
        raise TypeError("unsupported operand type(s) for /: 'Vector' and 'Vector'")

    def __floordiv__(self, other):
        if isinstance(other, Number):
            return Vector(*[x // other for x in self.elements])
        raise TypeError("unsupported operand type(s) for //: 'Vector' and 'int'")

    def _ventor_len_check(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError(f'A vector of size {len(self)} is expected')

class Range:

    def __init__(self, start_num, end_num, step=1):
        if step == 0:
            raise ValueError(f'\'step\' cannot be zero')
        self.start = start_num
        self.end = end_num
        self.step = step

    def __repr__(self):
        return f'Range ({self.start}, {self.end}, {self.step})'

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.n >= self.end) or (self.step < 0 and self.n <= self.end):
            raise StopIteration
        result = self.n
        self.n += self.step
        return result

    def __reversed__(self):
        return iter(list(Range(self.start,self.end,self.step))[::-1])



if __name__ == '__main__':
    vector1 = Vector(1, 2, 3, 4)
    vector2 = Vector(1,2,2,3)
    vector3 = Vector(1,2,2)
    print(
        vector1 == vector2
        )

    print(vector1)
    print(len(vector1))
    print(-vector1)
    print(vector1+vector2)
    # print(vector1+vector3)
    print(vector1 * vector2/8)
    print(vector2 * vector1)
    v = Vector(1, -2, 3)
    print(-v)
    s = Vector('a', 'b', 'c')
    print(str(s), '[a, b, c]')
    # rr = Range(1,2)
    # print(rr)
    #
    # # for x in Range(-10,20,100):
    # #     print(x)
    #
    # for x in reversed(Range(-10,20,100)):
    #     print(x)