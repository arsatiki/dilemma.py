# encoding: utf-8
from __future__ import division

import sys
import itertools
import strategies
from collections import defaultdict

from strategies import COOPERATE, DEFECT


CONTESTANTS = {'titfortat': strategies.titfortat,
               'saint': strategies.always_cooperate,
               'demon': strategies.always_defect}

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
    if temptation < reward:
        raise ValueError("Temptation to defect must be greater than reward for cooperation")
    if reward < punishment:
        message = "Reward for coperation must be greater than\npunishment for mutual defection"
        raise ValueError("")
    if punishment < sucker:
        raise ValueError("Punishment for mutual defection must be greater than the sucker's penalty.")
    if not (2 * reward > temptation + sucker):
        raise ValueError("Cooperation not Pareto optimal")
    
    return {
        (COOPERATE, COOPERATE): (reward, reward),
        (COOPERATE, DEFECT): (sucker, temptation),
        (DEFECT, COOPERATE): (temptation, sucker),
        (DEFECT, DEFECT): (punishment, punishment)
    }


def tournament(contestants):
    """Returns an all against all sequence of player pairs.
    tournament
    """
    return itertools.combinations(contestants, 2)


def main():
    rounds = int(sys.argv[1])
    
    scoring = build_scorer(0, -1, -5, -10)
    scores = defaultdict(int)
    
    for p1, p2 in tournament(CONTESTANTS):
        f1, f2 = CONTESTANTS[p1], CONTESTANTS[p2]
        reply1, reply2 = f1(None), f2(None)
        for round in range(rounds - 1):
            s1, s2 = scoring[reply1, reply2]
            scores[p1] += s1
            scores[p2] += s2
            reply1, reply2 = f1(reply2), f2(reply1)
    
    for p in scores:
        print "%16s: %.4f" % (p, scores[p] / rounds)
            

if __name__ == '__main__':
    if len(sys.argv) == 1:
        import doctest
        doctest.testmod()
    else:
        main()