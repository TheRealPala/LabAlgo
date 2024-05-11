from time import perf_counter


def roundSeconds(seconds, decimals=3):
    return round(seconds, decimals)


def testFunction(function, args=None, decimals=2):
    start = perf_counter()
    if args is None:
        function()
    else:
        function(args)
    end = perf_counter()
    diff = end - start
    diff = f"{diff:.{decimals}E}"
    return diff
