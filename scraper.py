import pandas as pd
from bs4 import BeautifulSoup
import requests
from googlesearch import search

URL = "https://www.ncsasports.org/mens-soccer/division-3-colleges"


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
page = requests.get(URL, headers=header)

soup = BeautifulSoup(page.content, 'html.parser')



college_items = soup.find_all('div', itemprop='itemListElement')

names = []
cities = []
states = []

for college in college_items:
    names.append(college.find('div', itemprop='name').text.strip())
    try:
        cities.append(college.find('span', itemprop='addressLocality').text.strip())
    except:
        cities.append("No City Found")
    states.append(college.find('span', itemprop='addressRegion').text.strip())

niche_query = 'https://www.niche.com/colleges/'

cookies = {
    'xid': '92a7f95d-8797-4f81-8be3-788a50016ede',
    'experiments': 'profile_sticky_header_cta%7Ccontrol%5E%5E%5E%240%7C1%5D',
    '_pxhd': '99WYxzlEJL/to9fe1ItDfTsGstFstJEiXK4eEjBI7YKWS9s6KQ0aSuGZs/h8AheGOQUYH4vNBidH6YIAdke69Q==:tD3rOiiRuUGo7a4n96ZBF/FyHqk2oKkGaT2vZmwLphRD8MkNBTzyBmW7pahUhPP1ORiGkCC6gPuTltxN1RchWbz8PiLJqENx2wgpqWIGh7o=',
    'pxcts': '4b25a2ca-dafd-11ec-a040-486f66505569',
    '_pxvid': '4abd6ff2-dafd-11ec-a457-704654427943',
    'navigation': '%7B%22location%22%3A%7B%22guid%22%3A%2227966205-db74-44e6-8d2d-79a4df61742a%22%2C%22type%22%3A%22State%22%2C%22name%22%3A%22Kentucky%22%2C%22url%22%3A%22kentucky%22%7D%2C%22navigationMode%22%3A%22full%22%2C%22vertical%22%3A%22colleges%22%2C%22mostRecentVertical%22%3A%22colleges%22%2C%22suffixes%22%3A%7B%22colleges%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22graduate-schools%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22k12%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22places-to-live%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22places-to-work%22%3A%22%2Fs%2Fkentucky%2F%22%7D%7D',
    'recentlyViewed': 'entityHistory%7CentityName%7CCentre%2BCollege%7CentityGuid%7C256bfe72-bef3-4a32-accd-91c9306baad9%7CentityType%7CCollege%7CentityFragment%7Ccentre-college%7CCarnegie%2BMellon%2BUniversity%7Cd8a17c0f-cc25-4d2a-b231-0303ea016427%7Ccarnegie-mellon-university%7CAmherst%2BCollege%7C127ec524-4bac-4a5c-a7f5-1ead9c309f44%7Camherst-college%7CsearchHistory%7CKentucky%7C27966205-db74-44e6-8d2d-79a4df61742a%7CState%7Ckentucky%7CPennsylvania%7C53fbb7b5-6943-466d-b2f1-f55c3ef2ce81%7Cpennsylvania%7CMassachusetts%7Ce08f5e71-b74a-4e28-ac28-8b4569dd5eef%7Cmassachusetts%5E%5E%5E%240%7C%40%241%7C2%7C3%7C4%7C5%7C6%7C7%7C8%5D%7C%241%7C9%7C3%7CA%7C5%7C6%7C7%7CB%5D%7C%241%7CC%7C3%7CD%7C5%7C6%7C7%7CE%5D%5D%7CF%7C%40%241%7CG%7C3%7CH%7C5%7CI%7C7%7CJ%5D%7C%241%7CK%7C3%7CL%7C5%7CI%7C7%7CM%5D%7C%241%7CN%7C3%7CO%7C5%7CI%7C7%7CP%5D%5D%5D',
}

