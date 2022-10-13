
def commands(binary_str):
    actions = [False, "jump", "close your eyes", "double blink", "wink"]
    local = []
    for index, digit in enumerate(binary_str):
        if index == 0:
            if digit == "1":
                is_reverse = True
            else:
                is_reverse = False
            continue
        if digit == "1":
            local.append(actions[index])
    if is_reverse:
        return local
    return local[::-1]


x = commands("00011")
print(x)