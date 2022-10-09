import requests
from bs4 import BeautifulSoup

cookies = {
    'PHPSESSID': 'e5027dc55693910e5ca64eeaf8f97baa',
    'TS01262d1d': '01b485afe510c475c69f159ec1a887bb79515585927ed87eda375b3b36a0cd5f5a61f247a5292d8fad2fdd451b5df607cfcf668eb8c7d0dee6a820c9feb80fc87ff5a8dbb7',
    '_ga': 'GA1.2.1275637127.1665180282',
    '_gid': 'GA1.2.1418242435.1665180282',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://oficinajudicialvirtual.pjud.cl',
    'Connection': 'keep-alive',
    'Referer': 'https://oficinajudicialvirtual.pjud.cl/indexN.php',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=e5027dc55693910e5ca64eeaf8f97baa; TS01262d1d=01b485afe510c475c69f159ec1a887bb79515585927ed87eda375b3b36a0cd5f5a61f247a5292d8fad2fdd451b5df607cfcf668eb8c7d0dee6a820c9feb80fc87ff5a8dbb7; _ga=GA1.2.1275637127.1665180282; _gid=GA1.2.1418242435.1665180282',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = {
    'dtaCausa': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvb2ZpY2luYWp1ZGljaWFsdmlydHVhbC5wanVkLmNsIiwiYXVkIjoiaHR0cHM6XC9cL29maWNpbmFqdWRpY2lhbHZpcnR1YWwucGp1ZC5jbCIsImlhdCI6MTY2NTI3NTMxNywiZXhwIjoxNjY1Mjc3MTE3LCJkYXRhIjp7ImNvZGlnb1RyaWJ1bmFsIjoiMjYxIiwiY3JyQ2F1c2EiOiIyNzY4MjMxNCIsImNvbW9kaW4iOjAsImNycklkQ3VhZGVybm8iOiIzNTE4NDc1NiIsImNvZFRpcEN1YWRlcm5vIjoiMSIsInJvbENhdXNhIjoiMTIzIiwidGlwb0NhdXNhIjoiQyIsImVyYUNhdXNhIjoiMjAyMiIsImZsZ19hbm9uaW1pemFjaW9uIjoiMCJ9fQ.FbA1QBJE36t2Frc26vOdHx-kNw3qLe1Dk_L0h3MEipU',
    #'tokenCaptcha': '03AIIukzgb8tJEn2j8xHBG-ChkQm2C_lQfMKk98-FnwZJknIlD6YE7RNCjRT1EEy2Ya-Q6NT2sG6s4HZT3w1D9OoakDfMdxgYZkrn-Ogxk32hqglb2tbT97wPTVYYHy7s5A7EIkL-O91XndJ5YMlYotEDxrbseeM4-YXqPCp1J5u2pAJ2hZ4s5ESqBYbIS7XCK5lSNBscdjmHtlDiXiCqnSvsM7NCLny3zE75PXK5ItRSMYDVXmpHWSoWIyFy7n--ixV25tLBYFe30d_g2vhG0rmcqA0M-5Pja5moZRlfKAklhpXkUIjRvXRBQwLH4Hs0ik30foclwBPZn-sxCw_gF1xZq_oiSgXd47oO6PaNpSoyyw69jhX9LrATRquiu6a9AgkpquMy4TXsofVQZtJJCa0XrTdq57ftgODQDzDgxexKveXIGTTAKNlmHLc890llkNjQ8elUdf43ASiWa33L3xTF5lcKVQwNrrWEFYK131JGxP-6ML_aSGeEvR3T1a6soIgjZb5YuqoSoaGNILgdab3MR5ogZyZFqfFV77Qf13xVtIY9Snydfj74',
}

response = requests.post('https://oficinajudicialvirtual.pjud.cl/ADIR_871/civil/modal/causaCivil.php', cookies=cookies, headers=headers, data=data)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find("div", {"class":"table-responsive"})
print(table)