

def indent(text):
    return '\n'.join(['    {0}'.format(l.strip()) for l in text.splitlines()])
