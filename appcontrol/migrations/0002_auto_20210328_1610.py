# Generated by Django 3.1.7 on 2021-03-28 21:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcontrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jefe',
            name='fechahora_creacion',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='actividad',
            fields=[
                ('id_actividad', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('telefono', models.CharField(blank=True, max_length=9, verbose_name='Teléfono')),
                ('correo', models.CharField(blank=True, max_length=100, verbose_name='Correo institucional')),
                ('nombre_dependencia', models.CharField(blank=True, max_length=200, verbose_name='Dependencia')),
                ('gr_comorbilidad', models.BooleanField(blank=True, verbose_name='Comorbilidad')),
                ('detalle_comorbilidad', models.CharField(blank=True, max_length=200, verbose_name='Detalle comorbilidad')),
                ('tiene_informe', models.BooleanField(blank=True, default=True, verbose_name='Tiene informe?')),
                ('actividad_resumen', models.CharField(blank=True, max_length=200, verbose_name='Resumen de actividad')),
                ('producto_entregado', models.CharField(blank=True, max_length=200, verbose_name='Producto entregado')),
                ('medio_verificacion', models.CharField(blank=True, max_length=200, verbose_name='Medio de verificación')),
                ('archivo_informe', models.FileField(null=True, upload_to='media/docs/informe')),
                ('modalidad', models.CharField(blank=True, max_length=200, verbose_name='Modalidad que trabajo')),
                ('dias_laborado', models.IntegerField(blank=True, verbose_name='Dias laborado')),
                ('nombre_jefe', models.CharField(blank=True, max_length=100, verbose_name='Jefe inmediato')),
                ('correo_jefe', models.CharField(blank=True, max_length=100, verbose_name='Correo de jefe inmediato')),
                ('telefono_jefe', models.CharField(blank=True, max_length=9, verbose_name='Télefono')),
                ('documento', models.CharField(blank=True, max_length=200, verbose_name='Documento de conformidad')),
                ('archivo_documento', models.FileField(null=True, upload_to='media/docs/documento')),
                ('observacion', models.CharField(blank=True, max_length=200, verbose_name='Observación')),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rf_persona_empleado_actividad', to='appcontrol.persona')),
                ('dni_jefe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rf_persona_jefe_actividad', to='appcontrol.persona')),
                ('id_dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appcontrol.dependencia')),
                ('id_periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appcontrol.periodo')),
                ('id_tipoactividad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appcontrol.tipoactividad')),
            ],
        ),
    ]
