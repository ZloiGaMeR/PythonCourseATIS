def gen_dict(offset=1, reverse_encryption=False):
    abc = "abcdefghijklmnopqrstuvwxyz"
    out_dict = {}
    for letter in abc:
        if reverse_encryption:
            out_dict[abc[offset % 26]] = letter
        else:
            out_dict[letter] = abc[offset % 26]
        offset += 1
    return out_dict


def coding(in_dict, in_str):
    out_str = []
    tmp = ""
    for word in in_str:
        for letter in word:
            tmp += in_dict.get(letter)
        out_str.append(tmp)
        tmp = ""
    return out_str
