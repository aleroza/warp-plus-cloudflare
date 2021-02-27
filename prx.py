from lxml.html import fromstring
import requests
import time
import json
from datetime import timedelta


# def get_time():
#     return round(time.perf_counter())


def resptt():
    old = old_resptt
    return round(old.elapsed.total_seconds(), 2)


def get_proxies():
    url = 'https://www.sslproxies.org/'
    headers = {"Connection": "close"}
    response = requests.get(url, headers)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        proxy = ":".join([i.xpath('.//td[1]/text()')
                          [0], i.xpath('.//td[2]/text()')[0]])
        proxies.add(proxy)
    return proxies


def write_to_file(proxies):
    try:
        with open('proxies.json', 'w') as f:
            f.write(json.dumps(proxies, indent=4))
    except Exception:
        print("Smth went wrong...")


def get_req_proxies(proxies):
    proxydict = [{"http": f"http://{proxy}", "https": f"http://{proxy}"}
                 for proxy in proxies]
    return proxydict


def chech_availability(proxydict, n=-1):
    good = []
    for i, proxy in enumerate(proxydict):
        if len(good) == n:
            return good
        try:
            response = requests.get(
                'https://api.myip.com', proxies=proxy, timeout=10)
            if response.ok:
                good.append(proxy)
        except requests.exceptions.ProxyError:
            pass
        except requests.exceptions.ConnectTimeout:
            pass
        except requests.exceptions.SSLError:
            pass
        except Exception:
            print("Поел говна")
            raise
        finally:
            hashs = i * 20 // len(proxydict)
            dashs = 20 - hashs
            print(
                f"[{'#'*hashs}{'-'*dashs}] {i} of {len(proxydict)} checked...", end='\r')
    return good


def main():
    write_to_file(chech_availability(get_req_proxies(get_proxies()), 5))


if __name__ == '__main__':

    old_resptt = requests.models.Response
    requests.models.Response = resptt

    main()
