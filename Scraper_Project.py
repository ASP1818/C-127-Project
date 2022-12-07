from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
brower = webdriver.Chrome("/users/satis/download/C-127 Project")
brower.get(start_url)
time.sleep(10)
def scrape():
    header = ["Name", "Distace", "Mass", "Radius"]
    Brightest_stars = []
    for i in range(0, 428):
        soup = BeautifulSoup(brower.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "Brighteststars"}):
            li_tags = ul_tag.find_all("li"):
            temp_list = []
            for index, li_tags in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tags.find_all("a" [0].contents [0]))
                else: 
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            Brightest_stars.append(temp_list)
        brower.find_elment_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("", "w")as f:
        csvwriter = csv.writer(f)