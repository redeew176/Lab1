import doctest

class HeadPhones:
    """
        Документация на класс.
        Класс описывает модель наушников.
        """
    def __init__(self, model:str, charge:int):
         """ Инициализация экземпляра класса.
        :param model: Модель наушников
        :param charge: кол-во процентов заряда кейса
        """
      ...
        if not isinstance(model, str):
                raise TypeError("Название модели должно быть типа str")
        if not isinstance(charge, int):
                raise TypeError("Количество зарядки должно быть типа int")
        if 0 > charge > 100:
                raise ValueError("Количество зарядки положительно и меньше 100%")

    def get_out_of_case(self,number:int)->None:
         """
         Метод достает из кейса нужное количество наушников
         :param number: сколько наушников нужно достать из кейса

         Пример:
         >>> headphones_1 = HeadPhones('airpods',20)
         >>> headphones_1.get_out_of_case(1)

         """
      ...
        if 0 > number > 2:
            raise ValueError("В кейсе только 2 наушника")

    def charge_until_number_of_percent(self, number_of_percent:int)->None:
        """
                 Метод заряжает кейс до определенного количества процентов
                 :param number_of_percent: до какого количества процентов зарядить наушники

                 """
      ...
        if number_of_percent > 100:
            raise ValueError("Максимальный заряд 100%")

if __name__ == "__main__":
    doctest.testmod()
    pass


class VkPage:
    """
            Документация на класс.
            Класс описывает модель Странички в ВК.
            """
    def __init__(self, name:str, frens:int):
        """ Инициализация экземпляра класса.
        :param name: Имя пользователя
        :param frens: кол-во друзей
        """
        ...

          if not isinstance(name, str):
                 raise TypeError("Имя должно быть типа str")
          if not isinstance(frens, int):
                 raise TypeError("Количество друзией должно быть типа int")
          if frens < 0:
              raise ValueError("Количество друзией должно быть положительным")

    def change_name(self,new_name:str)->None:
        """
        Метод изменяет имя пользователя
        :param new_name: Новое имя пользователя

        """
        ...
          if not isinstance(new_name, str):
                 raise TypeError("Новое имя должно быть типа str")

    def remove_frens(self,numbers:int)->None:
        """" Метод удаляет определенное количество друзей(неважно каких)

              :param numbers:Количество удаляемых друзей
              Пример:
              >>>my_page = VkPage("Савин Дима", 666)
              >>>my_page.remove_frens(665)
              """

        ...
          if not isinstance(numbers, int):
                  raise TypeError("Количество удаляемых друзей должно быть типа int")
          if numbers > self.frens:
                  raise ValueError("Количество удаляемых друзей превосходит количество имеющихся")

if __name__ == "__main__":
    doctest.testmod()
    pass

class Note:
    """
                Документация на класс.
                Класс описывает модель Дневника.
                """
    def __init__(self,pages:int,color:str):
        """ Инициализация экземпляра класса.
        :param pages: кол-во страниц
        :param color: цвет дневника
        """
        ...
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным")

    def make_note(self,page:int,note:str)->None:
        """
                Метод делает запись на определенной странице
                :param page: Номер страницы для записи
                :param note: Сама запись
                Пример:
                >>> my_note = Note(150,"красный")
                >>> my_note.make_note(1,"Дорогой дневник,...")
                """
        ...
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть типа int")
        if not isinstance(note, str):
            raise TypeError("Запись должна быть типа str")

    def change_color(self,new_color)->None:
        """"
             Метод изменяет цвет дневника
             :param new_color: Новый цвет дневника
               """
        ...
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть типа str")


if __name__ == "__main__":
    doctest.testmod()
    pass
