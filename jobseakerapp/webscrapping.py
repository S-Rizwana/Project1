import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd

url = 'https://internshala.com/job/detail/remote-customer-success-representative-fresher-jobs-at-uability1670311470'

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

name=soup.find('div', class_="detail_view")


title=soup.find('span', attrs={'class':'profile_on_detail_page'}).get_text()
company=soup.find('a', attrs={'class':'link_display_like_text view_detail_button'}).get_text()

details_companylinksrc=soup.find('div', attrs={'class':'text-container website_link'})
details_companylink = details_companylinksrc.find('a').get('href')
details_companylinktext = details_companylinksrc.find('a').get_text()

logosrc=soup.find('div', attrs={'class':'internship_logo'})
logo = logosrc.find('img').get('src')
location=soup.find('p', attrs={'id':'location_names'}).get_text()
internshipdetails=soup.find('div', attrs={'class':'other_detail_item_row'}).get_text()
tags=soup.find('div', attrs={'class':'tags_container_outer'}).get_text()
details=soup.find('div', attrs={'class':'internship_details'})
details_about_company_title=soup.find('div',attrs={'class':'section_heading heading_5_5'}).get_text()
details_about_company=soup.find('div',attrs={'class':'text-container about_company_text_container'}).get_text()
details_company_activity=soup.find('div',attrs={'class':'activity_section'}).get_text()
job_details=""
for i in details.find_all('div',attrs={'class':"text-container"})[2:3]:
    # print(i)
    job_details += i.text
skills_required = soup.find('div',attrs={'class':'round_tabs_container'}).get_text()
salary = soup.find('div',attrs={'class':'text-container salary_container'}).get_text()
print(job_details.strip())

