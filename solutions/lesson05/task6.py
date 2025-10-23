def simplify_path(path: str) -> str:
    
    elem = path.split('/')
    st = []
    
    for el in elem:
        if el == '' or el == '.':
            continue
        elif el == '..':
            if st:  
                st.pop()
            else:
                return ""
        else:
            st.append(el)
    
    return '/' + '/'.join(st)
    