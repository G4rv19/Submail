from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        # If there are any dependencies, list them here
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField()),
            ],
        ),
    ]
