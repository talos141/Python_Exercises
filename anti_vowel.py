v = ["o", "e", "a", "u","U", "A", "E", "O"]
nv = []

def anti_vowel(text):
    for c in text:
        if c not in v and c in text:
            nv.append(c)

    print("".join(nv))


anti_vowel("Hey look Words!")

# def anti_vowel(text):
#     t=""
#     for c in text:
#         for i in "ieaouIEAOU":
#             if c==i:
#                 c=""
#             else:
#                 c=c
#         t=t+c
#     return t