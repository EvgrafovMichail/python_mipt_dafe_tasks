def simplify_path(path: str) -> str:
    result = []
    parts = path.split('/')
    for part in parts:
        if part == '.' or part == '':
            continue
        elif part == '..':
            if result:
                result.pop()
            else:
                return ""
        else:
            result.append(part)
    return '/'+'/'.join(result)
print(simplify_path('/home/user/./Documents/../Pictures'))