from django.template.defaulttags import register


@register.filter
def get_count(lists):
    need_line = 6
    for row in lists:
        need_line -= 1
    return range(need_line)


