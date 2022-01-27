#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    cnt = 0
    str_cp = ""
    for compound in str:
        if cnt == n:
            cnt += 1
            continue
        str_cp += str[cnt]
        cnt += 1
    return str_cp
