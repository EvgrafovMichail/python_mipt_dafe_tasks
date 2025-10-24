def simplify_path(path: str) -> str:
    directories = path.split("/")
    ans = ""
    lst = []
    i = 0
    for i in directories:
        if i == "." or i == "":
            continue
        elif i == "..":
            if lst:
                lst.pop()
            else:
                return ""
        else:
            lst.append(i)

    if lst:
        ans = "/" + "/".join(lst)
    else:
        ans = "/"

    return ans


print(simplify_path("/home/user/./Documents/../Pictures"))
