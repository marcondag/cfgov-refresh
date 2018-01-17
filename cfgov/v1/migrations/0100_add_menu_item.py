# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('v1', '0099_add_rule_options_to_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_text', models.CharField(help_text=b'Display text for menu link', max_length=255)),
                ('external_link', models.CharField(default=b'#', max_length=1000, null=True, help_text=b'Enter url for page outside Wagtail.', blank=True)),
                ('order', models.PositiveSmallIntegerField(help_text=b'Determines order in which this menu item appears in nav.', null=True, blank=True)),
                ('column_1', wagtail.wagtailcore.fields.StreamField([(b'nav_group', wagtail.wagtailcore.blocks.StructBlock([(b'draft', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If draft is selected, this nav section will only show on sharing sites (like Content).', default=False, required=False)), (b'group_title', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'Column title')), (b'hide_group_title', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Hide column title')), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'state', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select state for this nav link. If draft, will only show on sharing sites (like Content). If live, will only show if not sharing site.', choices=[(b'both', b'Live and draft'), (b'live', b'Live'), (b'draft', b'Draft')])), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))], required=False)), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))]))])))]), required=False))], label=b'Nav items group'))], blank=True)),
                ('column_2', wagtail.wagtailcore.fields.StreamField([(b'nav_group', wagtail.wagtailcore.blocks.StructBlock([(b'draft', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If draft is selected, this nav section will only show on sharing sites (like Content).', default=False, required=False)), (b'group_title', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'Column title')), (b'hide_group_title', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Hide column title')), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'state', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select state for this nav link. If draft, will only show on sharing sites (like Content). If live, will only show if not sharing site.', choices=[(b'both', b'Live and draft'), (b'live', b'Live'), (b'draft', b'Draft')])), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))], required=False)), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))]))])))]), required=False))], label=b'Nav items group'))], blank=True)),
                ('column_3', wagtail.wagtailcore.fields.StreamField([(b'nav_group', wagtail.wagtailcore.blocks.StructBlock([(b'draft', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If draft is selected, this nav section will only show on sharing sites (like Content).', default=False, required=False)), (b'group_title', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'Column title')), (b'hide_group_title', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Hide column title')), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'state', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select state for this nav link. If draft, will only show on sharing sites (like Content). If live, will only show if not sharing site.', choices=[(b'both', b'Live and draft'), (b'live', b'Live'), (b'draft', b'Draft')])), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))], required=False)), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))]))])))]), required=False))], label=b'Nav items group'))], blank=True)),
                ('column_4', wagtail.wagtailcore.fields.StreamField([(b'nav_group', wagtail.wagtailcore.blocks.StructBlock([(b'draft', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If draft is selected, this nav section will only show on sharing sites (like Content).', default=False, required=False)), (b'group_title', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'Column title')), (b'hide_group_title', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Hide column title')), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'state', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select state for this nav link. If draft, will only show on sharing sites (like Content). If live, will only show if not sharing site.', choices=[(b'both', b'Live and draft'), (b'live', b'Live'), (b'draft', b'Draft')])), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))], required=False)), (b'nav_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.StructBlock([(b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'page_link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Link to a page in Wagtail.', required=False)), (b'external_link', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter url for page outside Wagtail. This will only be used if there is no page link.', max_length=1000, required=False))]))])))]), required=False))], label=b'Nav items group')), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'draft', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'link', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(help_text=b"If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))]))], label=b'Featured content module'))], blank=True)),
                ('nav_footer', wagtail.wagtailcore.fields.StreamField([(b'nav_footer', wagtail.wagtailcore.blocks.StructBlock([(b'draft', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False))], label=b'Footer'))], blank=True)),
                ('page_link', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', help_text=b'Link to a page in Wagtail.', null=True)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]