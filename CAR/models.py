from django.db import models


class CarShop(models.Model):
    CAR_TYPE = (
        ('Для молодых людей', "Для молодых людей"),
        ("Для работы", "Для работы"),
        ("Для большой семьи", "Для большой семье"),
        ("Для путешествий", "Для путешествий"),
        ("Для женщин", "Для женщин"),
        ("Для успешных", "Для успешных")
    )
    title = models.CharField("Название модели", max_length=100)
    description = models.TextField("Описание автомобиля")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()
    specifications = models.TextField("Характеристики", null=True)
    model_year = models.TextField("Модельный год", null=True)
    manufacturing_country = models.TextField("Страна изготовитель", null=True)

    def __str__(self):
        return self.title


class ReviewsCar(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    car_choice_comment = models.ForeignKey(CarShop, on_delete=models.CASCADE,
                                           related_name="comment_object")
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    rate_stars = models.CharField(max_length=100, choices=RATING)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.car_choice_comment}: {self.text} {self.rate_stars}'
