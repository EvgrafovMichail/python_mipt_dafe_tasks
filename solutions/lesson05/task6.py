def simplify_path(path: str) -> str:
    level = 0

    res = []

    path.replace("//", "/")

    tokens = path.split("/")

    for i in range(len(tokens)):
        token = tokens[i]

        if token == "..":
            level -= 1

            if level < 0:
                return ""

            if res:
                res.pop()

        elif token == "." or token == "":
            continue

        else:
            level += 1
            res.append(token)

    return "/" + "/".join(res)


print(simplify_path("/home/user/./Documents/../Pictures"))
