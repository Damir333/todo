from django.template.defaulttags import register


@register.filter
def get_count(lists):
    lst = []
    count = 0
    need_lines = 0
    for row in lists:
        count += 1
    need_lines = 8 - count
    while need_lines:
        lst.append(need_lines)
        need_lines -= 1
    return lst
