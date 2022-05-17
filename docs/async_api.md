
<a href="giphpy/async_api.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `async_api.py`





---

<a href="giphpy/async_api.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_gifs`

```python
async_search_gifs(
    q: str,
    lang: str = None,
    rating: giphpy.enums.Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: giphpy.enums.Bundle = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifListResponse]
```

Search for gifs asynchronously by a query string. 

https://developers.giphy.com/docs/api/endpoint#search 



**Args:**
 
 - <b>`q`</b>:  search query term or phrase 
 - <b>`lang`</b>:  specify language using a 2-letter ISO 639-1 language code. 
 - <b>`rating`</b>:  filters results by specified rating 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an ID/proxy for a specific user. 
 - <b>`bundle`</b>:  returns only renditions that correspond to the named bundle. 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_stickers`

```python
async_search_stickers(
    q: str,
    lang: str = None,
    rating: giphpy.enums.Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: giphpy.enums.Bundle = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifListResponse]
```

Search for stickers asynchronously by using a query string. 

https://developers.giphy.com/docs/api/endpoint#search 



**Args:**
 
 - <b>`q`</b>:  search query term or phrase 
 - <b>`lang`</b>:  specify language using a 2-letter ISO 639-1 language code. 
 - <b>`rating`</b>:  filters results by specified rating 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an ID/proxy for a specific user. 
 - <b>`bundle`</b>:  returns only renditions that correspond to the named bundle. 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_trending_gifs`

```python
async_trending_gifs(
    rating: giphpy.enums.Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: giphpy.enums.Bundle = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifListResponse]
```

Get trending gifs asynchronously. 

https://developers.giphy.com/docs/api/endpoint#trending 



**Args:**
 
 - <b>`rating`</b>:  filters results by specified rating 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an ID/proxy for a specific user. 
 - <b>`bundle`</b>:  returns only renditions that correspond to the named bundle. 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_trending_stickers`

```python
async_trending_stickers(
    rating: giphpy.enums.Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: giphpy.enums.Bundle = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifListResponse]
```

Get trending stickers asynchronously. 

https://developers.giphy.com/docs/api/endpoint#trending 



**Args:**
 
 - <b>`rating`</b>:  filters results by specified rating 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an ID/proxy for a specific user. 
 - <b>`bundle`</b>:  returns only renditions that correspond to the named bundle. 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_gif_translate`

```python
async_gif_translate(
    s: str,
    api_key: str = None,
    weirdness: int = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Asynchronously translate words or phrases to a single gif. 

https://developers.giphy.com/docs/api/endpoint#translate 



**Args:**
 
 - <b>`s`</b>:  search term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`weirdness`</b> ('int', `optional`):  value from 0-10 which makes results weirder as you go up the scale 
 - <b>`random_id`</b>:  an ID/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L242"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_sticker_translate`

```python
async_sticker_translate(
    s: str,
    api_key: str = None,
    weirdness: int = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Asynchronously translate words or phrases to a single sticker. 

https://developers.giphy.com/docs/api/endpoint#translate 



**Args:**
 
 - <b>`s`</b>:  search term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`weirdness`</b> ('int', `optional`):  value from 0-10 which makes results weirder as you go up the scale 
 - <b>`random_id`</b>:  an ID/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L267"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_random_gif`

