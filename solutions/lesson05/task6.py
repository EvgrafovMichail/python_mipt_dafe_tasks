def simplify_path(path: str) -> str:

    path1 = path.split('/')

    if path1[0] == '':
        path1 = path1[1:]

    if path1[0] == '..':
        return ''

    k = len(path1)-1
    i = -1
    while k >= 0:
        i+=1
        if path1[0] == '..':
            return ''
        if path1[i] == '.':
            del path1[i]
            i -= 1
        elif path1[i] == '':
            del path1[i]
            i -= 1
        elif path1[i] == '..':
            del path1[i]
            del path1[i-1]
            i -= 2
        k -= 1

    path = '/'
    for i in range(len(path1)):

        path += path1[i]
        path += '/'
    if path[-1] == '/' and len(path) > 1:
        return path[:-1]
    return path
