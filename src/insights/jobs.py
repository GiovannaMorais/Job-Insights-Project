from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode='r') as file:
        jobs_reader = csv.DictReader(file)
        jobs_list = []
        for job in jobs_reader:
            jobs_list.append(job)
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_reader = read(path)
    unique_job_type = set()
    for job in jobs_reader:
        unique_job_type.add(job['job_type'])
    return unique_job_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_types = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_types.append(job)
    return jobs_types
