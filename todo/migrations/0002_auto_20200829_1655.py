# Generated by Django 2.2.15 on 2020-08-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howtoorder',
            name='order',
            field=models.CharField(choices=[('creation_order', '作成された順'), ('due_order', '締め切り順'), ('priority_order', '優先度順')], default='creation_order', max_length=50, verbose_name='並び順'),
        ),
    ]