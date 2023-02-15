colors_values = {"black": "0", "brown": "1", "red": "2", "orange": "3", "yellow": "4",
                "green": "5", "blue": "6", "violet": "7", "grey": "8", "white": "9"}

metric_prefix = ["", "kilo", "mega", "giga", "tera"]


def label(colors):
    resp = str(int(colors_values[colors[0]] + colors_values[colors[1]]))
    resp += ("0" * int(colors_values[colors[2]]))
    count = 0
    while True:
        if resp[-3:] == "000":
            resp = resp[0:-3]
            count += 1
        else:
            return resp + " " + metric_prefix[count] + "ohms"

print(label(["yellow", "violet", "yellow"]))