import enum

class Enum(enum.Enum):
    def __str__(self) -> str:
        return self.name

class ActivityType(Enum):
    watch_together = 880218394199220334
    poker_night = 755827207812677713
    chess = 832012774040141894
    doodle_crew = 878067389634314250
    word_snacks = 879863976006127627
    letter_tile = 879863686565621790
    spellcast = 852509694341283871

    def application_id(self) -> int:
        return self.value

class ChannelType(Enum):
    text = 0
    private = 1
    voice = 2
    group = 3
    category = 4
    news = 5
    store = 6
    news_thread = 10
    public_thread = 11
    private_thread = 12
    stage_voice = 13