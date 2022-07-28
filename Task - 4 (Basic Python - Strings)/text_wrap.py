# text_wrap
def wrap(string, max_width):
    n = textwrap.TextWrapper(width = max_width)
    word = n.fill(text = string)
    return word