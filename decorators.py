# encoding: utf-8

def simple(f):
    """Simple strategies make their choice based only on the previous
    reply from the opponent.
    
    >>> f = simple(lambda x: 1)
    >>> f(None)
    (1, None)
    >>> f(None, None)
    (1, None)
    """
    def wrapped(last_reply, state=None):
        return f(last_reply), None
    return wrapped

if __name__ == '__main__':
    import doctest
    doctest.testmod()