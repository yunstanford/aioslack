from ..slack import SLACK_API_BASE
from .util import filter_none

# Constants
CHANNEL_ARCHIVE = "channels.archive"
CHANNEL_CREATE = "channels.create"
CHANNEL_HISTORY = "channels.history" 
CHANNEL_INFO = "channels.info"
CHANNEL_INVITE = "channels.invite"
CHANNEL_JOIN = "channels.join"
CHANNEL_KICK = "channels.kick"
CHANNEL_LEAVE = "channels.leave"
CHANNEL_LIST = "channels.list"
CHANNEL_MARK = "channels.mark"
CHANNEL_RENAME = "channels.rename"
CHANNEL_REPLIES = "channels.replies"
CHANNEL_SET_PURPOSE = "channels.setPurpose"
CHANNEL_SET_TOPIC = "channels.setTopic"
CHANNEL_UNARCHIVE = "channels.unarchive"


class ChannelException(Exception):
    pass


class ChannelClient:

    def __init__(self, session, token):
        self.session = session
        self.token = token

    async def archive_channel(self, channel: str):
        url = SLACK_API_BASE.format(CHANNEL_ARCHIVE)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "channel": channel,
                },
            )

    async def create_channel(self, name: str, validate: bool=True):
        url = SLACK_API_BASE.format(CHANNEL_CREATE)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "name": name,
                    "validate": validate,
                }
            )

    async def get_channel_history(self, channel: str, count: int=None,
                                  inclusive: bool=None, latest: int=None,
                                  oldest: int=None, unreads: bool=None):
        url = SLACK_API_BASE.format(CHANNEL_HISTORY)
        params = {
            "token": self.token,
            "channel": channel,
            "count": count,
            "inclusive": inclusive,
            "latest": latest,
            "oldest": oldest,
            "unreads": unreads,
        }
        params = filter_none(params)

        await self.session.get(
                url,
                params=params,
            )

    async def get_channel_info(self, channel: str, include_locale: bool=False):
        url = SLACK_API_BASE.format(CHANNEL_INFO)
        await self.session.get(
                url,
                params={
                    "token": self.token,
                    "channel": channel,
                    "include_locale": include_locale,
                },
            )

    async def invite_to_channel(self, channel: str, user: str):
        url = SLACK_API_BASE.format(CHANNEL_INVITE)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "channel": channel,
                    "user": user,
                }
            )

    async def join_channel(self, name: str, validate: bool=True):
        url = SLACK_API_BASE.format(CHANNEL_JOIN)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "name": name,
                    "validate": validate,
                }
            )

    async def kick_from_channel(self, channel: str, user: str):
        url = SLACK_API_BASE.format(CHANNEL_KICK)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "channel": channel,
                    "user": user,
                }
            )

    async def leave_channel(self, channel: str):
        url = SLACK_API_BASE.format(CHANNEL_LEAVE)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "channel": channel,
                }
            )

    async def list_channels(self, cursor: str=None, exclude_archived: bool=None,
                            exclude_members: bool=None, limit: int=None):
        url = SLACK_API_BASE.format(CHANNEL_LIST)
        params = {
            "token": self.token,
            "cursor": cursor,
            "exclude_archived": exclude_archived,
            "exclude_members": exclude_members,
            "limit": limit,
        }
        params = filter_none(params)
        await self.session.get(
                url,
                params=params
            )

    async def mark_channel(self, channel: str, ts: int):
        url = SLACK_API_BASE.format(CHANNEL_MARK)
        await self.session.post(
                url,
                params={
                    "token": self.token,
                    "channel": channel,
                    "ts": ts,
                }
            )