headers = {
    'authority': 'www.niche.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'xid=92a7f95d-8797-4f81-8be3-788a50016ede; experiments=profile_sticky_header_cta%7Ccontrol%5E%5E%5E%240%7C1%5D; _pxhd=99WYxzlEJL/to9fe1ItDfTsGstFstJEiXK4eEjBI7YKWS9s6KQ0aSuGZs/h8AheGOQUYH4vNBidH6YIAdke69Q==:tD3rOiiRuUGo7a4n96ZBF/FyHqk2oKkGaT2vZmwLphRD8MkNBTzyBmW7pahUhPP1ORiGkCC6gPuTltxN1RchWbz8PiLJqENx2wgpqWIGh7o=; pxcts=4b25a2ca-dafd-11ec-a040-486f66505569; _pxvid=4abd6ff2-dafd-11ec-a457-704654427943; navigation=%7B%22location%22%3A%7B%22guid%22%3A%2227966205-db74-44e6-8d2d-79a4df61742a%22%2C%22type%22%3A%22State%22%2C%22name%22%3A%22Kentucky%22%2C%22url%22%3A%22kentucky%22%7D%2C%22navigationMode%22%3A%22full%22%2C%22vertical%22%3A%22colleges%22%2C%22mostRecentVertical%22%3A%22colleges%22%2C%22suffixes%22%3A%7B%22colleges%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22graduate-schools%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22k12%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22places-to-live%22%3A%22%2Fs%2Fkentucky%2F%22%2C%22places-to-work%22%3A%22%2Fs%2Fkentucky%2F%22%7D%7D; recentlyViewed=entityHistory%7CentityName%7CCentre%2BCollege%7CentityGuid%7C256bfe72-bef3-4a32-accd-91c9306baad9%7CentityType%7CCollege%7CentityFragment%7Ccentre-college%7CCarnegie%2BMellon%2BUniversity%7Cd8a17c0f-cc25-4d2a-b231-0303ea016427%7Ccarnegie-mellon-university%7CAmherst%2BCollege%7C127ec524-4bac-4a5c-a7f5-1ead9c309f44%7Camherst-college%7CsearchHistory%7CKentucky%7C27966205-db74-44e6-8d2d-79a4df61742a%7CState%7Ckentucky%7CPennsylvania%7C53fbb7b5-6943-466d-b2f1-f55c3ef2ce81%7Cpennsylvania%7CMassachusetts%7Ce08f5e71-b74a-4e28-ac28-8b4569dd5eef%7Cmassachusetts%5E%5E%5E%240%7C%40%241%7C2%7C3%7C4%7C5%7C6%7C7%7C8%5D%7C%241%7C9%7C3%7CA%7C5%7C6%7C7%7CB%5D%7C%241%7CC%7C3%7CD%7C5%7C6%7C7%7CE%5D%5D%7CF%7C%40%241%7CG%7C3%7CH%7C5%7CI%7C7%7CJ%5D%7C%241%7CK%7C3%7CL%7C5%7CI%7C7%7CM%5D%7C%241%7CN%7C3%7CO%7C5%7CI%7C7%7CP%5D%5D%5D',
    'if-none-match': 'W/"2de4c-XAiml01KSw/dtTg/1elHhEVVEkw"',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}


sat_scores = []
acceptance_rates = []
for name in names:
    
    name = name.replace(' ', '-')
    print(name)

    try:
        search = requests.get(niche_query + name, headers=headers, cookies=cookies)
        s = BeautifulSoup(search.content, 'html.parser')

        vals = s.find_all('div', 'scalar__value')

        if len(vals) == 0:
            input("Type Something after Completing the CAPTCHA")


            search = requests.get(niche_query + name, headers=headers, cookies=cookies)
            s = BeautifulSoup(search.content, 'html.parser')

            vals = s.find_all('div', 'scalar__value')

        html = str(vals)
        acc_index = html.find('%')
        sat_index = html.find('-')

        acceptance_rate = html[acc_index-2:acc_index]
        sat_score = html[sat_index-4:sat_index+5]

        acceptance_rates.append(acceptance_rate)
        sat_scores.append(sat_score)
    except:
        acceptance_rates.append('None Found')
        sat_scores.append('None Found')

        
colleges = {
    'College Name': names,

    'City': cities,

    'State': states,

    'SAT Range': sat_scores,

    'Acceptance Rates': acceptance_rates
}

df = pd.DataFrame(colleges)

df.to_csv('college.csv')

# college_locations = []
# for ind, city in enumerate(college_cities):
#     college_locations.append(f'{city.text.strip()}, {college_states[ind].text.strip()}')

# print(college_locations)
