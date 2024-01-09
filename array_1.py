# This code is for web scraping. It iterates over a list of class resources, makes HTTP requests to their respective URLs, parses the HTML content, extracts URLs based on the title, and writes the extracted data into separate JSON files for each class resource.


import os, shutil

from bs4 import BeautifulSoup
import json
import requests

import dominate
from dominate.tags import *


def createPrintLines():
    print()
    print()
    print()
    print()
    print()
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")




#python program to check if a directory exists
htmlFilesFolder = "htmlFiles"



# Check whether the specified path exists or not
isExist = os.path.exists(htmlFilesFolder)
if isExist:
   shutil.rmtree(htmlFilesFolder)
else:
   # Create a new directory because it does not exist
   os.makedirs(htmlFilesFolder)
   print("The" + htmlFilesFolder + " directory is created!")



# Using a cookies dictionary so I can verifying the client device
cookies = {
    # Name : Value
    "wp-postpass_464b0e8bc4f9a79dba4186fc94e5189d": "%24P%24BPGWdk.V.jEN0ruMsY8e.GkQSvPEvL0",
    "wordpress_test_cookie": "WP%20Cookie%20check",
}


# Create an array of class_resources
class_resources = []

# Apologetics
class_resource_metadata_1 = {
    "first_index": 81,
    "last_index": 170,
    "title": "Apologetics",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/apologetics/",
}
class_resources.append(class_resource_metadata_1)


# Pre-calc chapters
class_resource_metadata_2 = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 1",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-1/",
}
class_resources.append(class_resource_metadata_2)


# Pre-calc chapters
class_resource_metadata_2A = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 2",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-2/",
}
class_resources.append(class_resource_metadata_2A)


# Pre-calc chapters
class_resource_metadata_2B = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 3",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-3/",
}
class_resources.append(class_resource_metadata_2B)


# Pre-calc chapters
class_resource_metadata_2C = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 4",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-4/",
}
class_resources.append(class_resource_metadata_2C)


# Pre-calc chapters
class_resource_metadata_2D = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 5",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-5/",
}
class_resources.append(class_resource_metadata_2D)


# Pre-calc chapters
class_resource_metadata_2E = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 6",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-6/",
}
class_resources.append(class_resource_metadata_2E)


# Pre-calc chapters
class_resource_metadata_2F = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 7",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-7/",
}
class_resources.append(class_resource_metadata_2F)


# Pre-calc chapters
class_resource_metadata_2G = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 8",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-8/",
}
class_resources.append(class_resource_metadata_2G)


# Pre-calc chapters
class_resource_metadata_2H = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 9",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-9/",
}
class_resources.append(class_resource_metadata_2H)


# Pre-calc chapters
class_resource_metadata_2I = {
    "first_index": 0,
    "last_index": 100,
    "title": "Pre-Calc Chapter 10",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-10/",
}
class_resources.append(class_resource_metadata_2I)


# AP Chemistry
class_resource_metadata_3 = {
    "first_index": 89,
    "last_index": 113,
    "title": "AP Chemistry",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/ap-chemistry/",
}
class_resources.append(class_resource_metadata_3)


# Computer Science
class_resource_metadata_4 = {
    "first_index": 0,
    "last_index": 96,
    "title": "Computer Science",
    "url": "https://www.stmonicaacademy.com/computer-science/",
}
class_resources.append(class_resource_metadata_4)


# Physics link to semester 1
class_resource_metadata_5 = {
    "first_index": 81,
    "last_index": 192,
    "title": "Physics First Semester",
    "url": "https://www.stmonicaacademy.com/physics/first-semester/",
}
class_resources.append(class_resource_metadata_5)


# Physics link to semester 2
class_resource_metadata_5A = {
    "first_index": 71,
    "last_index": 84,
    "title": "Physics Second Semester",
    "url": "https://www.stmonicaacademy.com/physics/second-semester/",
}
class_resources.append(class_resource_metadata_5A)


# Latin
class_resource_metadata_6 = {
    "first_index": 81,
    "last_index": 85,
    "title": "Latin",
    "url": "https://www.stmonicaacademy.com/latin/",
}
class_resources.append(class_resource_metadata_6)


# Calculus
class_resource_metadata_7 = {
    "first_index": 0,
    "last_index": 96,
    "title": "Calculus",
    "url": "https://www.stmonicaacademy.com/calculus/",
}
class_resources.append(class_resource_metadata_7)


# Chemistry link to semester 1
class_resource_metadata_8 = {
    "first_index": 81,
    "last_index": 94,
    "title": "Chemistry First Semester",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/chemistry-first-chapter/",
}
class_resources.append(class_resource_metadata_8)


# Chemistry link to semester 2
class_resource_metadata_8A = {
    "first_index": 81,
    "last_index": 101,
    "title": "Chemistry Second Semetester",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/chemistry-second-chapter/",
}
class_resources.append(class_resource_metadata_8A)


