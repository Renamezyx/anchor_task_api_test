import os


def get_project_root():
    # 获取根目录 不受运行目录影响
    current_dir = os.path.abspath(__file__)
    while not os.path.exists(os.path.join(current_dir, '.project_root')):
        current_dir = os.path.dirname(current_dir)
    return current_dir


rpc_headers = {
    "host": "cloud-sg.tiktok-row.net",
    "content-length": "1015",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-jwt-token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYWFzLnBhc3Nwb3J0LmF1dGgiLCJleHAiOjE3MzM1OTkyNTYsImlhdCI6MTczMzU5NTU5NiwidXNlcm5hbWUiOiJ6ZW5neXVodWkiLCJ0eXBlIjoicGVyc29uX2FjY291bnQiLCJyZWdpb24iOiJpMThuIiwidHJ1c3RlZCI6dHJ1ZSwidXVpZCI6ImFmNDIzYmQyLTBmZWMtNDc5MC05ZDUxLTZmZTBhMTA4NGM4ZCIsInNpdGUiOiJsb2NhbCIsImJ5dGVjbG91ZF90ZW5hbnRfaWRfb3JnIjoiYnl0ZWRhbmNlIiwic2NvcGUiOiJieXRlZGFuY2UiLCJzZXF1ZW5jZSI6IlRlc3QiLCJvcmdhbml6YXRpb24iOiJUaWtUb2sg56CU5Y-RLei0qOmHj-S_nemanC3lm73pmYXnm7Tmkq0t5ri45oiPIiwid29ya19jb3VudHJ5IjoiQ0hOIiwiYXZhdGFyX3VybCI6Imh0dHBzOi8vczE2LWltZmlsZS1zZy5mZWlzaHVjZG4uY29tL3N0YXRpYy1yZXNvdXJjZS92MS92M18wMDhsXzAzZDllODhlLWNmNmMtNDEzMS1iZjlhLThjOWM1NWI2NTNodX4_aW1hZ2Vfc2l6ZT1ub29wXHUwMDI2Y3V0X3R5cGU9XHUwMDI2cXVhbGl0eT1cdTAwMjZmb3JtYXQ9cG5nXHUwMDI2c3RpY2tlcl9mb3JtYXQ9LndlYnAiLCJlbWFpbCI6Inplbmd5dWh1aUBieXRlZGFuY2UuY29tIiwiZW1wbG95ZWVfaWQiOjMxMDU3MjksIm9nX2xpbWl0Ijoibm9uZSJ9.qrhqdJ-0lbeYNLxicrhOUMiPaCWW7OaCQNVyNBUzIsOeTcOsYudi0niCj5bX58-1DhvBz78O3IQKbqXl4gdNyMDCeAbNOcsu3GkiMyl03g0u8p1h1L3LS4Re2d8jc0a5X3R2VaKxlQqneFmmJIjCLGP3GuNa3Ux9Lscv1Xw6Juc",
    "accept-language": "zh",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "origin": "https://bits.bytedance.net",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://bits.bytedance.net/",
    "accept-encoding": "gzip, br",
    "priority": "u=1, i"
}
rpc_headers.pop("accept-encoding")

DEBUG = True

threading_num = 3
