import os
import cloudscraper

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Platform": "Windows",
    "Origin": "https://www.paofu.cloud",
    "Referer": "https://www.paofu.cloud/auth/login",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close"
}


def login(email, password):
    s = cloudscraper.create_scraper()
    data = {
        "email": email,
        "passwd": password
    }
    r = s.post("https://www.paofu.cloud/auth/login", headers=header, params=data)
    print(r.content)
    return s


def get_traffic(s, header=header):
    header["Accept"] = "application/json, text/javascript, */*; q=0.01"
    header["Referer"] = "https://www.paofu.cloud/user"
    r = s.post("https://www.paofu.cloud/user/checkin", headers=header)
    print(r.content)


if __name__ == '__main__':
    email = os.environ["PAOFU_EMAIL"]
    password = os.environ["PAOFU_PASSWORD"]

    session = login(email, password)
    get_traffic(session)
