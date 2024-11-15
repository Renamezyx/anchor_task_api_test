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

DEBUG = True
