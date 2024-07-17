from src.Vacancy import Vacancy
from src.user_interactive import UserInteractive

if __name__ == '__main__':

    user_name = input("Как вас зовут?: ")
    user = UserInteractive(user_name)
    print()
    keyword = input("Введите поисковый запрос: ")

    n = int(input("Введите количество вакансий для вывода в топ N: "))
    user.get_top_n_for_salary(n)
    print()
    for vacancy in user.get_vacancies_list(keyword):
        vac = Vacancy.new_vacancy(vacancy)
        print(vac)
        print()
        user.vacancies_list.append(vac)

    for vacancy in user.get_vacancy_from_keyword():
        print()
        print(vacancy)
        print()
