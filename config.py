main_url = 'https://www.kinopoisk.ru/'
url_api = 'https://api.kinopoisk.dev/v1.4/'
api_key = "SZYY5ED-NFMM9H2-G5X24J1-24AG3ZJ"
HEADERS = {
    "accept": "application/json",
    "X-API-KEY": "SZYY5ED-NFMM9H2-G5X24J1-24AG3ZJ"
}
cookie_string = 'yuidss=2493407331712159667; yandexuid=2493407331712159667; yashr=6845934701712159667; ymex=2027519668.yrts.1712159668; _ym_uid=1712159669924316716; bh=EkAiR29vZ2xlIENocm9tZSI7dj0iMTIzIiwgIk5vdDpBLUJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMjMiGgUieDg2IiIPIjEyMS4wLjYxNjcuODYiKgI/MDoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJaIk5vdCBBKEJyYW5kIjt2PSI5OS4wLjAuMCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMS4wLjYxNjcuODYiLCJDaHJvbWl1bSI7dj0iMTIxLjAuNjE2Ny44NiIi; amcuid=2804040861718108387; gdpr=0; receive-cookie-deprecation=1; yabs-dsp=mts_banner.bUNZV0RneFVUOU8wMk9YbGp0alFydw==; _ym_d=1727947194; is_gdpr=0; is_gdpr_b=CPeCThCcpAIoAg==; i=j3d/Vvt/uIrVReeh2EJi2aIr5exV8HHHf+S+8d/LQkeFfHLHQgrHjIoc3s+SaypN9j4okzedtyQFTpJ3Die9nB15nHo=; cycada=CWDNVBv0jx5qoi43FsVIUH1vkaw9ztRAYirKoyqGb/o=; Session_id=3:1737225096.5.0.1737225096621:zFb8sg:88a6.1.2:1|2031147226.0.2.3:1737225096|3:10301473.625351.mKwxPUd7f1rCkUpPAsiQOoZSEP8; sessar=1.1198.CiDYm723ivBV3OonJX1HhZ8hTyp5yJg6nf7xiO8Ti-yJ9A.1f0GDuKs34tAP6pX7rr0sBPCBbIwkORPzOe35zbz3DM; sessionid2=3:1737225096.5.0.1737225096621:zFb8sg:88a6.1.2:1|2031147226.0.2.3:1737225096|3:10301473.625351.fakesign0000000000000000000; yandex_login=tk.sanmed@mail.ru; yabs-vdrf=Dz8jd800oAG00zsPdB00IBCa1rsPd4W3Jfem10; ys=udn.cDp0ay5zYW5tZWRAbWFpbC5ydQ%3D%3D#wprid.1737291285192038-706269233346716045-balancer-l7leveler-kubr-yp-sas-58-BAL#c_chck.2855671369; _ym_isad=2; yp=2052585096.udn.cDp0ay5zYW5tZWRAbWFpbC5ydQ%3D%3D#1739541679.hdrc.1#1737804463.szm.1_25:1536x960:994x514#1768827293.swntab.1466204631#2052651293.pcs.0#1742475285.atds.1#2052313148.multib.1#1737390208.dlp.2; bh=EkEiR29vZ2xlIENocm9tZSI7dj0iMTMxIiwgIkNocm9taXVtIjt2PSIxMzEiLCAiTm90X0EgQnJhbmQiO3Y9IjI0IhoFIng4NiIiECIxMzEuMC42Nzc4LjI2NiIqAj8wMgIiIjoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJdIkdvb2dsZSBDaHJvbWUiO3Y9IjEzMS4wLjY3NzguMjY2IiwgIkNocm9taXVtIjt2PSIxMzEuMC42Nzc4LjI2NiIsICJOb3RfQSBCcmFuZCI7dj0iMjQuMC4wLjAiWgI/MGCcwLS8Bmoe3Mrh/wiS2KGxA5/P4eoD+/rw5w3r//32D6SYzYcI'
def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies

cookies = parse_cookies(cookie_string)