import json
import random
import datetime


db_list = list()

COUNTRYES = 10
MANUFACTURES = 50
CARS = 100
REVIEWS = 300


def random_date(start='2022-01-01', end='2022-03-31') -> str:  #  '2019-12-04'
    d1 = datetime.datetime.fromisoformat(start)
    d2 = datetime.datetime.fromisoformat(end)
    delta = d2 - d1
    int_delta = delta.days - 1
    random_day = random.randrange(int_delta)
    random_datetime = d1 + datetime.timedelta(days=random_day)
    rnd_date = random_datetime.date()
    #return random_datetime.isoformat(sep=' ')
    return rnd_date.isoformat()


def country(stop, start=1):
    for pk in range(start, stop + 1):
        db_line = {
            "model": "app_car_reviews.country",
            "pk": pk,
            "fields": {
                "name": f'Country_{str(pk)}'
            }
        }
        db_list.append(db_line)


def manufacturer(stop, start=1):
    for pk in range(start, stop + 1):
        db_line = {
            "model": "app_car_reviews.manufacturer",
            "pk": pk,
            "fields": {
                "name": f'Manufacture_{str(pk)}',
                "country": random.randint(1, COUNTRYES)
            }
        }
        db_list.append(db_line)


def car(stop, start=1):
    for pk in range(start, stop + 1):
        db_line = {
            "model": "app_car_reviews.car",
            "pk": pk,
            "fields": {
                "name": f'Car_{str(pk)}',
                "manufacturer": random.randint(1, MANUFACTURES),
                "release_year": random.randint(1990, 2000),
                "end_year": random.randint(2001, 2022)
            }
        }
        db_list.append(db_line)


def review(stop, start=1):
    for pk in range(start, stop):
        db_line = {
            "model": "app_car_reviews.reviews",
            "pk": pk,
            "fields": {
                "author_email": f'author{str(pk)}@mail.com',
                "car": random.randrange(1, CARS),
                "date_of_creation": random_date(),
                "comment": f'Comment text {str(pk)}'
            }
        }
        db_list.append(db_line)


def main():
    country(COUNTRYES)
    manufacturer(MANUFACTURES)
    car(CARS)
    review(REVIEWS)

    with open('fixtures/test_db_data.json', 'w') as file:
        json.dump(db_list, file)


if __name__ == '__main__':
    main()
