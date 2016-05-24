try:
    # Python 3
    from urllib.parse import quote_plus
except ImportError:
    # Python 2
    from urllib import quote_plus
