from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEntrega1', '0002_rename_contactmessages_contactmessage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('admin', models.CharField(max_length=30)),
                ('password', models.EmailField(max_length=45)),
            ]
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
