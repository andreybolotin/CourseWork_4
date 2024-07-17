import pytest

from src.Vacancy import Vacancy
from src.user_interactive import UserInteractive


@pytest.fixture
def test():
    test = UserInteractive("name")
    test_list = [Vacancy(f"testname {i}", f"testarea {i}", salary=i * 1000) for i in range(10)]
    test.vacancies_list = test_list
    return test


def test_get_top_n_for_salary(test):
    assert UserInteractive.get_top_n_for_salary(test, 0) == []


def test_get_top_n_for_salary_2(test):
    assert len(UserInteractive.get_top_n_for_salary(test, 5)) == 5


def test_get_top_n_for_salary_3(test):
    assert UserInteractive.get_top_n_for_salary(test, 1)[0].salary == 9000
