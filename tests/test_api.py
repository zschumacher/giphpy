import datetime

import pytest

import giphpy
from giphpy.models import CategoryListResponse
from giphpy.models import ChannelListResponse
from giphpy.models import GifListResponse
from giphpy.models import GifResponse
from giphpy.models import RandomIdResponse
from giphpy.models import SearchTermListResponse
from giphpy.models import TermListResponse
from giphpy.models import TrendingSearchTermsListResponse


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_query_parameters": ["api_key"],
        "record_mode": "once",
    }


@pytest.mark.vcr
class TestSearch:
    KWARGS = dict(
        rating=giphpy.Rating.g,
        limit=10,
        lang="en",
        offset=100,
        random_id=12345,
        bundle=giphpy.Bundle.low_bandwidth,
    )
    Q = "spongebob"

    @pytest.mark.parametrize("func", [giphpy.search_gifs, giphpy.search_stickers])
    def test(self, func):
        r = func(self.Q, **self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["rating"] == giphpy.Rating.g.value
        assert params["limit"] == "10"
        assert params["offset"] == "100"
        assert params["random_id"] == "12345"
        assert params["lang"] == "en"
        assert params["bundle"] == giphpy.Bundle.low_bandwidth.value

    @pytest.mark.parametrize("func", [giphpy.search_gifs, giphpy.search_stickers])
    def test_serialize(self, func):
        r = func(self.Q, serialize=True, **self.KWARGS)
        assert isinstance(r, GifListResponse)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_search_gifs, giphpy.async_search_stickers])
    async def test_async(self, func):
        r = await func(self.Q, **self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["rating"] == giphpy.Rating.g.value
        assert params["limit"] == "10"
        assert params["offset"] == "100"
        assert params["random_id"] == "12345"
        assert params["lang"] == "en"
        assert params["bundle"] == giphpy.Bundle.low_bandwidth.value

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_search_gifs, giphpy.async_search_stickers])
    async def test_async_serialize(self, func):
        r = await func("spongebob", serialize=True, **self.KWARGS)
        assert isinstance(r, GifListResponse)


@pytest.mark.vcr
class TestTrending:
    KWARGS = dict(
        rating=giphpy.Rating.g,
        limit=10,
        offset=100,
        random_id=12345,
        bundle=giphpy.Bundle.low_bandwidth,
    )

    @pytest.mark.parametrize("func", [giphpy.trending_gifs, giphpy.trending_stickers])
    def test(self, func):
        r = func(**self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["rating"] == giphpy.Rating.g.value
        assert params["limit"] == "10"
        assert params["offset"] == "100"
        assert params["random_id"] == "12345"
        assert params["bundle"] == giphpy.Bundle.low_bandwidth.value

    @pytest.mark.parametrize("func", [giphpy.trending_gifs, giphpy.trending_stickers])
    def test_serialize(self, func):
        r = func(serialize=True, **self.KWARGS)
        assert isinstance(r, GifListResponse)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_trending_gifs, giphpy.async_trending_stickers])
    async def test_async(self, func):
        r = await func(**self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["rating"] == giphpy.Rating.g.value
        assert params["limit"] == "10"
        assert params["offset"] == "100"
        assert params["random_id"] == "12345"
        assert params["bundle"] == giphpy.Bundle.low_bandwidth.value

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_trending_gifs, giphpy.async_trending_stickers])
    async def test_async_serialize(self, func):
        r = await func(serialize=True, **self.KWARGS)
        assert isinstance(r, GifListResponse)


@pytest.mark.vcr
class TestTranslate:
    KWARGS = dict(
        weirdness=5,
        random_id=12345,
    )
    S = "baseball"

    @pytest.mark.parametrize("func", [giphpy.gif_translate, giphpy.sticker_translate])
    def test(self, func):
        r = func(self.S, **self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["random_id"] == "12345"
        assert params["weirdness"] == "5"

    @pytest.mark.parametrize("func", [giphpy.gif_translate, giphpy.sticker_translate])
    def test_serialize(self, func):
        r = func(self.S, serialize=True, **self.KWARGS)
        assert isinstance(r, GifResponse)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_gif_translate, giphpy.async_sticker_translate])
    async def test_async(self, func):
        r = await func(self.S, **self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["random_id"] == "12345"
        assert params["weirdness"] == "5"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_gif_translate, giphpy.async_sticker_translate])
    async def test_async_serialize(self, func):
        r = await func(self.S, serialize=True, **self.KWARGS)
        assert isinstance(r, GifResponse)