```python
async_random_gif(
    api_key: str = None,
    tag: str = None,
    rating: giphpy.enums.Rating = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Get a single random GIF asynchronously 

https://developers.giphy.com/docs/api/endpoint#random 



**Args:**
 
  - <b>`api_key`</b>:  giphy api key 
  - <b>`tag`</b> ('str`, `optional`):  filter results by a specified tag 
  - <b>`rating`</b>:  filters results by specified rating 
  - <b>`random_id`</b>:  an ID/proxy for a specific user 
  - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
  - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_random_sticker`

```python
async_random_sticker(
    api_key: str = None,
    tag: str = None,
    rating: giphpy.enums.Rating = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Get a single random sticker asynchronously 

https://developers.giphy.com/docs/api/endpoint#random 



**Args:**
 
  - <b>`api_key`</b>:  giphy api key 
  - <b>`tag`</b> ('str`, `optional`):  filter results by a specified tag 
  - <b>`rating`</b>:  filters results by specified rating 
  - <b>`random_id`</b>:  an ID/proxy for a specific user 
  - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
  - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L327"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_random_id`

```python
async_random_id(
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.RandomIdResponse]
```

Asynchronously generate a unique ID you can assign to each new user in your app. 

https://developers.giphy.com/docs/api/endpoint#random-id 



**Args:**
 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `RandomIdResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `RandomIdResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L346"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_action_register`

```python
async_action_register(
    url: str,
    random_id: str,
    ts: int,
    api_key: str = None,
    **kwargs
) → Response
```

Asynchronously Register an impression, click, or send sing a callback url from the analytics object. 

https://developers.giphy.com/docs/api/endpoint#action-register 



**Args:**
 
 - <b>`url`</b>:  an impression, on click, or send callback url from the analytics object 
 - <b>`random_id`</b>:  an id/proxy for a specific user 
 - <b>`ts`</b>:  a unix timestamp in milliseconds corresponding to when the action occurred 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `httpx.Response` 


---

<a href="giphpy/async_api.py#L365"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_gif_by_id`

```python
async_get_gif_by_id(
    gif_id: str,
    api_key: str = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Get a single gif asynchronously by its unique identifier 

https://developers.giphy.com/docs/api/endpoint#get-gif-by-id 



**Args:**
 
 - <b>`gif_id`</b>:  the unique identifier of the gif you want details for 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an id/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L386"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_gifs_by_id`

```python
async_get_gifs_by_id(
    *gif_ids: str,
    api_key: str = None,
    random_id: str = None,
    serialize: bool = None,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifListResponse]
```

Get one or more gifs asynchronously by their unique identifiers. 

https://developers.giphy.com/docs/api/endpoint#get-gifs-by-id 



**Args:**
 
 - <b>`*gif_ids`</b>:  any number of unique identifiers for gifs you want details for 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an id/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L412"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_categories`

```python
async_categories(
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.CategoryListResponse]
```

Asynchronously get a list of gif categories on the giphy network. 

https://developers.giphy.com/docs/api/endpoint#categories 



**Args:**
 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `CategoryListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `CategoryListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L433"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_autocomplete`

```python
async_autocomplete(
    q: str,
    api_key: str = None,
    limit: int = None,
    offset: int = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.SearchTermListResponse]
```

Asynchronously provides a list of valid terms that completes the given tag on the giphy network 

https://developers.giphy.com/docs/api/endpoint#autocomplete 



**Args:**
 
 - <b>`q`</b>:  tag term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `SearchTermListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `SearchTermListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L457"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_channel_search`

```python
async_channel_search(
    q: str,
    api_key: str = None,
    limit: int = None,
    offset: int = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.ChannelListResponse]
```

Asynchronously returns all the giphy channels matching the query term. 

https://developers.giphy.com/docs/api/endpoint#channel-search 



**Args:**
 
 - <b>`q`</b>:  accepts term to search through giphy’s channels 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ChannelListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `ChannelListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L481"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_suggestions`

```python
async_search_suggestions(
    term: str,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.TermListResponse]
```

Asynchronously provides a list of tag terms related to the given tag on the giphy network. 

https://developers.giphy.com/docs/api/endpoint#search-suggestions 



**Args:**
 
 - <b>`term`</b>:  tag term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `TermListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `TermListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/async_api.py#L503"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_trending_search_terms`

```python
async_trending_search_terms(
    api_key: str = None,
    serialize: bool = False,
    **kwargs
)
```

Asynchronously provides a list of the most popular trending search terms on the giphy network. 

https://developers.giphy.com/docs/api/endpoint#trending-search-terms 



**Args:**
 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `TermListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.AsyncClient.get` 



**Returns:**
 `TrendingSearchTermsListResponse` if serialize is True, else `httpx.Response` 



