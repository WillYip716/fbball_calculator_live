# Generated by Django 3.1.5 on 2021-07-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvrComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pos', models.CharField(max_length=1)),
                ('FGM', models.FloatField()),
                ('FGA', models.FloatField()),
                ('FG_PCT', models.FloatField()),
                ('FG3M', models.FloatField()),
                ('FTM', models.FloatField()),
                ('FTA', models.FloatField()),
                ('FT_PCT', models.FloatField()),
                ('REB', models.FloatField()),
                ('AST', models.FloatField()),
                ('STL', models.FloatField()),
                ('BLK', models.FloatField()),
                ('TOV', models.FloatField()),
                ('PTS', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PLAYER_ID', models.IntegerField()),
                ('Player_Name', models.CharField(max_length=255)),
                ('Team_ID', models.IntegerField()),
                ('Team_Name', models.CharField(max_length=255)),
                ('GP', models.IntegerField()),
                ('MIN', models.FloatField()),
                ('FGM', models.FloatField()),
                ('FGA', models.FloatField()),
                ('FG_PCT', models.FloatField()),
                ('FG3M', models.FloatField()),
                ('FG3A', models.FloatField()),
                ('FG3_PCT', models.FloatField()),
                ('FTM', models.FloatField()),
                ('FTA', models.FloatField()),
                ('FT_PCT', models.FloatField()),
                ('OREB', models.FloatField()),
                ('DREB', models.FloatField()),
                ('REB', models.FloatField()),
                ('AST', models.FloatField()),
                ('STL', models.FloatField()),
                ('BLK', models.FloatField()),
                ('TOV', models.FloatField()),
                ('PF', models.FloatField()),
                ('PTS', models.FloatField()),
                ('PosStr', models.CharField(default='', max_length=3)),
                ('FTeamPos', models.CharField(default='', max_length=3)),
                ('Pos', models.ManyToManyField(to='fball_calculator.Positions')),
            ],
        ),
    ]
