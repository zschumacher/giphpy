
<a href="giphpy/api.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `api.py`





---

<a href="giphpy/api.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_gifs`

```python
search_gifs(
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

Search for gifs by a query string. 

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
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_stickers`

```python
search_stickers(
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

Search for stickers by using a query string. 

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
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `trending_gifs`

```python
trending_gifs(
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

Get trending gifs. 

https://developers.giphy.com/docs/api/endpoint#trending 



**Args:**
 
 - <b>`rating`</b>:  filters results by specified rating 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an ID/proxy for a specific user. 
 - <b>`bundle`</b>:  returns only renditions that correspond to the named bundle. 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `trending_stickers`

```python
trending_stickers(
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

Get trending stickers. 

https://developers.giphy.com/docs/api/endpoint#trending 



**Args:**
 
 - <b>`rating`</b>:  filters results by specified rating 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an ID/proxy for a specific user. 
 - <b>`bundle`</b>:  returns only renditions that correspond to the named bundle. 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gif_translate`

```python
gif_translate(
    s: str,
    api_key: str = None,
    weirdness: int = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Translate words or phrases to a single gif. 

https://developers.giphy.com/docs/api/endpoint#translate 



**Args:**
 
 - <b>`s`</b>:  search term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`weirdness`</b> ('int', `optional`):  value from 0-10 which makes results weirder as you go up the scale 
 - <b>`random_id`</b>:  an ID/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sticker_translate`

```python
sticker_translate(
    s: str,
    api_key: str = None,
    weirdness: int = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Translate words or phrases to a single sticker. 

https://developers.giphy.com/docs/api/endpoint#translate 



**Args:**
 
 - <b>`s`</b>:  search term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`weirdness`</b> ('int', `optional`):  value from 0-10 which makes results weirder as you go up the scale 
 - <b>`random_id`</b>:  an ID/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `random_gif`

```python
random_gif(
    api_key: str = None,
    tag: str = None,
    rating: giphpy.enums.Rating = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Get a single random GIF 

https://developers.giphy.com/docs/api/endpoint#random 



**Args:**
 
  - <b>`api_key`</b>:  giphy api key 
  - <b>`tag`</b> ('str`, `optional`):  filter results by a specified tag 
  - <b>`rating`</b>:  filters results by specified rating 
  - <b>`random_id`</b>:  an ID/proxy for a specific user 
  - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
  - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L289"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `random_sticker`

```python
random_sticker(
    api_key: str = None,
    tag: str = None,
    rating: giphpy.enums.Rating = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Get a single random sticker 

https://developers.giphy.com/docs/api/endpoint#random 



**Args:**
 
  - <b>`api_key`</b>:  giphy api key 
  - <b>`tag`</b> ('str`, `optional`):  filter results by a specified tag 
  - <b>`rating`</b>:  filters results by specified rating 
  - <b>`random_id`</b>:  an ID/proxy for a specific user 
  - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
  - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L319"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `random_id`

```python
random_id(
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.RandomIdResponse]
```

Generate a unique ID you can assign to each new user in your app. 

https://developers.giphy.com/docs/api/endpoint#random-id 



**Args:**
 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `RandomIdResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `RandomIdResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L338"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `action_register`

```python
action_register(
    url: str,
    random_id: str,
    ts: int,
    api_key: str = None,
    **kwargs
) → Response
```

Register an impression, click, or send sing a callback url from the analytics object. 

https://developers.giphy.com/docs/api/endpoint#action-register 



**Args:**
 
 - <b>`url`</b>:  an impression, on click, or send callback url from the analytics object 
 - <b>`random_id`</b>:  an id/proxy for a specific user 
 - <b>`ts`</b>:  a unix timestamp in milliseconds corresponding to when the action occurred 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `httpx.Response` 


---

<a href="giphpy/api.py#L357"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_gif_by_id`

```python
get_gif_by_id(
    gif_id: str,
    api_key: str = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifResponse]
```

Get a single gif by its unique identifier 

https://developers.giphy.com/docs/api/endpoint#get-gif-by-id 



**Args:**
 
 - <b>`gif_id`</b>:  the unique identifier of the gif you want details for 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an id/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L378"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_gifs_by_id`

```python
get_gifs_by_id(
    *gif_ids: str,
    api_key: str = None,
    random_id: str = None,
    serialize: bool = None,
    **kwargs
) → Union[httpx.Response, giphpy.models.GifListResponse]
```

Get one or more gifs by their unique identifiers 

https://developers.giphy.com/docs/api/endpoint#get-gifs-by-id 



**Args:**
 
 - <b>`*gif_ids`</b>:  any number of unique identifiers for gifs you want details for 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`random_id`</b>:  an id/proxy for a specific user 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `GifListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `GifListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L404"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `categories`

```python
categories(
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.CategoryListResponse]
```

Get a list of gif categories on the giphy network. 

https://developers.giphy.com/docs/api/endpoint#categories 



**Args:**
 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `CategoryListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `CategoryListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L423"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `autocomplete`

```python
autocomplete(
    q: str,
    api_key: str = None,
    limit: int = None,
    offset: int = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.SearchTermListResponse]
```

Provides a list of valid terms that completes the given tag on the giphy network 

https://developers.giphy.com/docs/api/endpoint#autocomplete 



**Args:**
 
 - <b>`q`</b>:  tag term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `SearchTermListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `SearchTermListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L445"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `channel_search`

```python
channel_search(
    q: str,
    api_key: str = None,
    limit: int = None,
    offset: int = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.ChannelListResponse]
```

Returns all the giphy channels matching the query term. 

https://developers.giphy.com/docs/api/endpoint#channel-search 



**Args:**
 
 - <b>`q`</b>:  accepts term to search through giphy’s channels 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`limit`</b>:  maximum number of objects to return. if not passed, 25 
 - <b>`offset`</b>:  the starting position of results. if not passed, 0 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ChannelListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `ChannelListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L467"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_suggestions`

```python
search_suggestions(
    term: str,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.TermListResponse]
```

Provides a list of tag terms related to the given tag on the giphy network. 

https://developers.giphy.com/docs/api/endpoint#search-suggestions 



**Args:**
 
 - <b>`term`</b>:  tag term 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `TermListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `TermListResponse` if serialize is True, else `httpx.Response` 


---

<a href="giphpy/api.py#L487"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `trending_search_terms`

```python
trending_search_terms(
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, giphpy.models.TrendingSearchTermsListResponse]
```

Provides a list of the most popular trending search terms on the giphy network. 

https://developers.giphy.com/docs/api/endpoint#trending-search-terms 



**Args:**
 
 - <b>`api_key`</b>:  giphy api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `TermListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `TrendingSearchTermsListResponse` if serialize is True, else `httpx.Response` 



