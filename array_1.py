# This code is for web scraping. It iterates over a list of class resources, makes HTTP requests to their respective URLs, parses the HTML content, extracts URLs based on the title, and writes the extracted data into separate JSON files for each class resource.


from bs4 import BeautifulSoup
import json
import requests

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
    "title": "Apologetics",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/apologetics/",
}
class_resources.append(class_resource_metadata_1)


#Pre-calc webpage
class_resource_metadata_2A1 = {
    "title": "Pre-Calc Chapters",
    "url": "https://www.stmonicaacademy.com/pre-calculus/",
}
class_resources.append(class_resource_metadata_2A1)

# Pre-calc chapters
class_resource_metadata_2 = {
    "title": "Pre-Calc Chapter 1",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-1/",
}
class_resources.append(class_resource_metadata_2)


# Pre-calc chapters
class_resource_metadata_2A = {
    "title": "Pre-Calc Chapter 2",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-2/",
}
class_resources.append(class_resource_metadata_2A)


# Pre-calc chapters
class_resource_metadata_2B = {
    "title": "Pre-Calc Chapter 3",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-3/",
}
class_resources.append(class_resource_metadata_2B)


# Pre-calc chapters
class_resource_metadata_2C = {
    "title": "Pre-Calc Chapter 4",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-4/",
}
class_resources.append(class_resource_metadata_2C)


# Pre-calc chapters
class_resource_metadata_2D = {
    "title": "Pre-Calc Chapter 5",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-5/",
}
class_resources.append(class_resource_metadata_2D)


# Pre-calc chapters
class_resource_metadata_2E = {
    "title": "Pre-Calc Chapter 6",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-6/",
}
class_resources.append(class_resource_metadata_2E)


# Pre-calc chapters
class_resource_metadata_2F = {
    "title": "Pre-Calc Chapter 7",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-7/",
}
class_resources.append(class_resource_metadata_2F)


# Pre-calc chapters
class_resource_metadata_2G = {
    "title": "Pre-Calc Chapter 8",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-8/",
}
class_resources.append(class_resource_metadata_2G)


# Pre-calc chapters
class_resource_metadata_2H = {
    "title": "Pre-Calc Chapter 9",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-9/",
}
class_resources.append(class_resource_metadata_2H)


# Pre-calc chapters
class_resource_metadata_2I = {
    "title": "Pre-Calc Chapter 10",
    "url": "https://www.stmonicaacademy.com/pre-calculus/pre-calc-chapter-10/",
}
class_resources.append(class_resource_metadata_2I)


# AP Chemistry
class_resource_metadata_3 = {
    "title": "AP Chemistry",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/ap-chemistry/",
}
class_resources.append(class_resource_metadata_3)


# Computer Science
class_resource_metadata_4 = {
    "title": "Computer Science",
    "url": "https://www.stmonicaacademy.com/computer-science/",
}
class_resources.append(class_resource_metadata_4)


# Physics link to semester 1
class_resource_metadata_5 = {
    "title": "Physics First Semester",
    "url": "https://www.stmonicaacademy.com/physics/first-semester/",
}
class_resources.append(class_resource_metadata_5)


# Physics link to semester 2
class_resource_metadata_5A = {
    "title": "Physics Second Semester",
    "url": "https://www.stmonicaacademy.com/physics/second-semester/",
}
class_resources.append(class_resource_metadata_5A)


# Latin
class_resource_metadata_6 = {
    "title": "Latin",
    "url": "https://www.stmonicaacademy.com/latin/",
}
class_resources.append(class_resource_metadata_6)


# Calculus
class_resource_metadata_7 = {
    "title": "Calculus",
    "url": "https://www.stmonicaacademy.com/calculus/",
}
class_resources.append(class_resource_metadata_7)


# Chemistry link to semester 1
class_resource_metadata_8 = {
    "title": "Chemistry First Semester",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/chemistry-first-chapter/",
}
class_resources.append(class_resource_metadata_8)


# Chemistry link to semester 2
class_resource_metadata_8A = {
    "title": "Chemistry Second Semetester",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/chemistry-second-chapter/",
}
class_resources.append(class_resource_metadata_8A)


# English link to medievel literature
# This webpage has no links on it
class_resource_metadata_9 = {
    "title": "English Medieval Literature",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/medieval-literature/",
}
class_resources.append(class_resource_metadata_9)


# English link to ancient literature
# This webpage has no links on it
class_resource_metadata_9A = { 
    "title": "English Ancient Literature",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/ancient-literature/",
}
class_resources.append(class_resource_metadata_9A)


# Geometry webpage
class_resource_metadata_10 = {
    "title": "Geometry",
    "url": "https://www.stmonicaacademy.com/geometry/",
}
class_resources.append(class_resource_metadata_10)


# Geometry link to book one
class_resource_metadata_10A = {
    "title": "Geometry Book One",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-one/",
}
class_resources.append(class_resource_metadata_10A)


# Geometry link to two
class_resource_metadata_10B = {
    "title": "Geometry Book Two",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-two/",
}
class_resources.append(class_resource_metadata_10B)


# Geometry link to book three
class_resource_metadata_10C = {
    "title": "Geometry Book Three",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-three/",
}
class_resources.append(class_resource_metadata_10C)


# Geometry link to book four
class_resource_metadata_10D = {
    "title": "Geometry Book Four",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-four/",
}
class_resources.append(class_resource_metadata_10D)


# Geometry link to book five
class_resource_metadata_10E = {
    "title": "Geometry Book Five",
    "url": "https://www.stmonicaacademy.com/student-parents/class-resources/geometry/book-five/",
}
class_resources.append(class_resource_metadata_10E)


count = 1

# Print the array using a for loop
for metadata in class_resources:
    # Code that does parsing stuff
    page = requests.get(metadata["url"], cookies=cookies)
    print(page.text)

    soup = BeautifulSoup(page.text, "html.parser")

    # Initialize an empty list to store URLs
    list_of_urls_on_page = []
    # list_of_urls_on_page_a = []
    #list_of_urls_on_page_iframe = []
  

    # Find all elements with class "middle div"
    middle_inner_elements = soup.find_all(class_="middle_inner")


    # Iterate over middle div elements
    for div in middle_inner_elements:
        # Find all anchor tags within the middle div
        anchor_tags = div.find_all("a")
        # Extract href attributes from anchor tags and append to the list
        for tag in anchor_tags:
            href = tag.get("href")
            if href:
                list_of_urls_on_page.append(href)

        # Find all iframe tags within the middle div
        iframe_tags = div.find_all("iframe")
        # Extract src attributes from iframe tags and append to the list
        for tag in iframe_tags:
            src = tag.get("src")
            if src:
                list_of_urls_on_page.append(src)
    


    print("---------------------------- beginning of iteration")
    print(metadata)
    print(count, metadata["title"], " - ", metadata["url"])
    count = count + 1
    print("---------------------------- end of iteration")
    with open(f"data_{metadata['title']}.json", "w", newline="") as file:
        # merge two lists arr1 + arr2
        file.write(json.dumps(list_of_urls_on_page))
