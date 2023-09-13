from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Страна")

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f'{self.name}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Название производителя")
    country = models.ForeignKey(Country, related_name='manufacturers', on_delete=models.CASCADE, verbose_name="Страна")

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Название автомобиля")
    manufacturer = models.ForeignKey(Manufacturer, related_name='cars', on_delete=models.CASCADE,
                                     verbose_name="Производитель")
    release_year = models.PositiveSmallIntegerField(blank=True, verbose_name='Год начала выпуска')
    end_year = models.PositiveSmallIntegerField(blank=True, verbose_name='Год окончания выпуска')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.name}'


class Reviews(models.Model):
    author_email = models.EmailField(verbose_name='E-mail автора')
    car = models.ForeignKey(Car, related_name='reviews', on_delete=models.CASCADE, verbose_name='Автомобиль')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    comment = models.TextField(blank=True, verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author_email} about {self.car} at {self.date_of_creation}'
