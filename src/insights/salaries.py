from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    reader = read(path)
    salaries = []
    for salary in reader:
        if salary['max_salary'].isdigit() and salary['max_salary'] != "":
            item = salary['max_salary']
            salaries.append(int(item))
    return max(salaries)


def get_min_salary(path: str) -> int:
    reader = read(path)
    salaries = []
    for salary in reader:
        if salary['min_salary'].isdigit() and salary['min_salary'] != "":
            item = salary['min_salary']
            salaries.append(int(item))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (ValueError, TypeError, KeyError):
        raise ValueError

    if min_salary > max_salary:
        raise ValueError

    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list
