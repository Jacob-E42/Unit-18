def validate_percentage(pct):
    """
    pct must be between 0 and 100 inclusive.

    >>> validate_percentage(50)
    50

    >>> validate_percentage(-1)
    Traceback (most recent call last):
        ...
    ValueError
    """
