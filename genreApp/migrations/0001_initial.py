# Generated by Django 5.1.5 on 2025-03-29 10:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration', models.FloatField(blank=True, null=True)),
                ('file', models.FileField(upload_to='songs/')),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('chroma_stft_mean', models.FloatField(blank=True, null=True)),
                ('chroma_stft_var', models.FloatField(blank=True, null=True)),
                ('rms_mean', models.FloatField(blank=True, null=True)),
                ('rms_var', models.FloatField(blank=True, null=True)),
                ('spectral_centroid_mean', models.FloatField(blank=True, null=True)),
                ('spectral_centroid_var', models.FloatField(blank=True, null=True)),
                ('spectral_bandwidth_mean', models.FloatField(blank=True, null=True)),
                ('spectral_bandwidth_var', models.FloatField(blank=True, null=True)),
                ('rolloff_mean', models.FloatField(blank=True, null=True)),
                ('rolloff_var', models.FloatField(blank=True, null=True)),
                ('zero_crossing_rate_mean', models.FloatField(blank=True, null=True)),
                ('zero_crossing_rate_var', models.FloatField(blank=True, null=True)),
                ('harmony_mean', models.FloatField(blank=True, null=True)),
                ('harmony_var', models.FloatField(blank=True, null=True)),
                ('perceptr_mean', models.FloatField(blank=True, null=True)),
                ('perceptr_var', models.FloatField(blank=True, null=True)),
                ('tempo', models.FloatField(blank=True, null=True)),
                ('mfcc1_mean', models.FloatField(blank=True, null=True)),
                ('mfcc1_var', models.FloatField(blank=True, null=True)),
                ('mfcc2_mean', models.FloatField(blank=True, null=True)),
                ('mfcc2_var', models.FloatField(blank=True, null=True)),
                ('mfcc3_mean', models.FloatField(blank=True, null=True)),
                ('mfcc3_var', models.FloatField(blank=True, null=True)),
                ('mfcc4_mean', models.FloatField(blank=True, null=True)),
                ('mfcc4_var', models.FloatField(blank=True, null=True)),
                ('mfcc5_mean', models.FloatField(blank=True, null=True)),
                ('mfcc5_var', models.FloatField(blank=True, null=True)),
                ('mfcc6_mean', models.FloatField(blank=True, null=True)),
                ('mfcc6_var', models.FloatField(blank=True, null=True)),
                ('mfcc7_mean', models.FloatField(blank=True, null=True)),
                ('mfcc7_var', models.FloatField(blank=True, null=True)),
                ('mfcc8_mean', models.FloatField(blank=True, null=True)),
                ('mfcc8_var', models.FloatField(blank=True, null=True)),
                ('mfcc9_mean', models.FloatField(blank=True, null=True)),
                ('mfcc9_var', models.FloatField(blank=True, null=True)),
                ('mfcc10_mean', models.FloatField(blank=True, null=True)),
                ('mfcc10_var', models.FloatField(blank=True, null=True)),
                ('mfcc11_mean', models.FloatField(blank=True, null=True)),
                ('mfcc11_var', models.FloatField(blank=True, null=True)),
                ('mfcc12_mean', models.FloatField(blank=True, null=True)),
                ('mfcc12_var', models.FloatField(blank=True, null=True)),
                ('mfcc13_mean', models.FloatField(blank=True, null=True)),
                ('mfcc13_var', models.FloatField(blank=True, null=True)),
                ('mfcc14_mean', models.FloatField(blank=True, null=True)),
                ('mfcc14_var', models.FloatField(blank=True, null=True)),
                ('mfcc15_mean', models.FloatField(blank=True, null=True)),
                ('mfcc15_var', models.FloatField(blank=True, null=True)),
                ('mfcc16_mean', models.FloatField(blank=True, null=True)),
                ('mfcc16_var', models.FloatField(blank=True, null=True)),
                ('mfcc17_mean', models.FloatField(blank=True, null=True)),
                ('mfcc17_var', models.FloatField(blank=True, null=True)),
                ('mfcc18_mean', models.FloatField(blank=True, null=True)),
                ('mfcc18_var', models.FloatField(blank=True, null=True)),
                ('mfcc19_mean', models.FloatField(blank=True, null=True)),
                ('mfcc19_var', models.FloatField(blank=True, null=True)),
                ('mfcc20_mean', models.FloatField(blank=True, null=True)),
                ('mfcc20_var', models.FloatField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
