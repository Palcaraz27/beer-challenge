from django.db import migrations

def create_default_beer(apps, schema_editor):
    Beer = apps.get_model('festival', 'Beer')
    Beer.objects.create(id= 1, name='Estrella Levante', price=1)

def remove_default_beer(apps, schema_editor):
    Beer = apps.get_model('festival', 'Beer')
    instance = Beer.objects.get(id=1)
    instance.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_beer, reverse_code=remove_default_beer),
    ]