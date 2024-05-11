from time import perf_counter


def roundSeconds(seconds, decimals=3):
    return round(seconds, decimals)


def testFunction(function, args=None, decimals=3):
    start = perf_counter()
    if args is None:
        function()
    else:
        function(args)
    end = perf_counter()
    return roundSeconds(end - start, decimals)
