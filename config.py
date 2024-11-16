import os


def get_project_root():
    # 获取根目录 不受运行目录影响
    current_dir = os.path.abspath(__file__)
    while not os.path.exists(os.path.join(current_dir, '.project_root')):
        current_dir = os.path.dirname(current_dir)
    return current_dir


rpc_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://bits.bytedance.net',
    'Pragma': 'no-cache',
    'Referer': 'https://bits.bytedance.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-Jwt-Token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYWFzLnBhc3Nwb3J0LmF1dGgiLCJleHAiOjE3MzE2NTU4NzksImlhdCI6MTczMTY1MjIxOSwidXNlcm5hbWUiOiJ6ZW5neXVodWkiLCJ0eXBlIjoicGVyc29uX2FjY291bnQiLCJyZWdpb24iOiJpMThuIiwidHJ1c3RlZCI6dHJ1ZSwidXVpZCI6ImQyNjE3OTQxLTJhMTctNDJhYi05ODczLThhM2M3NDJiMTI1NyIsInNpdGUiOiJpMThuIiwiYnl0ZWNsb3VkX3RlbmFudF9pZF9vcmciOiJieXRlZGFuY2UiLCJzY29wZSI6ImJ5dGVkYW5jZSIsInNlcXVlbmNlIjoiVGVzdCIsIm9yZ2FuaXphdGlvbiI6IlRpa1RvayDnoJTlj5Et6LSo6YeP5L-d6ZqcLeWbvemZheebtOaSrS3muLjmiI8iLCJ3b3JrX2NvdW50cnkiOiJDSE4iLCJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9zMTYtaW1maWxlLXNnLmZlaXNodWNkbi5jb20vc3RhdGljLXJlc291cmNlL3YxL3YzXzAwOGxfMDNkOWU4OGUtY2Y2Yy00MTMxLWJmOWEtOGM5YzU1YjY1M2h1fj9pbWFnZV9zaXplPW5vb3BcdTAwMjZjdXRfdHlwZT1cdTAwMjZxdWFsaXR5PVx1MDAyNmZvcm1hdD1wbmdcdTAwMjZzdGlja2VyX2Zvcm1hdD0ud2VicCIsImVtYWlsIjoiemVuZ3l1aHVpQGJ5dGVkYW5jZS5jb20iLCJlbXBsb3llZV9pZCI6MzEwNTcyOSwib2dfbGltaXQiOiJub25lIn0.Klqx5v34RVs_rxy7gFC6zHr5Dt5VTDN1dkMoHf0Jn3najN63rkRZARGNh58vULvlB-TJ8mSM_XwBmIau2UOA2bEa8ILzlshCQJMDIapd0-x5a6DRdNAxzp7DlpAhaN3lflJASwf1_DX5aRcx4lMnxm8yK6YPulu78EtTMJmfvOM',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

webcast_headers = {
    "Host": "webcast.tiktok.com",
    "Accept": "*/*",
    "Accept-Language": "zh-CN",
    "Cookie": "ttwid=1%7CwfTknI_KhNyNpN546SWEbCWVb-AxLtjzLZ0XqcAeRc4%7C1730778979%7C82366f85a73e09510614ae848a5748e97fd68baaef3a98335fee919271fb6c5f; d_ticket=ae98dffcb81c987bf3930be262ab87bc4eaef; multi_sids=7416313210217710597%3Ae45a66a9bad50ae47d7d170669f5ec83; cmpl_token=AgQQAPPdF-RO0rbS5zXOIp08_UgOGICZv5A3YNuwBQ; passport_auth_status=8b5a7c7dee9cf5b7735ebbb500a209fe%2C; passport_auth_status_ss=8b5a7c7dee9cf5b7735ebbb500a209fe%2C; store-idc=maliva; store-country-code=br; store-country-code-src=uid; tt-target-idc=useast1a; tt_chain_token=jMmPfZLO/VqyE5Pp3WUrcw==; passport_csrf_token=e59e7150afd32ae9604d671981f06060; passport_csrf_token_default=e59e7150afd32ae9604d671981f06060; sid_guard=52f84523a9800acf9eb3339a93d47cb9%7C1730779332%7C5183999%7CSat%2C+04-Jan-2025+04%3A02%3A11+GMT; uid_tt=d16fc50d0abeda2490abf46f982b5176d560e36b46b188d85d7600e5a1ed6f8a; uid_tt_ss=d16fc50d0abeda2490abf46f982b5176d560e36b46b188d85d7600e5a1ed6f8a; sid_tt=52f84523a9800acf9eb3339a93d47cb9; sessionid=52f84523a9800acf9eb3339a93d47cb9; sessionid_ss=52f84523a9800acf9eb3339a93d47cb9; sid_ucp_v1=1.0.0-KDM1NmQ0YmU2MDJkODIwOWUwNjA1ZTRhNTY1MTc2ZWFhMmEwYmM3NzUKGAiFiMGwpLKC9mYQxLGmuQYY90A4BkCACBADGgNzZzEiIDUyZjg0NTIzYTk4MDBhY2Y5ZWIzMzM5YTkzZDQ3Y2I5; ssid_ucp_v1=1.0.0-KDM1NmQ0YmU2MDJkODIwOWUwNjA1ZTRhNTY1MTc2ZWFhMmEwYmM3NzUKGAiFiMGwpLKC9mYQxLGmuQYY90A4BkCACBADGgNzZzEiIDUyZjg0NTIzYTk4MDBhY2Y5ZWIzMzM5YTkzZDQ3Y2I5; tt-target-idc-sign=ffpCeoy8tfF7Q9vKcXjYsXd6ivFwjQ18ElqUaqVuQPgZ9VgwxHuGiNKnwq0VQTdz2H3foFxlqWNopYTlERSsCE0HvgS9aSahotgY2rzQ7kbED0PUZAK0I5jp9SclIKY7YlJK2RR7x-Y9L4Uo5HmUJOa7iviBIUKdO5nD_LKjNAnpv8q4_wSokQa4Sa3j40r6uAwLlBd8CvOrTu5SOQ-qYKqxDOW1fvzxxJvYL422dzKk5i65cvy4UczQa9k-QfKOtYWkqMvPtJYGfkJdTzEGEfnSKsqo6OmXZ_er7agk6wqZ0JU4lQdZuZhFm24LKNfZVidzhe_NiEgUFbsighhnr13Wjymel-xzWwj6mNJvZPLUte-FGSKOtPWAPyzhw_ARVfuoSTC3TGDaAIXft4r2UMdLRWhE-99O7YJH2-7lH0N50j8Hhu_nNV7_RgqyaCxEc7e2PW8vX39TG7kKl1PxxmkCGuZ1fojGSpYPK0Db0SYdEKtY6qoYvR2YqZNj9hNn; odin_tt=a44ba6437551f05d102dac261fb8542ebb2200a9d60cefd99377d4bc0188746cc3c30020ad61c6c65f6fd075e974df8431d6297603a462d67699d21ada7dc9b2; csrfToken=aWMSFbqy-B-pFWRZAc3fmFrFUmzmwKi-hZsE; msToken=rSl2kR4p41OfoZwLaBwPSehv42qRwQknMqxRhT5y4WDlsGbMsXdM1JYjS2mDPFmxt5pqHQsXFlNTY1AWCGlJrhCR3OI5Eh07JaYUej-R25vR_3QE4DkCVouBF-Xecl8XzBCioYEJC-0="
}

DEBUG = True
