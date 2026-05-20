# Implements binary addition per Figure 2–42
def binadd(x,y):
    state = '0'
    pairs = list(zip(x,y))      # combine strings pairwise
    result = ''
    for pair in reversed(pairs):
        if state == '0':
            if pair in [('1','0'), ('0','1')]:
                result += '1'
            else:
                result += '0'
                if pair==('1','1'):
                    state = '1'
        else:   # state == '1'
            if pair in [('1','0'), ('0','1')]:
                result += '0'
            else:
                result += '1'
                if pair==('0','0'):
                    state = '0'
    if state == '1':
        result += '1'           # append carry
    return result[::-1]         # reverse result

print(binadd('1101','0110'))    # 10011
