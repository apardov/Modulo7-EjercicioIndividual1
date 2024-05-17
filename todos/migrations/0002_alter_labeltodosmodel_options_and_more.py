# Generated by Django 5.0.4 on 2024-05-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labeltodosmodel',
            options={'verbose_name': 'Etiqueta', 'verbose_name_plural': 'Etiquetas'},
        ),
        migrations.AlterModelOptions(
            name='todosusermodel',
            options={'verbose_name': 'Tarea', 'verbose_name_plural': 'Listado de Tareas'},
        ),
        migrations.RemoveField(
            model_name='todosusermodel',
            name='label',
        ),
        migrations.AddField(
            model_name='todosusermodel',
            name='labels',
            field=models.ManyToManyField(blank=True, to='todos.labeltodosmodel', verbose_name='Etiquetas'),
        ),
    ]
