

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_watch_quantity_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='more_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
