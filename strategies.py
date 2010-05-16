# encoding: utf-8

from decorators import simple

"""Strategy collection for the iterated prisoner's dilemma."""

COOPERATE = 'cooperate'
DEFECT = 'defect'

@simple
def titfortat(tat):
    """Returns the same answer given by the opponent during the previous
       iteration.
       >>> titfortat(None) == COOPERATE
       True
       >>> titfortat(COOPERATE) == COOPERATE
       True
       >>> titfortat(DEFECT) == DEFECT
       True
    """
    if tat is None:
        return COOPERATE
    return tat

@simple
def always_defect(prev):
    return DEFECT

@simple
def always_cooperate(prev):
    return COOPERATE


    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
