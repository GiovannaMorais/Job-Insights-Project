from src.pre_built.counter import count_ocurrences

path = 'data/jobs.csv'


def test_counter():
    assert(count_ocurrences(path, "location") == 1350)
    assert(count_ocurrences(path, "salary") == 598)
