def simplify_path(path: str) -> str:
    parts = path.split('/')
    right_path = []
    for part in parts:
        if part != '' and part != '.' and part != '..':
            right_path.append(part)
        elif part == '..':
            if len(right_path)>0:
                right_path.pop()
            else:
                return ""
            
    path = '/' 
    path += '/'.join(right_path)
    
    if path == '':
        return "/"
    return path
