

class Vector:

    def __init__(self, *elements):
        if len(elements) < 2:
            raise ValueError('At least two elements are required')
        self.elements = elements

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.elements, other.elements)])

    def __repr__(self):
        return str(list(self.elements))

    def __len__(self):
        return sum([1 for _ in self.elements])

    def __neg__(self):
        return [-val for val in self.elements]

    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError(f'A vector of size {len(self)} is expected')
        return [x + y for x, y in zip(self.elements, other.elements)]

    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError(f'A vector of size {len(self)} is expected')
        return [x - y for x, y in zip(self.elements, other.elements)]



class Range:

    def __init__(self, start_num, end_num, step=1):
        if step == 0:
            raise ValueError(f'\'step\' cannot be zero')
        self.start = start_num
        self.end = end_num
        self.step = step

    def __repr__(self):
        return f'Range object ({self.start}, {self.end}, {self.step})'

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.n >= self.end:
            raise StopIteration
        result = self.n
        self.n += self.step
        return result



"""
Problem 1.1

벡터는 최소 두 개 이상의 원소로 이루어진 값이다. 다음과 같이 생성할 수 있다.

Problem 1.2

이처럼 쉽게 인지할 수 있는 형식으로 출력하는 것이 여러모로 도움이 된다. 이렇게 나올 수 있도록 built-in 메소드를 오버라이드 해보자.

1.3
overwrite len 

2.4 
negation
"""

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
    print(vector1-vector2)

    rr = Range(1,2)
    print(rr)

    for x in Range(1,100,4):
        print(x)