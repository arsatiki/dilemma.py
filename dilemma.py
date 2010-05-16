# encoding: utf-8
import sys

def main():
    pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        import doctest
        doctest.testmod()
    else:
        main()