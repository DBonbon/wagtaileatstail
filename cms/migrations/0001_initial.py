# Generated by Django 3.2.8 on 2021-10-22 22:54

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailtrans', '0010_auto_20211022_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleIndexPage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.translatablepage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.translatablepage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('article_section_title', models.CharField(blank=True, help_text='Title to display above the article section', max_length=255, null=True)),
                ('article_section_intro', wagtail.core.fields.RichTextField(blank=True)),
                ('article_section', models.ForeignKey(blank=True, help_text='Featured articles for the homepage', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailtrans.translatablepage', verbose_name='Article section')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.translatablepage')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('body', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('caption', wagtail.core.blocks.CharBlock(label='Caption', required=False)), ('float', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'Right'), ('left', 'Left'), ('center', 'Center')], label='Float', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], label='Size', required=False))])), ('video', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(label='Video')), ('caption', wagtail.core.blocks.CharBlock(label='Caption', required=False)), ('float', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'Right'), ('left', 'Left'), ('center', 'Center')], label='Float', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], label='Size', required=False))]))])),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
    ]
