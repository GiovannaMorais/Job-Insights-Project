from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    reader = read(path)
    unique_industries = set()
    for job in reader:
        if job['industry'] != '':
            unique_industries.add(job['industry'])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_types = []
    for job in jobs:
        if job['industry'] == industry:
            industry_types.append(job)
    return industry_types
