from django.http import HttpResponse
import random


def status(request):
    return HttpResponse('OK')


def random_unicorn(request):
    color = "%06x" % random.randint(0, 0xFFFFFF)
    color_text = hex((int(color, 16) & 0xFF000000) | (~int(color, 16) & 0x00FFFFFF))
    html = f'<html><body bgcolor={color}><h1 style="color:{color_text[2:]};">Generated color {color}</h1></body></html>'
    return HttpResponse(html)
