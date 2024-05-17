# Generated by Django 5.0.3 on 2024-03-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_delete_student_10'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('image_path', models.ImageField(blank=True, upload_to='images', verbose_name='Сүрөтү')),
                ('gender', models.CharField(max_length=120, null=True, verbose_name='Жынысы')),
                ('birth_day', models.CharField(max_length=120, verbose_name='Тууган күнү')),
                ('class_of_year', models.CharField(max_length=120, verbose_name='Бүтүргөн классы')),
                ('region', models.TextField(verbose_name='Жашаган жери')),
                ('phone_number_student', models.CharField(max_length=120, verbose_name='Окуучунун телефон номери')),
                ('name_of_dud_mum', models.TextField(verbose_name='Ата-энесини аты-жөнү')),
                ('phone_of_dud_mum', models.CharField(max_length=120, verbose_name='Ата-энесинин телефону')),
                ('name_guardian', models.CharField(max_length=120, verbose_name='Жоопту киши')),
                ('phone_guardian', models.CharField(max_length=120, verbose_name='Жоопту кишинин номери')),
                ('whatsapp', models.CharField(max_length=120, verbose_name='Ватсап номери')),
                ('interesting_lesson', models.TextField(verbose_name='Кызыккан сабагы')),
                ('success', models.TextField(max_length=120, verbose_name='Ийгиликтери')),
                ('hobbies', models.TextField(max_length=120, verbose_name='Өнөрлөрү(Жөндөмдүүлүктөрү)')),
                ('date_of_saving', models.DateTimeField(auto_now_add=True, verbose_name='')),
            ],
            options={
                'verbose_name': '10-Класс',
                'verbose_name_plural': '10-Класс',
            },
        ),
    ]