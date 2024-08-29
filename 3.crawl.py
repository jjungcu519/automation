import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=0&BizJobtype_Bctgr_Name=%EC%A7%81%EB%AC%B4+%EC%A0%84%EC%B2%B4&BizJobtype_Code=0&BizJobtype_Name=%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth1=on'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')

company = soup.select('div.coTit > a > b')
# title = soup.select('ol > li:nth-child(1) > div.info > div.tit > a > span')
# roll = soup.select('ol > li:nth-child(1) > div.info > div.sTit')
# hire_type = soup.select('ol > li:nth-child(1) > div.info > div.sDsc > span:nth-child(4)')
# due_date = soup.select('ol > li:nth-child(1) > div.side > span.day')

print(company.text)
# print(title.text)
# print(roll.text)
# print(hire_type.text)
# print(due_date.text)

