# Generated by Django 5.0.6 on 2024-05-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todoitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('Todo', 'To-do'), ('DoToday', 'Do today'), ('InProcess', 'In Process'), ('Done', 'Done')], default='Todo', max_length=20),
        ),
    ]
