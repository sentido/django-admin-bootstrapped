# -*- coding: utf-8 -*-
"""
"""
from __future__ import absolute_import

from django.conf import settings
from django.forms import widgets
from django.utils import formats
from django.utils.safestring import mark_safe


class BootstrapDateTimeWidgetMixin(object):
    class Media:
        css = {
            'all':('bootstrap-datetimepicker/bootstrap-datetimepicker.min.css',),
            }

        js = (
            'bootstrap-datetimepicker/bootstrap-datetimepicker.min.js',
            'bootstrap-datetimepicker/bootstrap-datetimepicker-activate.js',
        )

    widget_format = 'dd.MM.yyyy hh:mm:ss'
    show_above = False
    pick_date = True
    pick_time = True

    # TODO: Extract to template
    TEMPLATE = u'<div id="{id}" class="input-append date bootstrap-datetimepicker" data-show-above="{show_above}" data-format="{format}" data-pick-time="{pick_time}" data-pick-date="{pick_date}" >' \
               u'{original}<span class="add-on"><i data-time-icon="icon-time" data-date-icon="icon-calendar"></i></span>' \
               u'</div>'

    def __init__(self, widget_format=None, pick_date=None, pick_time=None, show_above=None, *args, **kwargs):
        super(BootstrapDateTimeWidgetMixin, self).__init__(*args, **kwargs)

        self.widget_format = widget_format if widget_format else self.widget_format
        self.show_above    = show_above if show_above is not None else self.show_above
        self.pick_date     = pick_date if pick_date is not None else self.pick_date
        self.pick_time     = pick_time if pick_time is not None else self.pick_time


    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}

        attrs['data-format'] = self.widget_format

        rendered = super(BootstrapDateTimeWidgetMixin, self).render(name, value, attrs)

        id = 'datetimepicker'
        if attrs:
            id = attrs.get('id', id)
        id += '-wrapper'

        rendered = self.TEMPLATE.format(
            original=rendered,
            id=id,
            show_above=self.show_above,
            pick_time=self.pick_time,
            pick_date=self.pick_date,
            format=self.widget_format
        )

        return mark_safe(rendered)


class BootstrapDateTimeWidget(BootstrapDateTimeWidgetMixin, widgets.DateInput):
    pick_date = True
    pick_time = True
    widget_format = 'dd.MM.yyyy hh:mm'

class BootstrapDateWidget(BootstrapDateTimeWidgetMixin, widgets.DateInput):
    pick_date = True
    pick_time = False
    widget_format = 'dd.MM.yyyy'


class BootstrapTimeWidget(BootstrapDateTimeWidgetMixin, widgets.TimeInput):
    pick_date = False
    pick_time = True
    widget_format = 'hh:mm'


