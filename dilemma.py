# encoding: utf-8
from __future__ import division

import sys
import strategies
from operator import itemgetter


from tournament import build_scorer, iterate, run_tournament

CONTESTANTS = {'titfortat': strategies.titfortat,
               'saint': strategies.always_cooperate,
               'demon': strategies.always_defect,
               'unforgiving3': strategies.unforgiving(3),
               'unforgiving10': strategies.unforgiving(10),
               'unforgiving100': strategies.unforgiving(100),
               'random': strategies.randomized}
    

def main():
    rounds = int(sys.argv[1])
    if len(sys.argv) >= 6:
        TRPS = map(int, sys.argv[2:6])
    else:
        TRPS = (0, -1, -5, -10)
    scoring = build_scorer(*TRPS)
    scores = run_tournament(CONTESTANTS, rounds, scoring)

    for p, s in sorted(scores.iteritems(), key=itemgetter(1), reverse=True):
        print "%16s: %.4f" % (p, s / rounds)
    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        import doctest
        doctest.testmod()
    else:
        main()