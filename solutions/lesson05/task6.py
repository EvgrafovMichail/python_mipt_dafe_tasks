def simplify_path(path: str) -> str:
    ans = ""
    part = ""
    above_root = False

    for i in path:
        if i == "/":
            if part == "..":
                if ans != "":
                    for j in range(len(ans) - 1, 0, -1):
                        if ans[j] == "/":
                            ans = ans[:j]
                            break
                    else:
                        ans = ""
                else:
                    above_root = True
                    break
            elif part != "" and part != ".":
                ans += "/" + part
            part = ""
        else:
            part += i

    if not (above_root) and part:
        if part == "..":
            if ans != "":
                for j in range(len(ans) - 1, 0, -1):
                    if ans[j] == "/":
                        ans = ans[:j]
                        break
                else:
                    ans = ""
            else:
                above_root = True
        elif part != ".":
            ans += "/" + part

    if above_root:
        return ""
    if ans == "":
        return "/"
    return ans
