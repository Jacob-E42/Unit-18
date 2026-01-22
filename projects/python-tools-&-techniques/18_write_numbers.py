def write_numbers(path, n):
    """
    Write numbers 1..n each on its own line.

    >>> import tempfile
    >>> f = tempfile.NamedTemporaryFile(delete=False)
    >>> write_numbers(f.name, 3)
    >>> open(f.name).read()
    '1\\n2\\n3\\n'
    """
