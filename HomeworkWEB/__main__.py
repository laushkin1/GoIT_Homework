from Bot import Bot
from AddressBook import Formator

class HelpsFormator(Formator):
    def output_info(self):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))

help_command = HelpsFormator()

if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('>>> ').strip().lower()
        if action == 'help':
            help_command.output_info()
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
