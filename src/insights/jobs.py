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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
