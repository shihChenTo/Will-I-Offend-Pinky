# encoding: utf-8

from bs4 import BeautifulSoup
import requests
import time
import os
import re
import codecs
import json

start_time_str = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
os.mkdir(start_time_str)

headers = {
    "Accept-Language": "zh-CN"
}

# words_list = ["中国", "中华人民共和国", "中华民国", "美国", "日本", "中日", "中美", "国民党", "抗日", "日军", "侵华",
#               "不平等条约", "清", "大屠杀", "公祭日", "反法西斯"]
words_list = ["抗日", "日军", "侵华", "不平等条约", "大屠杀", "公祭日", "反法西斯"]
person_list = ["毛泽东", "毛岸英"]


months_template = "https://zh.wikipedia.org/wiki/Template:%E6%9C%88%E4%BB%BD"
r = requests.get(months_template, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

days_urls = []

for tr in soup.tbody.find_all("tr")[5:]:
    for day in tr.find_all("li"):
        days_urls.append("https://zh.wikipedia.org" +
                         day.a.get('href'))

total_json = {}
result_json = {}
for day in days_urls:
    r = requests.get(day, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser').find(id="content")
    date = soup.find(id="firstHeading").get_text()
    print(date)
    # body_content = soup.find(id="bodyContent")
    # while body_content.table is not None:
    #     body_content.table.extract()
    day_result_json = {}
    day_total_json = {}

    body_text = soup.find(class_="mw-parser-output")
    while body_text.table is not None:
        body_text.table.extract()
    body_text.find("div", id="toc").extract()
    current_category = ""
    for line in body_text.find_all(["h2", "li"]):
        if(line.find("span", class_="mw-headline") is not None):
            current_category = line.find(
                "span", class_="mw-headline").get_text()
            if(current_category not in ["大事记", "出生", "逝世", "节假日和习俗", "节日与纪念日"]):
                break
            # print(current_category)
            if(current_category in ["节假日和习俗", "节日与纪念日"]):
                current_category = "节假日和习俗"
            day_total_json[current_category] = []
            day_result_json[current_category] = []
        else:
            search_list = []
            for a in line.find_all("a"):
                if(re.search("^.*[0-9]+年$", a.get_text()) is None):
                    a.replace_with("[[" + a.get_text() + "]]")
                if(re.search("^[.*?]$", a.get_text()) is not None):
                    a.replace_with("")
                # search_word = a.get_text()
                # if search_word not in search_list and re.search("^.*[0-9]+年$", search_word) is None:
                #     search_list.append(a.get_text())
            content = line.get_text()
            content = re.sub('\s', ' ', content)
            # content = content.replace(" ", "")
            # content = content.replace("\t", "")
            # for search_word in search_list:
            #     content = content.replace(search_word, "[[" +
            #                               search_word + "]]")
            day_total_json[current_category].append(content)

            if re.search("^.*[0-9]+年.*$", content) is not None:
                # Sometimes may be sub <li> under a year, so use "^.*[0-9]+年.*$"
                if current_category in ["大事记", "节假日和习俗", "节日与纪念日"]:
                    for word in words_list:
                        if content.find(word) != -1:
                            day_result_json[current_category].append(content)
                            break
                if current_category in ["出生", "逝世"]:
                    for word in person_list:
                        if content.find(word) != -1:
                            day_result_json[current_category].append(content)
                            break

    copied = day_result_json.copy()
    for key, value in copied.items():
        if value == []:
            del day_result_json[key]

    f = codecs.open(os.path.join(start_time_str, date + ".json"), "w", "utf-8")
    f.write(json.dumps(day_result_json, indent=2, ensure_ascii=False))
    f.close()
    f = codecs.open(os.path.join(
        start_time_str, date + "_total.json"), "w", "utf-8")
    f.write(json.dumps(day_total_json, indent=2, ensure_ascii=False))
    f.close()

    total_json[date] = day_total_json
    result_json[date] = day_result_json

    time.sleep(3)

f = codecs.open(os.path.join(start_time_str, "total.json"), "w", "utf-8")
f.write(json.dumps(total_json, indent=2, ensure_ascii=False))
f.close()

f = codecs.open(os.path.join(start_time_str, "result.json"), "w", "utf-8")
f.write(json.dumps(result_json, indent=2, ensure_ascii=False))
f.close()
