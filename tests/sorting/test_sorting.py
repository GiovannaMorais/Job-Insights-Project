from src.pre_built.sorting import sort_by


mock = [
    {"min_salary": 1000, "max_salary": 3000},
    {"min_salary": 4000, "max_salary": 8000},
    {"min_salary": 10000, "max_salary": 16000},
]

order_min_salary = [
    {"min_salary": 1000, "max_salary": 3000},
    {"min_salary": 4000, "max_salary": 8000},
    {"min_salary": 10000, "max_salary": 16000},
]

order_max_salary = [
    {"min_salary": 10000, "max_salary": 16000},
    {"min_salary": 4000, "max_salary": 8000},
    {"min_salary": 1000, "max_salary": 3000},
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == order_min_salary

    sort_by(mock, "max_salary")
    assert mock == order_max_salary
