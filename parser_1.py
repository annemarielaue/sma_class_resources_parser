from bs4 import BeautifulSoup
import requests
import json

cookies = {
    # Name : Value
    'wp-postpass_464b0e8bc4f9a79dba4186fc94e5189d': '%24P%24BPGWdk.V.jEN0ruMsY8e.GkQSvPEvL0',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
}


# driver = [
#     url, name of page, first index (50), second index (170)
# ]

# for each item in drvier 

for classResources in ""
    print()

URL = "https://www.stmonicaacademy.com/student-parents/class-resources/"
page = requests.get(URL, cookies=cookies)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())

list_of_urls_on_page = []

# extracted_video_title = "POOP POOP"

for a_tag in soup.find_all('a'):
    # print(a_tag.get('href'))
    list_of_urls_on_page.append([a_tag.get('href'), a_tag.text])

# print(list_of_urls_on_page[81:170])

with open("data.json", "w", newline="") as file:
    file.write(json.dumps(list_of_urls_on_page[81:170]))

# with open("stmonicaacademy_student-parents_class-resources.html", "w", newline="") as file:
#     file.write(page.text)
    



    