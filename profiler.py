"""
https://github.com/rkern/line_profiler
pip install line_profiler

Line #:
    The line number in the file.
Hits:
    The number of times that line was executed.
Time:
    The total amount of time spent executing the line in the timer's units.
    In the header information before the tables, you will see a line
    "Timer unit:" giving the conversion factor to seconds.
    It may be different on different systems.
Per Hit:
    The average amount of time spent executing the line once in the timer's units.
% Time:
    The percentage of time spent on that line relative to the total amount of
    recorded time spent in the function.
Line Contents:
    The actual source code. Note that this is always read from disk when the formatted
    results are viewed, not when the code was executed. If you have edited the file in
    the meantime, the lines will not match up, and the formatter may not even be able
    to locate the function for display.

Eg.
from base.profiler import profile

@profile(follow=[get_auth_data])
def func(self, arg1):
    auth = self.get_auth_data()
    return 'stuff'
"""

try:
    from line_profiler import LineProfiler

    def profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

except ImportError:
    def profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner

if __name__ == '__main__':
    pass