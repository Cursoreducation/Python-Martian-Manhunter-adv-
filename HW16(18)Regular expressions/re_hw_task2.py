import requests
import re

site = requests.get("http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%"
                    "B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%8"
                    "2%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82"
                    "%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%"
                    "D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83")
res = re.finditer(r"<p>(?P<institution>.*).*(\n\t)?<b>(?P<email>.*)<", site.text)
res_1 = list((re.sub(r'\t', '', match.group('institution')), match.group('email')) for match in res)
print(res_1)
dict_group = {}
res_2 = re.finditer(r">\s\d+\.\s((?P<title>[а-яА-Яa-z-іїІЇЄє,\s]+)\<\/span><\/h2>\s?)((<p>)?[а-яА-Яa-z-іїІЇЄє,.\s]+<b>[a"
                    r"-zA-Z0-9_@.]+<\/b>\s?\n?(<\/p>)?)*", site.text)
for i in res_2:
    result = re.finditer(r'<p>(?P<institution>.*).*(\n\t)?<b>(?P<email>.*)<<', i.group(0))
    dict_group.update({i.group("title"): list((re.sub(r"\t", "", match.group("institution")), match.group("email")) for
                                              match in result)})
print(dict_group)