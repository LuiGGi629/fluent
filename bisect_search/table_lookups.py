import bisect


def grade(score, breakpoints=None, grades=None) -> str:
    """
    Function that convert test scores to letter grades
    """
    if breakpoints is None:
        breakpoints = [60, 70, 80, 90]

    if grades is None:
        grades = 'FDCBA'

    i = bisect.bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
