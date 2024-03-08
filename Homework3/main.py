from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users: list) -> None:
    corrent_datetime = datetime.now()
    containers = []

    def SortWeekday(users: list) -> None:
        for user, date in users.items():
            date = datetime(year=corrent_datetime.year,
                            month=date.month, day=date.day)
            return date
    users.sort(key=SortWeekday)

    for user in users:
        name, birthday = user.popitem()
        birthday = datetime(year=corrent_datetime.year,
                            month=birthday.month, day=birthday.day)

        def containers_append() -> None:
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                containers.append('Monday' + ': ' + name)
            else:
                containers.append(birthday.strftime('%A') + ': ' + name)

        if corrent_datetime.weekday() == 0:
            if corrent_datetime - timedelta(days=3) < birthday <= corrent_datetime + timedelta(days=4):
                containers_append()

        elif corrent_datetime.weekday() == 5:
            if corrent_datetime - timedelta(days=1) < birthday <= corrent_datetime + timedelta(days=6):
                containers_append()

        elif corrent_datetime.weekday() == 6:
            if corrent_datetime - timedelta(days=1) < birthday <= corrent_datetime + timedelta(days=5):
                containers_append()

        else:
            if corrent_datetime <= birthday <= corrent_datetime + timedelta(days=7):
                containers_append()

    containers_ddict = defaultdict(list)
    for element in containers:
        e = element.split(': ')
        char = e[0]
        containers_ddict[char].append(e[1])

    for weekday in dict(containers_ddict):
        time_name_string = ''
        for name in dict(containers_ddict)[weekday]:
            time_name_string += name + ', '
        names = time_name_string.removesuffix(', ')

        print(f'{weekday}: {names}')


if __name__ == '__main__':

    users = [
        {'Luke': datetime(year=1990, month=datetime.now().month, day=datetime.now().day)},
        {'Mike': datetime(year=2000, month=4, day=22)},
        {'John': datetime(year=2002, month=4, day=23)},
        {'Dave': datetime(year=1991, month=4, day=24)},
        {'Jack': datetime(year=1995, month=4, day=25)},
        {'Max': datetime(year=1999, month=4, day=26)},
        {'Leon': datetime(year=1994, month=4, day=27)},
        {'Bogdan': datetime(year=2004, month=4, day=28)},
        {'Dima': datetime(year=1989, month=4, day=29)},
        {'Marck': datetime(year=1985, month=4, day=30)},
        {'Svatoslav': datetime(year=1980, month=6, day=1)},
        {'Vova': datetime(year=2004, month=4, day=30)},
        {'Kostya': datetime(year=2002, month=4, day=29)}
    ]

    get_birthdays_per_week(users)
    