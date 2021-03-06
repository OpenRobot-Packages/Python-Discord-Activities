import datetime
import aiohttp
import asyncio
import typing
import json
from .utils import *
from .errors import *
from .enums import *
from .dataclass import *

class DiscordActivity:
    def __init__(self, bot_token: str):
        self.bot_token = str(bot_token)

        self._tries = 5

    async def _request(self, method: str, url: str, **kwargs) -> typing.Union[typing.Dict[str, typing.Any], str]:
        headers = {
            'Authorization': 'Bot ' + self.bot_token,
            'Content-Type': 'application/json'
        }
        
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))

        async with aiohttp.ClientSession() as sess:
            for tries in range(self._tries):
                async with sess.request(method, url, headers=headers, **kwargs) as resp:
                    data = await json_or_text(resp)

                    if 300 > resp.status >= 200:
                        return data

                    if resp.status in {500, 502, 504}:
                        await asyncio.sleep(1 + tries * 2)
                        continue

                    raise UnexpectedHTTPResponse(resp, data)

    async def set_activity(self, channel_id: int, activity_type: ActivityType, *, max_age: datetime.timedelta = None, max_uses: int = 0, temporary: bool = False, unique: bool = False) -> ActivityResult:
        app_id = activity_type.application_id()

        js = await self._request('POST', f'https://discord.com/api/v9/channels/{channel_id}/invites', data=json.dumps({
            'max_age': max_age.total_seconds() if isinstance(max_age, datetime.timedelta) else max_age if max_age else 0,
            'max_uses': max_uses,
            'temporary': temporary,
            'unique': unique,
            'target_type': 2,
            'target_application_id': app_id
        }, separators=(',', ':'), ensure_ascii=True))

        return ActivityResult(js)