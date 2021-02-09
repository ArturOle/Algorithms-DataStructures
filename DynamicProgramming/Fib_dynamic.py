import cProfile
import pstats


#  Traditional Fibonacci  #
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


#  Dynamic Fibonacci - memoization #
memo = {1: 1, 2: 1}


def fib_dynamic(n):
    if n not in memo.keys():
        memo[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)

    return memo[n]


if __name__ == "__main__":
    n_in = 40

    #  Profiling traditional Fibonacci  #
    profiler = cProfile.Profile()
    profiler.enable()
    fib_test = fib(n_in)
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()
    print(fib_test)

    #  Profiling dynamic Fibonacci  #
    profiler = cProfile.Profile()
    profiler.enable()
    fib_dynamic_test = fib_dynamic(n_in)
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()
    print(fib_dynamic_test)
