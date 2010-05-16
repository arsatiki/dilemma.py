# encoding: utf-8
from __future__ import division

import sys
import itertools
import strategies
from collections import defaultdict
from operator import itemgetter

from strategies import COOPERATE, DEFECT


CONTESTANTS = {'titfortat': strategies.titfortat,
               'saint': strategies.always_cooperate,
               'demon': strategies.always_defect,
               'unforgiving10': strategies.unforgiving}

def build_scorer(temptation, reward, punishment, sucker):
    """
    build_scorer(T, R, P, S) -> tuple-indexed score dict
    
    >>> b = build_scorer(5, 3, 1, 0)
    >>> b[COOPERATE, DEFECT]
    (0, 5)
    >>> b[DEFECT, COOPERATE]
    (5, 0)
    >>> b[DEFECT, DEFECT]
    (1, 1)
    >>> b[COOPERATE, COOPERATE]
    (3, 3)
    """
    if temptation <= reward:
        raise ValueError("Temptation to defect must be greater than reward for cooperation")
    if reward <= punishment:
        message = "Reward for coperation must be greater than\npunishment for mutual defection"
        raise ValueError("")
    if punishment <= sucker:
        raise ValueError("Punishment for mutual defection must be greater than the sucker's penalty.")
    if not (2 * reward > temptation + sucker):
        raise ValueError("Cooperation not Pareto optimal")
    
    return {
        (COOPERATE, COOPERATE): (reward, reward),
        (COOPERATE, DEFECT): (sucker, temptation),
        (DEFECT, COOPERATE): (temptation, sucker),
        (DEFECT, DEFECT): (punishment, punishment)
    }


def iterate(rounds, f1, f2):
    r1, state1 = f1(None)
    r2, state2 = f2(None)
    yield r1, r2
    for k in range(rounds - 1):
        r1, state1 = f1(r2, state1)
        r2, state2 = f2(r1, state2)
        yield r1, r2

def tournament(contestants, rounds, scoring):
    scores = defaultdict(int)
    
    for p1, p2 in itertools.combinations(contestants, 2):
        f1, f2 = contestants[p1], contestants[p2]

        for reply1, reply2 in iterate(rounds, f1, f2):
            # Restrict to strategies that do not use the cost matrix.
            s1, s2 = scoring[reply1, reply2]
            scores[p1] += s1
            scores[p2] += s2
    
    return scores
    

def main():
    rounds = int(sys.argv[1])
    if len(sys.argv) >= 6:
        TRPS = map(int, sys.argv[2:6])
    else:
        TRPS = (0, -1, -5, -10)
    scoring = build_scorer(*TRPS)
    scores = tournament(CONTESTANTS, rounds, scoring)

    for p, s in sorted(scores.iteritems(), key=itemgetter(1), reverse=True):
        print "%16s: %.4f" % (p, s / rounds)
    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        import doctest
        doctest.testmod()
    else:
        main()