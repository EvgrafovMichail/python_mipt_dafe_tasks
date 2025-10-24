def simplify_path(path: str) -> str:
    lst = path.split('/')
    way = []

    for element in lst:
        if element == '' or element == '.':
            continue
        elif element == '..':
            if len(way) != 0:
                way.pop()
            else:
                return ''
        else:
            way.append(element)

    result = '/' + '/'.join(way)

    return result