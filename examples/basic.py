import discord # pip install discord.py
from openrobot.discord_activities import DiscordActivity, ActivityType # pip install git+https://github.com/OpenRobot/Python-Discord-Activities

activity = DiscordActivity('<Insert Bot Token>')

# Insert your own stuff here
channel_id: int = ...
activity: ActivityType = ...
# ...

# List of ActivityType:
# - ActivityType.watch_together
# - ActivityType.poker_night
# - ActivityType.chess
# - ActivityType.doodle_crew
# - ActivityType.word_snacks
# - ActivityType.letter_tile
# - ActivityType.spellcast
# - ActivityType.checkers
# - ActivityType.fishington
# - ActivityType.betrayal

act = await activity.set_activity(channel_id, activity, ...) # openrobot.discord_activities.dataclass.ActivityResult

await Messageable.send(embed=discord.Embed(description=f'[Click Here to enjoy your `{str(activity).replace("_", " ").title()}` activity!]({act.url})'))