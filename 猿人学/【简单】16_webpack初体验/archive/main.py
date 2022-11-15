import time
import requests
from loguru import logger
from node_vm2 import NodeVM

with open('./code.js', mode='r', encoding='utf-8') as file:
    js_code = file.read()

vm = NodeVM.code(js_code)

with requests.Session() as session:
    values = []
    for page in range(1, 6):
        t = str(int(time.time())) + '000'
        m = vm.call_member('btoa', t)
        logger.debug(f't: {t} m: {m}')
        res = session.get(
            url='https://match.yuanrenxue.com/api/match/16',
            headers={
                'User-Agent': 'yuanrenxue.project',
                'cookie': 'sessionid=fza7nzksd8gb4ymybfg1offeczq155at'
            },
            # cookies={
            #     'sessionid': '8zj8ey2s8oo69bb22una97idvyi2l5f3',
            # },
            params={
                'page': page,
                't': t,
                'm': m,
            }
        )
        logger.debug(res.status_code and res.json())
        values += [_.get('value') for _ in res.json().get('data')]
    logger.debug(f'总和：{sum(values)}')
