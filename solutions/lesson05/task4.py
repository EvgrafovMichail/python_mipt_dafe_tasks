def unzip(compress_text: str) -> str:
    a = compress_text.split()
    answer = ""
    for i in a:
        if i.rfind("*") != -1:
            if i.rfind("*") == len(i) - 1:
                answer += i
                continue
            if i[i.rfind("*") + 1 :].isdigit():
                for _ in range(int(i[i.rfind("*") + 1 :])):
                    answer += i[: i.rfind("*")]
                continue
            else:
                answer += i
                continue
        answer += i
    return answer
