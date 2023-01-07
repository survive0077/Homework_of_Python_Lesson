from pythonds.basic import Stack


def htmlchecker(htmllist):
    s = Stack()
    balanced = True
    index = 0
    while index < len(htmllist) and balanced:
        symbol = htmllist[index]
        if symbol in ["<html>", "<head>", "<title>", "<body>", "<h1>"]:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            elif symbol in ["</html>", "</head>", "</title>", "</body>", "</h1>"]:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = ["<html>", "<head>", "<title>", "<body>", "<h1>"]
    closers = ["</html>", "</head>", "</title>", "</body>", "</h1>"]
    return opens.index(open) == closers.index(close)


print(htmlchecker(["<html>", "<head>", "<title>", "Example", "</title>", "</head>", "<body>", "<h1>"\
                      , "Hello, world", "</h1>", "</body>", "</html>"]))
