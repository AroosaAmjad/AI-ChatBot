from requests_html import HTMLSession

def weather():

    s = HTMLSession()
    query = "Lahore"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})
    temp = r.html.find('span#wob_tm', first= True).text


    # Find the unit element
    unit_element = r.html.find('div.vk_bk.wob_unit span.wob_t', first=True)
    if unit_element:
        unit = unit_element.text
        
    else:
        print("Unit not found")
    desc = r.html.find('span#wob_dc', first= True).text

    return temp+" "+unit+" "+desc