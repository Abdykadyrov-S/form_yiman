from django.db import models

genders = [
    ('эркек', 'Эркек'),
    ('кыз', 'Кыз'),
]
classes = [
    ('7-класс', '7-класс'),
    ('8-класс', '8-класс'),
    ('9-класс', '9-класс'),
    ('10-класс', '10-класс'),
]
lang = [
    ('кыргыз тили', 'Кыргыз тили'),
    ('орус тили', 'Орус тили'),
]

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(verbose_name="Окуучунун толук аты жөнү", max_length=120)
    image_path = models.ImageField(verbose_name="Окуучунун сүрөтү (3Х4 өлчөмүндө)", upload_to="images", blank=True, null=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120, choices=genders, default="эркек", blank=True, null=True)
    birth_day = models.CharField(verbose_name="Тууган күнү, айы, жылы", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120, choices=classes, default="7-класс",
                                     null=True)
    region = models.CharField(verbose_name="Жашаган облусу, району, айылы", max_length=120)
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.CharField(verbose_name="Ата-энесинин аты-жөнү", max_length=120)
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин байланыш номери", max_length=120)
    name_guardian = models.CharField(verbose_name="Окуучуга жоопту кишинин толук аты-жөнү", max_length=120)
    phone_guardian = models.CharField(verbose_name="Окуучуга жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ар дайым байланышта болгон вотсап номери", max_length=120)
    interesting_lesson = models.CharField(verbose_name="Кызыккан сабактары", max_length=120)
    success = models.CharField(verbose_name="Ийгиликтери (олимпиада, сабактар, спорт, маданий ж.б.)", max_length=120)
    hobbies = models.CharField(verbose_name="Өнөрлөрү (Жөндөмдүүлүктөрү)", max_length=120)
    lang = models.CharField(verbose_name="Сынакты кайсыл тилде тапшырасыз?", max_length=120, choices=lang, default="Кыргыз тили",
                                     null=True)
    date_of_saving = models.DateTimeField(verbose_name="Катталган датасы", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Жалпы"
        verbose_name_plural = "Жалпы"

    def __str__(self):
        return self.full_name
    
class Student_7(models.Model):
    full_name = models.CharField(verbose_name="Окуучунун толук аты жөнү", max_length=120)
    image_path = models.ImageField(verbose_name="Окуучунун сүрөтү (3Х4 өлчөмүндө)", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120, choices=genders, default="эркек", null=True)
    birth_day = models.CharField(verbose_name="Тууган күнү, айы, жылы", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120, choices=classes, default="7-класс",
                                     null=True)
    region = models.CharField(verbose_name="Жашаган облусу, району, айылы", max_length=120)
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.CharField(verbose_name="Ата-энесинин аты-жөнү", max_length=120)
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин байланыш номери", max_length=120)
    name_guardian = models.CharField(verbose_name="Окуучуга жоопту кишинин толук аты-жөнү", max_length=120)
    phone_guardian = models.CharField(verbose_name="Окуучуга жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ар дайым байланышта болгон вотсап номери", max_length=120)
    interesting_lesson = models.CharField(verbose_name="Кызыккан сабактары", max_length=120)
    success = models.CharField(verbose_name="Ийгиликтери (олимпиада, сабактар, спорт, маданий ж.б.)", max_length=120)
    hobbies = models.CharField(verbose_name="Өнөрлөрү (Жөндөмдүүлүктөрү)", max_length=120)
    lang = models.CharField(verbose_name="Сынакты кайсыл тилде тапшырасыз?", max_length=120, choices=lang, default="Кыргыз тили",
                                     null=True)
    date_of_saving = models.DateTimeField(verbose_name="Катталган датасы", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "7-Класс"
        verbose_name_plural = "7-Класс"

    def __str__(self):
        return self.full_name


class Student_8(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    lang = models.CharField(verbose_name="Сынакты кайсыл тилде тапшырасыз?", max_length=120, choices=lang, default="Кыргыз тили",
                                     null=True)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "8-Класс"
        verbose_name_plural = "8-Класс"

    def __str__(self):
        return self.full_name


class Student_9(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    lang = models.CharField(verbose_name="Сынакты кайсыл тилде тапшырасыз?", max_length=120, choices=lang, default="Кыргыз тили",
                                     null=True)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "9-Класс"
        verbose_name_plural = "9-Класс"

    def __str__(self):
        return self.full_name


class Student_10(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120, null=True)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    lang = models.CharField(verbose_name="Сынакты кайсыл тилде тапшырасыз?", max_length=120, choices=lang, default="Кыргыз тили",
                                     null=True)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "10-Класс"
        verbose_name_plural = "10-Класс"

    def __str__(self):
        return self.full_name
    

class Active(models.Model):
    is_start = models.BooleanField(
        default=False,
        verbose_name="Активация"
    )

    def __str__(self):
        return f"Азыркы учурда - {self.is_start}"

    class Meta:
        verbose_name = "Активация"
        verbose_name_plural = "Активация"

    