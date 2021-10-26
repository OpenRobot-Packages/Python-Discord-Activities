import typing
import aiohttp
import json
from typing import Union, Dict, Any

async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding='utf-8')
    try:
        if response.headers['content-type'] == 'application/json':
            return json.loads(text)
    except KeyError:
        # Thanks Cloudflare
        pass

    return text

def try_int(self, obj: Any) -> typing.Union[int, Any]:
    try:
        return int(obj)
    except:
        return obj