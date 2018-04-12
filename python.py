class A:
    def __init__(self, a, b, c):
        pass


OBJS = {}
OBJS['a'] = A


def test(a, b, c):
    pass


def main():
    test(
        a=3,
        b=4,
        c=5,
    )

    OBJS['a'](
        a=1,
        b=2,
        c=3,
    )

    o = OBJS['a']
    o(
        a=1,
        b=2,
        c=3,
    )
