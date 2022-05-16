import datetime
import typing

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from pygiphy import Rating


class ImageSize(BaseModel):
    size: str


class ImageDimensions(BaseModel):
    height: str
    width: str


class Url(BaseModel):
    url: str


class Mp4(BaseModel):
    mp4_size: str
    mp4: str


class Webp(BaseModel):
    webp_size: str
    webp: str


class FixedHeightImage(ImageSize, ImageDimensions, Url, Mp4, Webp):
    pass


class FixedHeightStillImage(Url, ImageDimensions):
    pass


class FixedHeightDownsampledImage(Url, ImageDimensions, ImageSize, Webp):
    pass


class FixedWidthImage(Url, ImageDimensions, ImageSize, Mp4, Webp):
    pass


class FixedWidthStillImage(Url, ImageDimensions):
    pass


class FixedWidthDownsampledImage(Url, ImageDimensions, ImageSize, Webp):
    pass


class FixedHeightSmallImage(Url, ImageDimensions, ImageSize, Mp4, Webp):
    pass


class FixedHeightSmallStillImage(Url, ImageDimensions):
    pass


class FixedWidthSmallImage(Url, ImageDimensions, ImageSize, Mp4, Webp):
    pass


class FixedWidthSmallStillImage(Url, ImageDimensions):
    pass


class DownsizedImage(Url, ImageDimensions, ImageSize):
    pass


class DownsizedStillImage(Url, ImageDimensions):
    pass


class DownsizedLargeImage(Url, ImageDimensions, ImageSize):
    pass


class DownsizedMediumImage(Url, ImageDimensions, ImageSize):
    pass


class DownsizedSmallImage(ImageDimensions, Mp4):
    pass


class OriginalImage(ImageDimensions, ImageSize, Mp4, Webp):
    frames: str


class OriginalStillImage(Url, ImageDimensions):
    pass


class OriginalMp4Image(ImageDimensions, Mp4):
    pass


class LoopingImage(BaseModel):
    mp4: str


class PreviewImage(Mp4, ImageDimensions):
    pass


class PreviewGifImage(Url, ImageDimensions):
    pass


class PreviewWebpImage(Url, ImageDimensions, ImageSize):
    pass


class Still480w(Url, ImageDimensions):
    size: typing.Optional[str]


class Images(BaseModel):
    downsized: typing.Optional[DownsizedImage]
    downsized_large: typing.Optional[DownsizedLargeImage]
    downsized_medium: typing.Optional[DownsizedMediumImage]
    downsized_small: typing.Optional[DownsizedSmallImage]
    downsized_still: typing.Optional[DownsizedStillImage]
    fixed_height: typing.Optional[FixedHeightImage]
    fixed_height_downsampled: typing.Optional[FixedHeightDownsampledImage]
    fixed_height_small: typing.Optional[FixedHeightSmallImage]
    fixed_height_small_still: typing.Optional[FixedHeightSmallStillImage]
    fixed_height_still: typing.Optional[FixedHeightStillImage]
    fixed_width: typing.Optional[FixedWidthImage]
    fixed_width_downsampled: typing.Optional[FixedWidthDownsampledImage]
    fixed_width_small: typing.Optional[FixedWidthSmallImage]
    fixed_width_small_still: typing.Optional[FixedWidthSmallStillImage]
    fixed_width_still: typing.Optional[FixedWidthStillImage]
    looping: typing.Optional[LoopingImage]
    original_still: typing.Optional[OriginalStillImage]
    original_mp4: typing.Optional[OriginalMp4Image]
    preview: typing.Optional[PreviewImage]
    preview_gif: typing.Optional[PreviewGifImage]
    preview_webp: typing.Optional[PreviewWebpImage]
    still_480w: typing.Optional[Still480w] = Field(alias="480w_still")


class User(BaseModel):
    avatar_url: str
    banner_image: str
    banner_url: typing.Optional[str]
    profile_url: str
    username: str
    display_name: str
    description: str
    instagram_url: typing.Optional[str]
    website_url: typing.Optional[str]
    is_verified: bool


class Analytics(BaseModel):
    onload: Url
    onclick: Url
    onsent: Url


class Gif(BaseModel):

    type: str
    id: str
    url: str
    slug: str
    bitly_gif_url: str
    bitly_url: str
    embed_url: str
    username: str
    source: str
    title: str
    rating: Rating
    content_url: typing.Optional[str]
    source_tld: str
    source_post_url: typing.Optional[str]
    is_sticker: bool
    import_datetime: datetime.datetime
    trending_datetime: typing.Optional[datetime.datetime]
    images: Images
    user: typing.Optional[User]
    analytics_response_payload: typing.Optional[str]
    analytics: typing.Optional[Analytics]

    @validator("trending_datetime", pre=True)
    def validate_trending_datetime(cls, v):
        if v == "0000-00-00 00:00:00":
            return None
        return v


class Pagination(BaseModel):
    total_count: typing.Optional[int]
    count: int
    offset: typing.Optional[int]


class Meta(BaseModel):
    status: int
    msg: str
    response_id: str


class GifResponse(BaseModel):
    data: Gif
    meta: Meta


class GifListResponse(BaseModel):
    data: typing.List[Gif]
    pagination: Pagination
    meta: Meta


class BaseCategory(BaseModel):
    name: str
    name_encoded: str


class Subcategory(BaseCategory):
    pass


class Category(BaseCategory):
    subcategories: typing.List[Subcategory]
    gif: Gif


class CategoryListResponse(BaseModel):
    data: typing.List[Category]
    pagination: Pagination
    meta: Meta


class RandomId(BaseModel):
    random_id: str


class RandomIdResponse(BaseModel):
    data: RandomId
    meta: Meta


class SearchTerm(BaseModel):
    name: str
    analytics_response_payload: str


class SearchTermListResponse(BaseModel):
    data: typing.List[SearchTerm]
    pagination: Pagination
    meta: Meta


class ChannelTag(BaseModel):
    id: int
    channel: int
    rank: int
    tag: str


class Channel(BaseModel):
    id: int
    url: typing.Optional[str]
    display_name: str
    parent: typing.Optional[int]
    slug: str
    type: str
    content_type: str
    short_display_name: str
    description: str
    has_children: bool
    featured_gif: typing.Optional[Gif]
    user: User
    banner_image: typing.Optional[str]
    metadata_description: typing.Optional[str]
    is_visible: typing.Optional[bool]
    is_private: typing.Optional[bool]
    is_live: typing.Optional[bool]
    screensaver_gif: typing.Optional[str]
    live_since_datetime: typing.Optional[datetime.datetime]
    live_until_datetime: typing.Optional[datetime.datetime]
    ancestors: typing.List["Channel"]
    analytics_response_payload: str
    tags: typing.List[ChannelTag]
    syncable_tags: typing.Optional[typing.List[ChannelTag]]


class ChannelListResponse(BaseModel):
    data: typing.List[Channel]
    pagination: Pagination
    meta: Meta


class Term(BaseModel):
    name: str
    analytics_response_payload: str


class TermListResponse(BaseModel):
    data: typing.List[Term]
    meta: Meta


class TrendingSearchTermsListResponse(BaseModel):
    data: typing.List[str]
    meta: Meta
