import typing
import datetime
from .utils import try_int
from .enums import ChannelType

class Emoji:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.id: int = try_int(data.get('id'))
        self.name: str = data.get('name')

class WelcomeChannel:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.id: int = try_int(data.get('id'))
        self.description: str = data.get('description')
        self.emoji: Emoji = Emoji({'id': data.get('emoji_id'), 'name': data.get('emoji_name')})

class WelcomeScreen:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.description: str = data.get('description')
        self.welcome_channels: typing.List[WelcomeChannel] = [WelcomeChannel(d) for d in data.get('welcome_channels', [])]

class Guild:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.id: int = try_int(data.get('id'))
        self.name: str = data.get('name')
        self.description: str = data.get('description')

        self.splash_hash: str = data.get('splash')
        self.banner_hash: str = data.get('banner')
        self.icon_hash: str = data.get('icon')

        self.features: typing.List[str] = data.get('features')

        self.verification_level: int = try_int(data.get('verification_level'))

        self.vanity_url_code: str = data.get('vanity_url_code')

        self.welcome_screen: WelcomeScreen = WelcomeScreen(data.get('welcome_screen')) if data.get('welcome_screen') else data.get('welcome_screen')

        self.nsfw: bool = data.get('nsfw')
        self.nsfw_level: int = try_int(data.get('nsfw_level'))

class Channel:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.id: int = try_int(data.get('id'))
        self.name: str = data.get('name')

        self.raw_type: int = try_int(data.get('type'))

        # It would prob be voice, but who cares
        if self.raw_type == 0:
            self.type: ChannelType = ChannelType.text
        elif self.raw_type == 1:
            self.type: ChannelType = ChannelType.private
        elif self.raw_type == 2:
            self.type: ChannelType = ChannelType.voice
        elif self.raw_type == 3:
            self.type: ChannelType = ChannelType.group
        elif self.raw_type == 4:
            self.type: ChannelType = ChannelType.category
        elif self.raw_type == 5:
            self.type: ChannelType = ChannelType.news
        elif self.raw_type == 6:
            self.type: ChannelType = ChannelType.store
        elif self.raw_type == 10:
            self.type: ChannelType = ChannelType.news_thread
        elif self.raw_type == 11:
            self.type: ChannelType = ChannelType.public_thread
        elif self.raw_type == 12:
            self.type: ChannelType = ChannelType.private_thread
        elif self.raw_type == 13:
            self.type: ChannelType = ChannelType.stage_voice
        else:
            self.type: ChannelType = ChannelType.voice

class Inviter:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.id: int = try_int(data.get('id'))
        self.username: str = data.get('username')
        self.discriminator: str = try_int(data.get('discriminator'))

        self.public_flags: int = try_int(data.get('public_flags'))

        self.avatar_hash: str = data.get('avatar')

        self.bot: bool = data.get('bot')

class TargetApplication:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.id: int = try_int(data.get('id'))
        self.name: str = data.get('name')
        self.icon_hash: str = data.get('icon')
        self.description: str = data.get('description')
        self.summary: str = data.get('summary')
        self.cover_image_hash: str = data.get('cover_image')
        self.hook: bool = data.get('hook')
        self.terms_of_service_url: str = data.get('terms_of_service_url')
        self.privacy_policy_url: str = data.get('privacy_policy_url')
        self.verify_key: str = data.get('verify_key')
        self.max_participants: int = try_int(data.get('max_participants'))

class ActivityResult:
    def __init__(self, data: typing.Dict[str, typing.Any]):
        self.raw = data.copy()

        self.code: str = data.get('code')
        self.created_at: datetime.datetime = datetime.datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else data.get('created_at')
        self.expires_at: datetime.datetime = datetime.datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else data.get('expires_at')

        self.guild: Guild = Guild(data.get('guild')) if data.get('guild') else data.get('guild')
        self.channel: Channel = Channel(data.get('channel')) if data.get('channel') else data.get('channel')
        self.inviter: Inviter = Inviter(data.get('inviter')) if data.get('inviter') else data.get('inviter')

        self.target_type: int = try_int(data.get('target_type'))
        self.target_application: TargetApplication = TargetApplication(data.get('target_application')) if data.get('target_application') else data.get('target_application')

        self.uses: int = try_int(data.get('uses'))
        self.max_uses: int = try_int(data.get('max_uses'))
        self.max_age: datetime.timedelta = datetime.timedelta(seconds=data.get('max_age')) if data.get('max_age') else data.get('max_age')
        self.temporary: bool = data.get('temporary')

    @property
    def url(self):
        if not self.code:
            return self.code # Just in case self.code is None for some reason

        return f'https://discord.gg/{self.code}'