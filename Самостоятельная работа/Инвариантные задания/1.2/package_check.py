from guestbookpackage import GuestBook


guest_book = GuestBook()
guest_book.add_guest("Venom", "Dreadful", "venom@space.com")
guest_book.add_guest("Harold", "Great", "Harold@gmail.com")
guest_book.remove_guest("Harold@gmail.com")
guest_book.full_remove_guest("Ribo@gmail.com")
guest_book.rename_guest("Harold@gmail.com","REY12","Scalator")
guest_book.write_file()
guest_book.file_cleanup()
