import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter
def sub(value,arg):
    return value - arg


@register.simple_tag()
def debug_object_dump(var):
    return vars(var)



@register.filter()

def mark(value):
    extensions = ["nl2br","fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

    # 입력된 무자열을 html 코드로 변환해 주는 필터함수입니다..