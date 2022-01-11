# collect email from a string
import re

str = '''
Join Softobiz
About Us
Softobiz Technologies India | Contact Us

Reach Us!
Want to connect with us on a call or send an email? Please select from the options below.

+91-172-4000275
India

+1(732)-231-2522
United States

info@softobiz.com
Reach out to us via email

Softobiz Technologies India
Maximize your ROI and minimize chances of failure with our research-backed MVP & Prototyping services.
Leverage our industry expertise to plan a successful IoT journey.
Transform your business to overcome new challenges and leverage new opportunities.
Leverage our DevOps expertise to deploy apps faster while ensuring the finest quality.
Improve your brand’s value with interactive UI/UX design experiences.
Let’s work together to unravel new paths, uncover new possibilities, and transform the world with products that make a difference.
Accelerate software development and unlock unlimited business potential with our agile development services.
Gain an edge over your competitors with powerful and feature-rich mobile apps.
Grow your business with bespoke enterprise solutions that appeal to your business needs.
Jump-start a successful transformation journey to the cloud with our cutting-edge cloud computing services.
Maximize your ROI and minimize chances of failure with our research-backed MVP & Prototyping services.
Leverage our industry expertise to plan a successful IoT journey.
Transform your business to overcome new challenges and leverage new opportunities.
Leverage our DevOps expertise to deploy apps faster while ensuring the finest quality.
Improve your brand’s value with interactive UI/UX design experiences.
Let’s work together to unravel new paths, uncover new possibilities, and transform the world with products that make a difference.
Accelerate software development and unlock unlimited business potential with our agile development services.
Gain an edge over your competitors with powerful and feature-rich mobile apps.
Grow your business with bespoke enterprise solutions that appeal to your business needs.
Jump-start a successful transformation journey to the cloud with our cutting-edge cloud computing services.
© 2022 Softobiz. All Rights Reserved.

SERVICES
Agile Software Development
Enterprise Application Development
Mobile App Development
Digital Transformation
Cloud Computing
Devops
MVP & Prototyping
UX & UI
Internet of Things (IOT)
ABOUT US
About Us
Join Softobiz
Case Studies
Insights
Contact Us
FIND US
SoftoBiz Technologies (P) LTD
Sector 67, Sahibzada Ajit Singh Nagar, Punjab 160062

'''

# lst = re.findall(r'[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+', str)
# lst = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', str)
lst = re.findall(r'\w+@\S+\w', str)
# print(lst)

index = 1
for i in lst:
    print(index, i)
    index += 1