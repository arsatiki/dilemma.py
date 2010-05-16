# encoding: utf-8

from decorators import simple

"""Strategy collection for the iterated prisoner's dilemma.
The arguments for a strategy are the opponent's last reply and
a state object. The strategy returns a reply and a new state object.

If the strategy does not make use of the state, it can use the simple
decorator. Simple strategies take in the last reply and return their new one."
"""

COOPERATE = 'cooperate'
DEFECT = 'defect'

always_defect = simple(lambda prev: DEFECT)
always_cooperate = simple(lambda prev: COOPERATE)

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

def unforgiving(prev, defect_counter=0):
    """Start out trusting, but if other defects, punish for 10 turns"""
    if defect_counter:
        return DEFECT, defect_counter - 1
    
    if prev == DEFECT:
        return DEFECT, 10
    
    return COOPERATE, 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
