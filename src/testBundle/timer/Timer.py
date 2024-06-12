from time import perf_counter

from timeit import default_timer as timer
def roundSeconds(seconds, decimals=3):
    return round(seconds, decimals)


def testFunction(function, args=None, decimals=2):
    start = timer()
    ret = None
    if args is None:
        ret = function()
    else:
        ret = function(args)
    end = timer()
    diff = end - start
    # diff = f"{diff:.{decimals}E}"
    return {
        "time": diff,
        "retFunction": ret
    }
