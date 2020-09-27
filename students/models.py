from django.db import models


class Student(models.Model):
    """Student Model"""

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="По-батькові",
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name="Дата народження",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name="Фото",
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Білет")

    notes = models.TextField(
        blank=True,
        verbose_name="Додаткові нотатки")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

    def __str__(self):
        """ Return the first_name plus the last_name, with a space in betwen"""

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()