import datetime


def add(moment):
    delta1 = datetime.timedelta(seconds=10 ** 9)
    return delta1 + moment


add(datetime.datetime(2011, 4, 25, 0, 0))
