import requests
from bs4 import BeautifulSoup
import re

cookies = {
    'PHPSESSID': 'e5027dc55693910e5ca64eeaf8f97baa',
    'TS01262d1d': '01b485afe5bb58c0d79190366affbba202845db187ab95e060a14dbd9ba44e783fcffdce0368392d4a04627fc9f67b02a49878d0d00dd831919c92933b7da1fc12cdb4a2fe',
    '_ga': 'GA1.2.1275637127.1665180282',
    '_gid': 'GA1.2.1418242435.1665180282',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
}

data = {
    'g-recaptcha-response-rit': '03AIIukzh0f0MMNhWK3xk94zdCLzlKD1t54PKigjCrrv3Q4MOk_KwNO5lmQ27D996XfGxL5bXJb3I1XVdJBZ9tGaTmDJBrqN_Wx6iaSUlgRwFh4o11qcOEOk03lr6N7yxiYpd2KO-fe_deDrFOpwueIaG1DXeSEtvE1ST1CaRgd2glP6KPNzsO9WqG_7pde1S6Qp1RXENwezSdFmdtFADiBc48V6dChwFoPyUpfymgywxX49lU7rrWzzFaLOfk1I-BeJK20CkBk8tgaTyuvI0ZRKM9f_DFs92QX9_isuU2zpDGwSFGhWdQy7IbnAgZ6tEoSpRyawuGj2egsLMAj1bXi5H44HGUUK9E3XOzWLodvR8UbShE3_h8NjO7AY90NkAs7ErX5VGejnyfCubbw7W1Y7PGWqy_U16n6JArhXvVPqxubfqXpkJ4uQ05Y19wtOwrR6SR-a4vdWAuxN5i3p90S9Zzam61yuqb-HbTqP-wwBALlNsfTj9IfDU897ggFJjpZcpu1dVKR2OfhNbsalQ29sHM8xslKaQZ8MjjWH7DW5TsAITV_wJvMnA',
    'action': 'validate_captcha_rit',
    'competencia': '3',
    'conCorte': '90',
    'conTribunal': '0',
    'conTipoBusApe': '0',
    'radio-groupPenal': '1',
    'conTipoCausa': 'C',
    'radio-group': '1',
    'conRolCausa': '123',
    'conEraCausa': '2022',
    'ruc1': '',
    'ruc2': '',
    'rucPen1': '',
    'rucPen2': '',
    'conCaratulado': '',
}

response = requests.post('https://oficinajudicialvirtual.pjud.cl/ADIR_871/civil/consultaRitCivil.php', cookies=cookies, headers=headers, data=data)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all("tr")
print(f"Total de registrol {len(rows)}")
for row in rows:
    try:
        dtaCausa = row.find("a").get('onclick')
        #print(dtaCausa)
        print(re.search(r'\((.*?)\)',dtaCausa).group(1))
    except:
        pass

