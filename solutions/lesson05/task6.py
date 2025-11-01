def simplify_path(path: str) -> str:
    components = path.split('/')
    stuff = []
    
    for comp in components:
        if comp == '' or comp == '.':
            continue
        elif comp == '..':
            if stuff != []:
                stuff.pop()
            else:
                return ""
        else:
            stuff.append(comp)

    path = "/"
    for i in range(len(stuff)):
        path = path + stuff[i] + '/'

    if stuff == []:
        return '/'
    return path[:-1]

