class GuestBook:
    """Класс с методами, позволяющими взаимодействовать с JSON-файлом"""
    book: list

    def __init__(self):
        self.book = list()

    def add_guest(self, name: str, surname: str, email: str, status: str = "in processing"):
        """Добавление нового гостя"""
        self.book.append({"guest_name": name,
                          "guest_surname": surname,
                          "email": email,
                          "status": status})

    def full_remove_guest(self, email: str):
        """Полное удаление гостя из книги"""
        for guest in self.book:
            if dict(guest).get("email") == email:
                self.book.remove(guest)

    def remove_guest(self, email: str):
        """Изменение статуса гостя на "удалён" """
        for guest in self.book:
            if guest.get("email") == email:
                guest["status"] = "Guest deleted"

    def rename_guest(self, email: str, new_name: str, new_surname: str):
        """Изменение имени и фамилии гостя"""
        for guest in self.book:
            if guest.get("email") == email:
                guest["guest_name"] = new_name
                guest["guest_surname"] = new_surname

    def write_file(self):
        """Сериализация списка на форматированную строку JSON и запись в файл"""
        with open("./book.json", 'w') as file:
            import json
            self.book = {"Book": self.book}
            file.write(json.dumps(self.book, indent=4))

    def file_cleanup(self):
        """Очистка файла"""
        f = open("./book.json", 'w')
        f.close()


if __name__ == "__main__":
    guest_book = GuestBook()
    guest_book.add_guest("Venom", "Dreadful", "venom@space.com")
    guest_book.add_guest("Harold", "Great", "Harold@gmail.com")
    guest_book.remove_guest("Harold@gmail.com")
    guest_book.full_remove_guest("Ribo@gmail.com")
    guest_book.rename_guest("Harold@gmail.com","REY12","Scalator")
    guest_book.write_file()
    guest_book.file_cleanup()
