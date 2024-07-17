from src.Json_worker import WorkWithJson
from src.Parser import HH


class UserInteractive(WorkWithJson):
    def __init__(self, user_name):
        """
        Здесь добавлять логику взаимодействия с пользователем и получением списка вакансий
        """
        super().__init__()
        self.user_name = user_name
        self.vacancies_list = self.read_file()
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_top_n_for_salary(self, n):
        """
        Здесь добавлять логику получения топ N вакансий с самой высокой зарплатой
        """
        sort_by_salary = list(sorted(self.vacancies_list, key=lambda x: x.salary, reverse=True))
        return sort_by_salary[:n]

    def get_vacancy_from_keyword(self):
        """
        Здесь добавлять логику получения вакансии по ключевому слову
        """
        keyword = input("Введите ключевое слово для поиска: ")
        res = []
        for vacancy in self.vacancies_list:
            if keyword.lower() in vacancy.name.lower():
                res.append(vacancy)

        return res