# English link to medievel literature
# This webpage has no links on it
class_resource_metadata_9 = {
    "first_index": 0,
    "last_index": 0,
    "title": "English Medieval Literature",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/medieval-literature/",
}
class_resources.append(class_resource_metadata_9)


# English link to ancient literature
# This webpage has no links on it
class_resource_metadata_9A = {
    "first_index": 0,
    "last_index": 0,
    "title": "English Ancient Literature",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/ancient-literature/",
}
class_resources.append(class_resource_metadata_9A)


# Geometry webpage
class_resource_metadata_10 = {
    "first_index": 81,
    "last_index": 91,
    "title": "Geometry",
    "url": "https://www.stmonicaacademy.com/geometry/",
}
class_resources.append(class_resource_metadata_10)


# Geometry link to book one
class_resource_metadata_10A = {
    "first_index": 0,
    "last_index": 83,
    "title": "Geometry Book One",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-one/",
}
class_resources.append(class_resource_metadata_10A)


# Geometry link to two
class_resource_metadata_10B = {
    "first_index": 0,
    "last_index": 83,
    "title": "Geometry Book Two",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-two/",
}
class_resources.append(class_resource_metadata_10B)


# Geometry link to book three
class_resource_metadata_10C = {
    "first_index": 0,
    "last_index": 83,
    "title": "Geometry Book Three",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-three/",
}
class_resources.append(class_resource_metadata_10C)


# Geometry link to book four
class_resource_metadata_10D = {
    "first_index": 0,
    "last_index": 83,
    "title": "Geometry Book Four",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-four/",
}
class_resources.append(class_resource_metadata_10D)


# Geometry link to book five
class_resource_metadata_10E = {
    "first_index": 0,
    "last_index": 83,
    "title": "Geometry Book Five",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-five/",
}
class_resources.append(class_resource_metadata_10E)


#lean how to use the dominate library here: https://github.com/Knio/dominate
smaClassesDoc = dominate.document(title='SMA Classes')

with smaClassesDoc:
    with div(id='header').add(ul()):
        for class_resource in class_resources:
            li(a(class_resource['title'], href='%s' % class_resource["url"]))
print(smaClassesDoc)
createPrintLines()



count = 1

# Print the array using a for loop
for metadata in class_resources:
    # Code that does parsing stuff
    page = requests.get(metadata["url"], cookies=cookies)
    #print(page.text)

    soup = BeautifulSoup(page.text, "html.parser")

    # Initialize an empty list to store URLs
    list_of_urls_on_page = []
    # list_of_urls_on_page_a = []
    #list_of_urls_on_page_iframe = []

    if metadata["title"] == "Computer Science" or metadata["title"] == "Calculus":
        # Enters a loop to iterate over all <iframe> tags on the webpage using BeautifulSoup's find_all method
        # these specific iframes are an embeded youtube clients
        for iframe_tag in soup.find_all("iframe"):
            # For each <iframe> tag, it extracts the 'src' attribute (the URL) using iframe_tag.get('src') and appends it to list_of_urls_on_page
            list_of_urls_on_page.append([iframe_tag.get("src"), iframe_tag.text])
    elif metadata["title"] in [
        # all of these -- can get <a> , can't get <iframe> DATA
        "Physics First Semester",  # Links are wrong -- Gave range, but is wrong index
        "Physics Second Semester",  # Links are wrong -- Gave range, but is wrong index
        "Chemistry First Semester",
        "Chemistry Second Semester",
        "AP Chemistry",
    ]:
        for iframe_tag in soup.find_all("iframe"):
            # Iterate over all <iframe> tags on the webpage and append them to empty url list
            list_of_urls_on_page.append([iframe_tag.get("src"), iframe_tag.text])

        for a_tag in soup.find_all("a"):
            # Iterate over all <a> tags on the webpage and append them to empty url list
            list_of_urls_on_page.append([a_tag.get("href"), a_tag.text])

    else:
        for a_tag in soup.find_all("a"):
            list_of_urls_on_page.append([a_tag.get("href"), a_tag.text])

    # print("---------------------------- beginning of iteration")
    # print(metadata)
    # print(count, metadata["title"], " - ", metadata["url"])
    # count = count + 1
    # print("---------------------------- end of iteration")


    docIteration = dominate.document(title = metadata['title'])

    with docIteration:
        h1("I am the list for " + metadata['title'])
        with div(id='resourceList').add(ul()):
            for urlItem in list_of_urls_on_page[metadata["first_index"] : metadata["last_index"]]:
                li(a(urlItem[1], href='%s' % urlItem[0]))

    print(docIteration)
    createPrintLines()

    with open(htmlFilesFolder + f"/data_{metadata['title']}.html", "w", newline="") as file:
        # merge two lists arr1 + arr2
        file.write(docIteration.render())
