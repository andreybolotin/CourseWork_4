class Vacancy:
    def __init__(self, name, area, salary, experience, currency):  # url, snippet):
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary
        self.experience = experience
        self.currency = currency

    # elf.url = url
    # self.snippet = snippet

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else 'Не указана'}\n"
                f"Валюта: {self.currency if self.currency else 'Не указана'}\n"
                f"Опыт работы: {self.experience if self.experience else 'Не указан'}"
                )

    def __lt__(self, other):
        if not self.salary:
            return "Зарплата не указана"
        elif not other.salary:
            return False
        elif self.salary or not other.salary:
            return True
        else:
            return False

    @staticmethod
    def __validation_data(data):
        if data:
            return data
        else:
            return "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = vacancy.get("salary").get("from")
                currency = vacancy.get("salary").get("currency")
            else:
                salary = 0
                currency = " "
        else:
            salary = 0
            currency = " "

        if vacancy.get("experience"):
            if vacancy.get("experience").get("name"):
                experience = vacancy.get("experience").get("name")
            else:
                experience = 0
        else:
            experience = 0

        return cls(name, area, salary, experience, currency)
