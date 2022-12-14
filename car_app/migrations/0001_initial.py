# Generated by Django 2.2.4 on 2022-10-14 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=45)),
                ('model', models.CharField(max_length=45)),
                ('color', models.CharField(max_length=45)),
                ('production_year', models.IntegerField()),
                ('plate_number', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('photo', models.FileField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='user_app.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.TextField(null=True)),
                ('comment', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_feedhback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_feedback', to='user_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Car_Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_feedback', to='car_app.Car')),
                ('cars', models.ManyToManyField(related_name='feededbacked_cars', to='car_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_date', models.DateField(null=True)),
                ('drop_off_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_booked', to='car_app.Car')),
                ('customer_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_booked', to='user_app.Customer')),
            ],
        ),
    ]
