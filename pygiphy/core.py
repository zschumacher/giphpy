import os
import typing
from typing import Final
from typing import TypeVar

import httpx

BASE_URL: Final = "https://api.giphy.com/v1"
GIPHY_API_KEY_VAR_NAME: Final = "GIPHY_API_KEY"

SerializedType = TypeVar("SerializedType")


def _set_api_key_on_params(func_kwargs: dict, instance_api_key: typing.Optional[str]):
    params = func_kwargs.setdefault("params", dict())
    if "api_key" not in params or params["api_key"] is None:
        params["api_key"] = instance_api_key


class GifpyClient(httpx.Client):
    def __init__(self, *args, api_key: str = None, **kwargs):
        self.api_key = api_key or os.getenv(GIPHY_API_KEY_VAR_NAME)
        super().__init__(*args, base_url=BASE_URL, **kwargs)

    def request(self, *args, **kwargs):
        _set_api_key_on_params(kwargs, self.api_key)
        return super().request(*args, **kwargs)


class AsyncGifpyClient(httpx.AsyncClient):
    def __init__(self, *args, api_key: str = None, **kwargs):
        self.api_key = api_key or os.getenv(GIPHY_API_KEY_VAR_NAME)
        super().__init__(*args, base_url=BASE_URL, **kwargs)

    async def request(self, *args, **kwargs):
        _set_api_key_on_params(kwargs, self.api_key)
        response = await super().request(*args, **kwargs)
        return response


def get(*args, model: typing.Type[SerializedType] = None, **kwargs) -> typing.Union[httpx.Response, SerializedType]:
    with GifpyClient() as client:
        response = client.get(*args, **kwargs)
    if model:
        response.raise_for_status()
        return model(**response.json())
    return response


async def async_get(
    *args, model: typing.Type[SerializedType] = None, **kwargs
) -> typing.Union[httpx.Response, SerializedType]:
    async with AsyncGifpyClient() as client:
        response = await client.get(*args, **kwargs)
    if model:
        response.raise_for_status()
        return model(**response.json())
    return response


def _handle_params(func_kwargs: typing.Dict[str, typing.Any], **params):
    """For a better user exp, the api functions have all parameters as named kwargs instead of accepting a dict.

    This function is a helper for ensuring this behaves correctly and constructing the param dict accordingly.
    """
    if "params" in func_kwargs:
        raise ValueError("Params should be passed as named kwargs to this function, not as a separate keyword argument")
    return {k: v for k, v in params.items() if v is not None}


def _validate_weirdness(v: typing.Optional[int]):
    if v is not None and (v < 0 or v > 10):
        raise ValueError("Weirdness must be an int between 0 and 10, inclusive.")
