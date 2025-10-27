def simplify_path(path: str) -> str:
    new_text=[]
    path=path.split("/")
    text=""
    for i in range(len(path)):
        if path[i]=="." or  path[i]=="":
            continue   
        elif path[i]=="..":
            if new_text:
                new_text=new_text[:-1]
            else:
                return ""
        else:
            new_text.append(path[i])
    if not(new_text):
        return "/"
    for i in new_text:
        text=text+"/"+i
    return text