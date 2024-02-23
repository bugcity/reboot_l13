import requests
from util import jquery_now, password_algorithms_cookie, hex_sha256, DictToClass


class ZTEL13:
    _session = requests.Session()

    def __init__(self, host: str, password: str):
        self.host = host
        self.password = password

    def _get_cmd_process(self, cmd: str, with_ts: bool = False) -> DictToClass:

        url = f'http://{self.host}/goform/goform_get_cmd_process'
        params = {
            'isTest': 'false',
            'cmd': cmd,
        }
        if with_ts:
            params['_'] = jquery_now()
        if ',' in cmd:
            params['multi_data'] = 1
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Language': 'ja',
            'Connection': 'keep-alive',
            'Referer': f'http://{self.host}/',
            'Sec-GPC': '1',
            # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        res = self._session.get(url, params=params, headers=headers, verify=False).json()
        return DictToClass(res)

    def _set_cmd_process(self, cmd: str, params: dict) -> DictToClass:

        url = f'http://{self.host}/goform/goform_set_cmd_process'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Language': 'ja',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': f'http://{self.host}',
            'Referer': f'http://{self.host}/',
            'Sec-GPC': '1',
            # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'isTest': 'false',
            'goformId': cmd,
        }
        if params:
            data.update(params)
        res = self._session.post(url, headers=headers, data=data, verify=False).json()
        return DictToClass(res)

    def _ld(self) -> DictToClass:
        return self._get_cmd_process('LD', with_ts=True)

    def login(self) -> bool:
        a = self._ld()
        p1 = password_algorithms_cookie(self.password)
        pw = password_algorithms_cookie(p1 + a.LD)
        res = self._set_cmd_process('LOGIN', {'password': pw})
        return res.result == '0'

    def _rd(self) -> DictToClass:
        res = self._get_cmd_process('wa_inner_version,cr_version,RD')
        return res

    def reboot(self) -> bool:
        a = self._rd()
        a1 = hex_sha256(a.wa_inner_version + a.cr_version)
        ad = hex_sha256(a1 + a.RD)
        self._set_cmd_process('REBOOT_DEVICE', {'AD': ad})
        return True
