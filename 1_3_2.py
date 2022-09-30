def pal(slovo):
    if slovo.replace(" ", "") == slovo[::-1].replace(" ", ""):
        print('true')
    else: print('no')

pal('black cat')