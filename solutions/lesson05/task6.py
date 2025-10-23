def simplify_path(path: str) -> str:
    if path.find("/../",0, 4)!= -1:
        return ""
    while path.find("/./")!=-1:
        path = path.replace("/./", "/") 
    while path.find("//")!=-1:
        path = path.replace("//", "/")  
    while path.find("/../")!=-1:
            if len(path)==4:
                 return ""
            r_index=path.index("/../")
            l_index=path.rindex("/",0, r_index-1)
            path = path[:l_index]+path[r_index+3:] 


    if path[-3:] =="/..":
        if len(path)==3:
            return ""
        r_index=path.index("/..")
        l_index=path.rindex("/",0, r_index-1)
        path = path[:l_index]+path[r_index+3:] 
    if path[-2:] =="/." and len(path)==2:
         return "/"
    if path[-1] =="/" and len(path)>1:
         path= path[:-1]          
    return path 