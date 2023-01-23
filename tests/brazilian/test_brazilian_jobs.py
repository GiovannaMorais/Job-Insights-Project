from src.pre_built.brazilian_jobs import read_brazilian_file

mock = {"title": "Pessoa Programadora", "salary": "3000", "type": "full time"}


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')

    for job in brazilian_jobs:
        assert mock.keys() == job.keys()
