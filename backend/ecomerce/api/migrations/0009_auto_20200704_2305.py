# Generated by Django 3.0.4 on 2020-07-05 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200704_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaints',
            options={'verbose_name': 'Denunciante', 'verbose_name_plural': 'Denunciantes'},
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='date',
        ),
        migrations.AddField(
            model_name='complaints',
            name='comment',
            field=models.TextField(null=True, verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='problem',
            field=models.CharField(max_length=20, null=True, verbose_name='Problema'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='accuser_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accuser_user_id', to=settings.AUTH_USER_MODEL, verbose_name='Denunciante'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='denounced_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='denounced_user_id', to=settings.AUTH_USER_MODEL, verbose_name='Denunciado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payment_method_order', to='api.Payment_method'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_method_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shipping_method_order', to='api.Shipping_method'),
        ),
        migrations.AlterField(
            model_name='payment_data',
            name='payment_method_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payment_method', to='api.Payment_method'),
        ),
    ]
