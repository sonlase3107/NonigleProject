from datetime import datetime

from django import template
from django.template.defaultfilters import stringfilter
from dateutil import parser

register = template.Library()


@register.simple_tag
def checks():
    return 'Le Anh Son'


@register.filter
@stringfilter
def dateformat(value: datetime):
    return convertdate(value)


def convertdate(datetime_str):
    current = datetime.now()
    time_iso_created = parser.parse(datetime_str)
    remain_sec = (current - time_iso_created.replace(tzinfo=None)).total_seconds()
    print(current, time_iso_created.replace(tzinfo=None))
    if remain_sec >= 86400:
        return str(int(remain_sec / (60 * 60 * 24))) + ' day ago '
    if remain_sec >= 3600:
        return str(int(remain_sec / (60 * 60))) + ' hour ago'
    if remain_sec > 60:
        return str(int(remain_sec / 60)) + ' minutes ago'
    if remain_sec <= 60:
        return str(int(remain_sec)) + ' second ago'
