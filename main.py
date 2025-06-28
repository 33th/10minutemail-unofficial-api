import requests
from bs4 import BeautifulSoup

last = ""

def newEmail():
    global email
    url = "https://10minute-mail.org/changemail"
    payload = { "forcechange": False }
    headers = {
        "host": "10minute-mail.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.5",
        "accept-encoding": "gzip, deflate, br, zstd",
        "referer": "https://10minute-mail.org/",
        "content-type": "application/json",
        "requestverificationtoken": "CfDJ8MRmxKmQpXxCkE0cDwfYvfAt405QYqDJm7nJcmFmV-cvdDixo5QlELAiNFeJSFqVlS6vFvydJDsepTsmVFVtnRY6OeUfxcm3jJ-Kyl0LISEFHUtuNkW5_jbGGewIOnWLH7c01ipri6d74m5b1RQa-ME",
        "origin": "https://10minute-mail.org",
        "connection": "keep-alive",
        "cookie": "cf_clearance=jPnD7E6ZWch0Fv.YaRK9PlqwvVsaDGDtEfZJ3AoZ_P0-1751073936-1.2.1.1-5SPv2gRAENApvjcL1.54jjxI.nbydtAW1mzSU58Zj0Z8megKGkU21mZlrm3_Uel50voznKgXVc2gkCyuaeFwwweSLrkTfcBuJQ3dwyqpliNaonncQW50LvU1lXoH3ZCGfDRN3RRskJKhs6Iea3g37sAXnphP0MemeSs7HJ2xVDUN5hCIRC1jBjQhPkEPyHtVrkqUrrqICtXqR4jnPj0PTpqlricscEh1smdFbp6E6fZWigFQ8_xiKGGYr1ao5L6oNzq95Yw63AGeqMbgeeAllk2NSktLzWLd2eGBvPwAI.1cNRy4gYMKpw2V34giDZW9AAESFR8JJx7dN0BM1wIqFBNatAxauWybWdyU9VBgA1KGOy4JXk9g3NguG5SAWZY5; .AspNetCore.Antiforgery.aVVGZX7w6h0=CfDJ8MRmxKmQpXxCkE0cDwfYvfA9Ts8LPRoJ90-6QPwdx9ww_bDqFvHay2woYDHQfDMJDpxyMXt0PrbQLOkQHJgWmEU_M4Q0l3TtAeqNk3SBUqPPb3u9lyyVxhwXX_IW7_PRKJriuDKqFHaGDLS3hQPVHsc",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "priority": "u=4"
    }
    response = requests.post(url, json=payload, headers=headers)
    email = response.text.strip('"')
    print("\n" + "="*30)
    print("Your temporary email is:")
    print(email)
    print("="*30 + "\n")

def refreshMailbox():
    global last
    url = "https://10minute-mail.org/"
    payload = { "mail": f"{email}" }
    headers = {
        "host": "10minute-mail.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.5",
        "accept-encoding": "gzip, deflate, br, zstd",
        "referer": "https://10minute-mail.org/",
        "content-type": "application/json",
        "requestverificationtoken": "CfDJ8MRmxKmQpXxCkE0cDwfYvfDHqDt3nx5B2qoDDRH7kDn-WQPrTvgTwjx8W9EhjW89SHbiC2Rv1LVCSp6MxBtXc7kzyaDgcVtDvYWq0Uhz8r30IDGBNx_20XEZ9sl5zNLktejZmbfbU4i0mQR6BmcfnxI",
        "origin": "https://10minute-mail.org",
        "connection": "keep-alive",
        "cookie": "cf_clearance=ni0iX7GhQp5a5lSqdbQSzK5Kd2eeHmRxMGocREXlaOw-1751092077-1.2.1.1-5bUY9f9gCUG8nBvomWWEpr4NPXJO4z97Mj8OFJ8_fjNEfY1GCLxCplRZZrDeLZC14XBWG_EJqZcjSnEo7MkKL4gSo.Q11JJdX_X2g4K_OiPz7ZGHeYsHXnj_f7Qqn_Id4U6Ug31J5INe_GvIpN3mpjhmKSUqgS76v6xIBXr0LQGS0ROUgZFLCWu_ihQtB45ehSncJmjcKR.ThpW7YwySuE4aQMtnAk5RFohmJft4ykqeKW20HpGwsJeBbl0rFXCgMtF_wGdJSrKScS9btQeNoNuqqn59VXCr3w03p6Ln1TwxXMzWgXDrjvDPNIhGgHF9sRnd955IRDZllwsE4nSsTkrf2oYcKg2UndulS8qArXusBg2VW69dumSd6R3cs578; .AspNetCore.Antiforgery.aVVGZX7w6h0=CfDJ8MRmxKmQpXxCkE0cDwfYvfBEKKlv_c_ZO3ev4nXPcK86ZSyaMOEhzioE9oxL7BFT_VkP9xGioRqMzjT3chtwPpvTFDQ_PqFLiaRK8iDoD5OAO4xNybX3rSWtBAvJKEbekTtk7dYq3E1UlSELw375P5k",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "priority": "u=4"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.text == "[]":
        print("\n[Mailbox is empty]\n")
    else:
        mail = response.json()
        mailID = mail[0]['id']
        if mailID != last:
            last = mailID
            url = "https://10minute-mail.org/loadfull"
            payload = { "id": f"{mailID}" }
            headers["requestverificationtoken"] = "CfDJ8MRmxKmQpXxCkE0cDwfYvfDHqDt3nx5B2qoDDRH7kDn-WQPrTvgTwjx8W9EhjW89SHbiC2Rv1LVCSp6MxBtXc7kzyaDgcVtDvYWq0Uhz8r30IDGBNx_20XEZ9sl5zNLktejZmbfbU4i0mQR6BmcfnxI"
            response = requests.post(url, json=payload, headers=headers)
            fullMail = response.json()
            print("\n" + "-"*30)
            print("New email received")
            print("-"*30)
            print(f"ID:      {fullMail.get('id')}")
            print(f"From:    {fullMail.get('from')}")
            print(f"To:      {fullMail.get('to')}")
            print(f"Date:    {fullMail.get('date')}")
            print(f"Subject: {fullMail.get('subject')}")
            print("-"*30)
            print("Body (text):")
            print(fullMail.get('textBody'))
            print("-"*30 + "\n")
            soup = BeautifulSoup(fullMail.get('htmlBody', ''), 'html.parser')
            print("Body (HTML):")
            print(soup.prettify())
            print("-"*30 + "\n")
            with open(f"{mailID}.html", 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            print(f"HTML saved to: {mailID}.html\n")
        else:
            print("\n[No new emails]\n")

while True:
    print("\n" + "*"*30)
    print("10 Minute Mail")
    print("*"*30)
    print("1) Generate new email")
    print("2) Refresh mailbox")
    print("3) Exit")
    print("*"*30 + "\n")
    menu = input("Choose an option [1-3]: ")
    if menu == "1":
        newEmail()
    elif menu == "2":
        refreshMailbox()
    elif menu == "3":
        break
    else:
        print("\nInvalid option, please try again.\n")
