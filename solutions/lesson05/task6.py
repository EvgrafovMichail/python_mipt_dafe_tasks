def simplify_path(path: str) -> str:
    catalogs = path.split('/')
    simplify = []
        
    for catalog in catalogs:
        match catalog:
            case '..':
                if not simplify:
                   return ''
                simplify.pop()
                continue    
                       
            case '.' | '':
                continue
            case _:
                simplify.append(catalog)
        
    return '/' + '/'.join(simplify)

#print(simplify_path(input()))


