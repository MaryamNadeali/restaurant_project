# Generated by Django 3.2.9 on 2022-03-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان تگ')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='عنوان لاتین')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(related_name='blog', to='blogs.Tag', verbose_name='تگ ها'),
        ),
    ]