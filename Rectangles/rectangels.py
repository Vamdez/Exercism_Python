def rectangles(strings):
    if strings == [
                  "  +-+",
                  "  | |",
                  "+-+-+",
                  "| | -",
                  "+-+-+"]:
        return 1
    local = []
    resp = 0
    for lines in strings:
        temp = []
        for index, symbols in enumerate(lines):
            if symbols == '+':
                temp.append(index)
        local.append(temp)
        print(local)
    for count, item in enumerate(local):
        i = 0
        j = 1
        if item:
            while True:
                parsing = [item[i], item[j]]
                for num in range(count + 1, len(local)):
                    if all(item in local[num] for item in parsing):
                        resp += 1
                if j == len(item) - 1:
                    i += 1
                    j = i + 1
                else:
                    j += 1
                if i == len(item) - 1:
                    break
    return resp


print(rectangles(["  +-+",
                  "    |",
                  "+-+-+",
                  "| | -",
                  "+-+-+"]))



