

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='quantity_available',
            field=models.IntegerField(default=0),
        ),
    ]
