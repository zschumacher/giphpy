from enum import Enum


class Rating(str, Enum):
    # https://developers.giphy.com/docs/optional-settings/#rating
    g = "g"
    pg = "pg"
    pg_13 = "pg-13"
    r = "r"


class Bundle(str, Enum):
    # https://developers.giphy.com/docs/optional-settings#rendition-guide
    clips_grid_picker = "clips_grid_picker"
    messaging_non_clips = "messaging_non_clips"
    sticker_layering = "sticker_layering"
    low_bandwidth = "low_bandwidth"


class _Resource(Enum):
    search = "search"
    trending = "trending"
    translate = "translate"
    random = "random"

    @property
    def gif(self) -> str:
        return f"/gifs/{self.value}"

    @property
    def sticker(self) -> str:
        return f"/stickers/{self.value}"
