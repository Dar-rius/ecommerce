# Generated by Django 4.0.6 on 2022-08-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=200)),
                ('pTotal', models.IntegerField(default=0)),
                ('quantite', models.IntegerField(default=0)),
                ('livraison', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=200)),
                ('quantite', models.IntegerField(default=0)),
                ('pTotal', models.IntegerField(default=0)),
                ('photo_produit', models.ImageField(upload_to='images_card/')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=200)),
                ('marque_produit', models.CharField(max_length=100)),
                ('descrip_produit', models.TextField()),
                ('prix_produit', models.IntegerField(default=0)),
                ('quantite_produit', models.IntegerField(default=0)),
                ('cat_produit', models.CharField(choices=[('Informatique', 'Informatique'), ('Bureautique', 'Bureautique'), ('Telephone', 'Telephone'), ('Accesoir', 'Accesoir'), ('Console et jeux video', 'Console et jeux video'), ('Multimedia', 'Multimedia')], max_length=50, verbose_name='categories')),
                ('photo_produit', models.ImageField(upload_to='images/')),
                ('tendance', models.IntegerField(default=0)),
            ],
        ),
    ]
