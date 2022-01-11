# collect email from a string/web-page
import re

str = '''
International Tractors Limited Vill. Chak Gurjran, P.O. Piplanwala Jalandhar road, Hoshiarpur, Punjab, (India) 146022.
01882 522 220
sonalika@sonalika.com
exports@sonalika.com
'''

lst = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', str)

# print(lst)

index = 1
for i in lst:
    print(index, i)
    index += 1