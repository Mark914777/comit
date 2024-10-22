def high_and_low(numbers):
    res = []
    max =int(str[0])
    min =int(str[0])
    for integer in str:
        if int(integer) > max:
          max = int(integer)
        if int(integer) < min:
            min = int(integer)
    res.append(max)
    res.append(min)
    return "".join(res)
