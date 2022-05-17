[![test](https://github.com/zschumacher/pygiphy/actions/workflows/test.yml/badge.svg)](https://github.com/zschumacher/pygiphy/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/pygiphy/badge/?version=latest)](https://pygiphy.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/zschumacher/pygiphy/branch/main/graph/badge.svg?token=ADXWQI8YMX)](https://codecov.io/gh/zschumacher/pygiphy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# pygiphy
`pygiphy` was written to be a hand-spun alternative to the existing [giphy client](https://github.com/Giphy/giphy-python-client).

You should use it because:

* it uses [pydantic](https://pydantic-docs.helpmanual.io) for lightning fast data serialization
* it uses [httpx](https://www.python-httpx.org) to provide both a sync and async api

## Installation
=== "pip"
    ```console
    pip install pygiphy
    ```

=== "poetry"
    ```console
    poetry add pygiphy
    ```

## Authentication
In order to authenticate to the GIPHY API, you must [request an API key](https://support.giphy.com/hc/en-us/articles/360020283431-Request-A-GIPHY-API-Key)
from their developer portal.

Once you have your key, you can use it in `pygiphy` by setting the `GIPHY_API_KEY` environment variable or by passing
`api_key="xxx"` as a kwarg to any function (see examples below).

=== "environment variable"
    ```python
    import os

    import pygiphy
    
    os.environ["GIPHY_API_KEY"] = "xxx"
    response = pygiphy.gif_translate("spongebob")
    ```

=== "kwarg"
    ```python
    import pygiphy

    response = pygiphy.gif_translate("spongebob", api_key="xxx)
    ```

## Simple Example
pygiphy is extremely easy to use.  By setting `serialize=True`, you get a pydantic model returned to you instead of
a `httpx.Response` object.

Below are examples of what the code looks like for both the sync and async apis.

=== "sync"
    ```python
    import pygiphy

    gif = pygiphy.gif_translate("spongebob", api_key="xxx", serialize=True)
    print(gif)
    ```

=== "async"
    ```python
    import asyncio 

    import pygiphy
    
    async def main():
        gif = await pygiphy.async_gif_translate("spongebob", api_key="xxx)
        print(gif)

    asyncio.run(main())
    ```

This will give you a `GifResponse` object.

```python
GifResponse(
        data=Gif(
            type='gif',
            id='o6TTJ6ak4A97a',
            url='https://giphy.com/gifs/spongebob-squarepants-squidward-nose-o6TTJ6ak4A97a',
            slug='spongebob-squarepants-squidward-nose-o6TTJ6ak4A97a',
            bitly_gif_url='http://gph.is/YBiYub',
            bitly_url='http://gph.is/YBiYub',
            embed_url='https://giphy.com/embed/o6TTJ6ak4A97a',
            username='spongebob',
            source='',
            title='Nose GIF by SpongeBob SquarePants',
            rating=<Rating.g: 'g'>,
            content_url='',
            source_tld='',
            source_post_url='',
            is_sticker=False,
            import_datetime=datetime.datetime(1970, 1, 1, 0, 0),
            trending_datetime=datetime.datetime(2017, 12, 21, 16, 0, 1),
            images=Images(
                downsized=DownsizedImage(
                    size='430185',
                    height='336',
                    width='500',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=giphy.gif&ct=g'
                    ),
                ),
                downsized_large=DownsizedLargeImage(
                    size='430185',
                    height='336',
                    width='500',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=giphy.gif&ct=g'
                    ),
                ),
                downsized_medium=DownsizedMediumImage(
                    size='430185',
                    height='336',
                    width='500',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=giphy.gif&ct=g'
                    ),
                ),
                downsized_small=DownsizedSmallImage(
                    mp4_size='162356',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy-downsized-small.mp4?cid=9fbc9b3fgy0n3l2a9s'
                        'mslyf34wgd2s5z68p60zymuq6950uz&rid=giphy-downsized-small.mp4&ct=g'
                    ),
                    height='336',
                    width='500',
                ),
                downsized_still=DownsizedStillImage(
                    height='336',
                    width='500',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy_s.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z'
                        '68p60zymuq6950uz&rid=giphy_s.gif&ct=g'
                    ),
                ),
                fixed_height=FixedHeightImage(
                    webp_size='112580',
                    webp=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200.webp?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p'
                        '60zymuq6950uz&rid=200.webp&ct=g'
                    ),
                    mp4_size='36280',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p6'
                        '0zymuq6950uz&rid=200.mp4&ct=g'
                    ),
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p6'
                        '0zymuq6950uz&rid=200.gif&ct=g'
                    ),
                    height='200',
                    width='298',
                    size='188398',
                ),
                fixed_height_downsampled=FixedHeightDownsampledImage(
                    webp_size='118418',
                    webp=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200_d.webp?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z6'
                        '8p60zymuq6950uz&rid=200_d.webp&ct=g'
                    ),
                    size='166021',
                    height='200',
                    width='298',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200_d.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=200_d.gif&ct=g'
                    ),
                ),
                fixed_height_small=FixedHeightSmallImage(
                    webp_size='38138',
                    webp=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100.webp?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p'
                        '60zymuq6950uz&rid=100.webp&ct=g'
                    ),
                    mp4_size='12397',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p6'
                        '0zymuq6950uz&rid=100.mp4&ct=g'
                    ),
                    size='54532',
                    height='100',
                    width='149',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p6'
                        '0zymuq6950uz&rid=100.gif&ct=g'
                    ),
                ),
                fixed_height_small_still=FixedHeightSmallStillImage(
                    height='100',
                    width='149',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100_s.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=100_s.gif&ct=g'
                    ),
                ),
                fixed_height_still=FixedHeightStillImage(
                    height='200',
                    width='298',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200_s.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=200_s.gif&ct=g'
                    ),
                ),
                fixed_width=FixedWidthImage(
                    webp_size='61756',
                    webp=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200w.webp?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=200w.webp&ct=g'
                    ),
                    mp4_size='19095',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200w.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p'
                        '60zymuq6950uz&rid=200w.mp4&ct=g'
                    ),
                    size='87701',
                    height='134',
                    width='200',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200w.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p'
                        '60zymuq6950uz&rid=200w.gif&ct=g'
                    ),
                ),
                fixed_width_downsampled=FixedWidthDownsampledImage(
                    webp_size='62046',
                    webp=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200w_d.webp?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z'
                        '68p60zymuq6950uz&rid=200w_d.webp&ct=g'
                    ),
                    size='78853',
                    height='134',
                    width='200',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200w_d.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z6'
                        '8p60zymuq6950uz&rid=200w_d.gif&ct=g'
                    ),
                ),
                fixed_width_small=FixedWidthSmallImage(
                    webp_size='19028',
                    webp=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100w.webp?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=100w.webp&ct=g'
                    ),
                    mp4_size='7319',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100w.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p'
                        '60zymuq6950uz&rid=100w.mp4&ct=g'
                    ),
                    size='25141',
                    height='67',
                    width='100',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100w.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68p'
                        '60zymuq6950uz&rid=100w.gif&ct=g'
                    ),
                ),
                fixed_width_small_still=FixedWidthSmallStillImage(
                    height='67',
                    width='100',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/100w_s.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z6'
                        '8p60zymuq6950uz&rid=100w_s.gif&ct=g'
                    ),
                ),
                fixed_width_still=FixedWidthStillImage(
                    height='134',
                    width='200',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/200w_s.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z6'
                        '8p60zymuq6950uz&rid=200w_s.gif&ct=g'
                    ),
                ),
                looping=LoopingImage(
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy-loop.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2'
                        's5z68p60zymuq6950uz&rid=giphy-loop.mp4&ct=g'
                    ),
                ),
                original_still=OriginalStillImage(
                    height='336',
                    width='500',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy_s.gif?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z'
                        '68p60zymuq6950uz&rid=giphy_s.gif&ct=g'
                    ),
                ),
                original_mp4=OriginalMp4Image(
                    mp4_size='123856',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z68'
                        'p60zymuq6950uz&rid=giphy.mp4&ct=g'
                    ),
                    height='322',
                    width='480',
                ),
                preview=PreviewImage(
                    height='184',
                    width='273',
                    mp4_size='21235',
                    mp4=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy-preview.mp4?cid=9fbc9b3fgy0n3l2a9smslyf34w'
                        'gd2s5z68p60zymuq6950uz&rid=giphy-preview.mp4&ct=g'
                    ),
                ),
                preview_gif=PreviewGifImage(
                    height='90',
                    width='134',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy-preview.gif?cid=9fbc9b3fgy0n3l2a9smslyf34w'
                        'gd2s5z68p60zymuq6950uz&rid=giphy-preview.gif&ct=g'
                    ),
                ),
                preview_webp=PreviewWebpImage(
                    size='34118',
                    height='94',
                    width='140',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/giphy-preview.webp?cid=9fbc9b3fgy0n3l2a9smslyf34'
                        'wgd2s5z68p60zymuq6950uz&rid=giphy-preview.webp&ct=g'
                    ),
                ),
                still_480w=Still480w(
                    height='323',
                    width='480',
                    url=(
                        'https://media3.giphy.com/media/o6TTJ6ak4A97a/480w_s.jpg?cid=9fbc9b3fgy0n3l2a9smslyf34wgd2s5z6'
                        '8p60zymuq6950uz&rid=480w_s.jpg&ct=g'
                    ),
                    size='430185',
                ),
            ),
            user=User(
                avatar_url='https://media2.giphy.com/avatars/spongebob/U4nimQFVGMqR.jpg',
                banner_image='',
                banner_url='',
                profile_url='https://giphy.com/spongebob/',
                username='spongebob',
                display_name='SpongeBob SquarePants',
                description='Who gifs in a pineapple under the sea?',
                instagram_url='',
                website_url='http://www.spongebob.com',
                is_verified=True,
            ),
            analytics_response_payload=None,
            analytics=None,
        ),
        meta=Meta(
            status=200,
            msg='OK',
            response_id='gy0n3l2a9smslyf34wgd2s5z68p60zymuq6950uz',
        ),
    )
```