@pytest.mark.vcr
class TestRandom:

    KWARGS = dict(
        tag="basketball",
        rating=giphpy.Rating.g,
        random_id=12345,
    )

    @pytest.mark.parametrize("func", [giphpy.random_gif, giphpy.random_sticker])
    def test(self, func):
        r = func(**self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["random_id"] == "12345"
        assert params["tag"] == "basketball"

    @pytest.mark.parametrize("func", [giphpy.random_gif, giphpy.random_sticker])
    def test_serialize(self, func):
        r = func(serialize=True, **self.KWARGS)
        assert isinstance(r, GifResponse)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_random_gif, giphpy.async_random_sticker])
    async def test_async(self, func):
        r = await func(**self.KWARGS)
        assert r.status_code == 200
        params = r.request.url.params
        assert params["random_id"] == "12345"
        assert params["tag"] == "basketball"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("func", [giphpy.async_random_gif, giphpy.async_random_sticker])
    async def test_async_serialize(self, func):
        r = await func(serialize=True, **self.KWARGS)
        assert isinstance(r, GifResponse)


@pytest.mark.vcr
class TestRandomId:
    def test(self):
        r = giphpy.random_id()
        assert r.status_code == 200

    def test_serialize(self):
        r = giphpy.random_id(serialize=True)
        assert isinstance(r, RandomIdResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_random_id()
        assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_random_id(serialize=True)
        assert isinstance(r, RandomIdResponse)


@pytest.mark.vcr
class TestActionRegister:
    ON_SENT = (
        "https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX"
        "2lkPWw0NkN2Qjd5RXpBQkVDanphJmV2ZW50X3R5cGU9R0lGX1NFQVJDSCZjaWQ9OWZiYzliM2ZydGdicmt3N3E0bW"
        "1zZm42ejRqbm8zNHg3MXRmZWdqdm5idWRibGpjJmN0PWc&action_type=SENT"
    )
    ON_CLICK = (
        "https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX"
        "2lkPWw0NkN2Qjd5RXpBQkVDanphJmV2ZW50X3R5cGU9R0lGX1NFQVJDSCZjaWQ9OWZiYzliM2ZydGdicmt3N3E0bW"
        "1zZm42ejRqbm8zNHg3MXRmZWdqdm5idWRibGpjJmN0PWc&action_type=CLICK"
    )

    ON_LOAD = (
        "https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX"
        "2lkPWw0NkN2Qjd5RXpBQkVDanphJmV2ZW50X3R5cGU9R0lGX1NFQVJDSCZjaWQ9OWZiYzliM2ZydGdicmt3N3E0bW"
        "1zZm42ejRqbm8zNHg3MXRmZWdqdm5idWRibGpjJmN0PWc&action_type=SEEN"
    )

    @pytest.mark.parametrize("url", [ON_SENT, ON_CLICK, ON_LOAD])
    def test(self, url):
        ts = datetime.datetime(2021, 1, 1, 12).toordinal()
        r = giphpy.action_register(url, random_id=12346, ts=ts)
        assert r.request.url.params["ts"] == str(ts)
        assert r.request.url.params["random_id"] == "12346"
        assert r.status_code == 200

    @pytest.mark.parametrize("url", [ON_SENT, ON_CLICK, ON_LOAD])
    @pytest.mark.asyncio
    async def test_async(self, url):
        ts = datetime.datetime(2021, 1, 1, 12).toordinal()
        r = await giphpy.async_action_register(url, random_id=12345, ts=ts)
        assert r.request.url.params["ts"] == str(ts)
        assert r.request.url.params["random_id"] == "12345"
        assert r.status_code == 200


@pytest.mark.vcr
class TestGetGifById:

    GIF_ID = "z1c1SGEsPa1aM"

    def test(self):
        r = giphpy.get_gif_by_id(self.GIF_ID, random_id=12345)
        assert r.request.url.params["random_id"] == "12345"
        assert r.status_code == 200

    def test_serialize(self):
        r = giphpy.get_gif_by_id("z1c1SGEsPa1aM", serialize=True)
        assert isinstance(r, GifResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_get_gif_by_id(self.GIF_ID, random_id=12345)
        assert r.request.url.params["random_id"] == "12345"
        assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_get_gif_by_id(self.GIF_ID, serialize=True)
        assert isinstance(r, GifResponse)


@pytest.mark.vcr
@pytest.mark.parametrize("gif_ids", [("z1c1SGEsPa1aM", "26ufm9YcCl3Cb7dwk"), ("z1c1SGEsPa1aM",)])
class TestGetGifsById:
    def test(self, gif_ids):
        r = giphpy.get_gifs_by_id(*gif_ids, random_id=12345)
        assert r.request.url.params["random_id"] == "12345"
        assert r.status_code == 200

    def test_serialize(self, gif_ids):
        r = giphpy.get_gifs_by_id(*gif_ids, serialize=True)
        assert isinstance(r, GifListResponse)

    @pytest.mark.asyncio
    async def test_async(self, gif_ids):
        r = await giphpy.async_get_gifs_by_id(*gif_ids, random_id=12345)
        assert r.request.url.params["random_id"] == "12345"
        assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_async_serialize(self, gif_ids):
        r = await giphpy.async_get_gifs_by_id(*gif_ids, serialize=True)
        assert isinstance(r, GifListResponse)


@pytest.mark.vcr
class TestGetCategories:
    def test(self):
        r = giphpy.categories()
        assert r.status_code == 200

    def test_serialize(self):
        r = giphpy.categories(serialize=True)
        assert isinstance(r, CategoryListResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_categories()
        assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_categories(serialize=True)
        assert isinstance(r, CategoryListResponse)


@pytest.mark.vcr
class TestAutocomplete:
    SEARCH_TERM = "spongebob"
    KWARGS = dict(limit=10, offset=10)

    def test(self):
        r = giphpy.autocomplete(self.SEARCH_TERM, **self.KWARGS)
        assert r.status_code == 200
        assert r.request.url.params["limit"] == "10"
        assert r.request.url.params["offset"] == "10"

    def test_serialize(self):
        r = giphpy.autocomplete(self.SEARCH_TERM, serialize=True, **self.KWARGS)
        assert isinstance(r, SearchTermListResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_autocomplete(self.SEARCH_TERM, **self.KWARGS)
        assert r.status_code == 200
        assert r.request.url.params["limit"] == "10"
        assert r.request.url.params["offset"] == "10"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_autocomplete(self.SEARCH_TERM, serialize=True, **self.KWARGS)
        assert isinstance(r, SearchTermListResponse)


@pytest.mark.vcr
class TestChannelSearch:
    Q = "basketball"
    KWARGS = dict(limit=10, offset=10)

    def test(self):
        r = giphpy.channel_search(self.Q, **self.KWARGS)
        assert r.status_code == 200
        assert r.request.url.params["limit"] == "10"
        assert r.request.url.params["offset"] == "10"

    def test_serialize(self):
        r = giphpy.channel_search(self.Q, serialize=True, **self.KWARGS)
        assert isinstance(r, ChannelListResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_channel_search(self.Q, **self.KWARGS)
        assert r.status_code == 200
        assert r.request.url.params["limit"] == "10"
        assert r.request.url.params["offset"] == "10"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_channel_search(self.Q, serialize=True, **self.KWARGS)
        assert isinstance(r, ChannelListResponse)


@pytest.mark.vcr
class TestSearchSuggestions:
    SEARCH_TERM = "shaq"

    def test(self):
        r = giphpy.search_suggestions(self.SEARCH_TERM)
        assert r.status_code == 200

    def test_serialize(self):
        r = giphpy.search_suggestions(self.SEARCH_TERM, serialize=True)
        assert isinstance(r, TermListResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_search_suggestions(self.SEARCH_TERM)
        assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_search_suggestions(self.SEARCH_TERM, serialize=True)
        assert isinstance(r, TermListResponse)


@pytest.mark.vcr
class TestGetTrendingSearchTerms:
    def test(self):
        r = giphpy.trending_search_terms()
        assert r.status_code == 200

    def test_serialize(self):
        r = giphpy.trending_search_terms(serialize=True)
        assert isinstance(r, TrendingSearchTermsListResponse)

    @pytest.mark.asyncio
    async def test_async(self):
        r = await giphpy.async_trending_search_terms()
        assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        r = await giphpy.async_trending_search_terms(serialize=True)
        assert isinstance(r, TrendingSearchTermsListResponse)
