def unzip(compress_text: str) -> str:
    answer = ""
    for i in compress_text.split():
        if i.rfind("*") != -1 and i[i.rfind("*") + 1 :].isdigit():
            for _ in range(int(i[i.rfind("*") + 1 :])):
                answer += i[: i.rfind("*")]
        else:
            answer += i
    return answer
