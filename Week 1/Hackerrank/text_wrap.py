def wrap(string, max_width):
    lst = []
    lst = textwrap.wrap(string, max_width)
    print(*lst, sep = "\n")
    return textwrap.fill(lst,max_width)