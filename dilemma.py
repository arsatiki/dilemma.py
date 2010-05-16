# encoding: utf-8
import sys
import itertools

def tournament(contestants):
    """Returns an all against all sequence of player pairs.
    tournament
    """
    return itertools.combinations(contestants, 2)


def main():
    pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        import doctest
        doctest.testmod()
    else:
        main()