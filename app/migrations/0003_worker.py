# Generated by Django 4.1.7 on 2023-04-08 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_depatment_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100, unique=True)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.IntegerField()),
                ('hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField(null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]