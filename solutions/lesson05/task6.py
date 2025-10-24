def simplify_path(path: str) -> str:
    ans = []
    i = 0
    path = path.split("/")
    for i in path:
        if i == "." or i == "":
            continue
        if i == "..":
            if len(ans):
                ans.pop()
            else:
                return ""
        else:
            ans.append(i)
    return "/" + "/".join(ans)
