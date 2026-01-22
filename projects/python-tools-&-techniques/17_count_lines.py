def count_lines(path):
    """
    Count number of lines in a file.

    >>> import tempfile
    >>> f = tempfile.NamedTemporaryFile(mode="w+", delete=False)
    >>> _ = f.write("a\\nb\\nc\\n")
    >>> f.close()
    >>> count_lines(f.name)
    3
    """
