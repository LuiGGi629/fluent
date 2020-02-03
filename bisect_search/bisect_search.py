import bisect
import fire

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn=None) -> None:
    """
    Function that does a binary search for needle in haystack--which must be a sorted sequence--to locate the position
    where needle can be inserted while maintaining haystack in ascending order.
    e.g., usage: PYTHONPATH=. python3 bisect_search/bisect_search.py --bisect_fn=left
    """
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))

    if bisect_fn is None:
        bisect_fn = bisect.bisect
    else:
        bisect_fn = bisect.bisect_left

    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

    print(f'DEMO: {bisect_fn.__name__}')


if __name__ == '__main__':
    fire.Fire(demo)
