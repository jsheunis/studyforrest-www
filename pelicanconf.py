#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'Michael Hanke & Alex Waite'
SITENAME = u'studyforrest.org'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['better_tables', 'bootstrap-rst', 'pelican_javascript', 'tipue_search',]

THEME = 'pelican-theme'
DIRECT_TEMPLATES = ['categories', 'authors', 'archives', 'search'] # unset all templates; use these

#
# Disable when developing
#
FEED_ALL_ATOM = None

#
# Configure the site
#
STATIC_PATHS = ['img', 'pics', 'css', 'js', 'data']
MENUITEMS = (
            ('About', 'about.html'),
            ('Access', 'access.html'),
            ('Data', 'data.html'),
            ('Publications', 'categories.html'),
)
LINKS = (('Psychoinformatics', 'http://psychoinformatics.de'),
         ('Real-Life Cognition Channel', 'http://f1000research.com/channels/real-cognition'),
         ('NeuroDebian', 'http://neuro.debian.net'),
         ('PyMVPA', 'http://www.pymvpa.org'))
DEFAULT_PAGINATION = 10

#
# Social media jazz
#
ADDTHIS_PROFILE = 'ra-53a573780cc42d73'
GOOGLE_ANALYTICS = "UA-46839658-1"
TWITTER_USERNAME = 'studyforrest'
TWITTER_WIDGET_ID = '435327568237965312'

#
# Likely to be removed
#
RESPONSIVE_IMAGES = True
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
WITH_FUTURE_DATES = True
SHOW_ARTICLE_AUTHOR = True
