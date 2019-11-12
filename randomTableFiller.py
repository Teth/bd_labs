import math
import random
import time
import names





cities = [
    'Greg',
    'Jolly',
    'Kellington',
    'Worrywert',
    'Hollywrap',
    'Olengor',
    'Stanviktor',
    'Opel'
]

teamname = [
    'Breakers',
    'Haters',
    'Makers',
    'Raptors',
    'Keepers',
    'Sweepers',
    'Incorporate',
    'Belters',
    'Jammers',
    'Loners',
    'Hornets',
    'Otters'
]


class RandomTeam:
    def __init__(self):
        pass

    @staticmethod
    def get_random():
        ST_DATE = '1-1-1980'
        END_DATE = '1-1-2010'
        city = random.choice(cities)
        name = random.choice(teamname)
        cr_date = random_date(ST_DATE, END_DATE)
        arr = {'name': "'{0}'".format(name),
               'city': "'{0}'".format(city),
               'cr_date': "'{0}'".format(cr_date)}
        print arr
        return arr


class RandomStadium:
    def __init__(self):
        pass

    @staticmethod
    def get_random():
        cap = (5 + math.floor(random.random() * 95)) * 1000
        phone = random.randint(999999999, 9999999999)
        address = random.choice(cities) + \
                  ' city, ' + names.get_full_name() + \
                  ' street, ' + random.randint(1, 100).__repr__()
        arr = {'capacity': cap.__repr__(),
               'address': "'{0}'".format(address),
               'phone_number': phone.__repr__()}
        return arr


class RandomGame:
    # score from 0 to 5
    # random date from 2017 to 2019

    def __init__(self):
        pass

    @staticmethod
    def get_random():
        MAX_SCORE = 5
        ST_DATE = '1-1-2017'
        END_DATE = '1-1-2020'

        score_a = math.floor(random.random() * MAX_SCORE)
        score_b = math.floor(random.random() * MAX_SCORE)
        date = random_date(ST_DATE, END_DATE)

        arr = {'score_a': score_a.__repr__(),
               'score_b': score_b.__repr__(),
               'match_date': "'{0}'".format(date)}
        return arr


class RandomPlayer:
    #
    #
    #
    #
    def __init__(self):
        pass

    @staticmethod
    def get_random():
        MIN_AGE = 18
        MAX_AGE = 40
        name = names.get_first_name()
        surname = names.get_last_name()
        age = MIN_AGE + math.floor(random.random() * (MAX_AGE - MIN_AGE))
        active = random.random() > 0.2
        phone = random.randint(999999999, 9999999999)
        arr = {'first_name': "'{0}'".format(name),
               'surname': "'{0}'".format(surname),
               'age': age.__repr__(),
               'is_active': active.__repr__(),
               'phone_number': "'{0}'".format(phone)}
        return arr


def random_date(start, end):
    _format = '%m-%d-%Y'
    stime = time.mktime(time.strptime(start, _format))
    etime = time.mktime(time.strptime(end, _format))

    delta = random.random() * (etime - stime)
    ptime = stime + math.floor(delta)
    return time.strftime(_format, time.localtime(ptime))
