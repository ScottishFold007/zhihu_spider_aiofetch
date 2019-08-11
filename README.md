# aiofetch

## Description

- This is a project to crawl the zhihu website(https://www.zhihu.com/).
- Most commonly used APIs are availible.
## Dependencies

- Python 3 only
- Only tested in **Python 3.7**
```
import sys
import time
import random
import aiohttp
import asyncio
import logging
from multiprocessing import Pool, Manager
```
## Operation
1.Clone floder `aiofetch`

2.Mark `aiofetch` as `Sources Root` in your IDE

3.Replace the code in `aiofetch/headers_pool.py` and `aiofetch/zhihu_APIs.py` wrapped in `<` and `>` with the hints in `<` and `>`

4.Import `data_getter` in your code and construct request refer to the example in `if __name__ == '__main__':` of `aiofetch/data_getter`

5.Run and wait for the dict it return

## Output Format
**Part of code:**
```
FUNC = ZHI.members.followers

FETCH_BODY = [{"identifier": 'zhang-jia-wei',
                   "query_args": ["following_count"], "range":[0, 1]},
                  {"identifier": 'imike', "range": [0, 21, 20, 2]}, ]
```
**Outputs:**
```
{
    'zhang-jia-wei':
    {
        'paging':
        {
            'is_end': False,
            'is_start': True,
            'next': 'https://www.zhihu.com/members/zhang-jia-wei/followers?include=data%5B%2A%5D.following_count&limit=2&offset=2',
            'previous': 'https://www.zhihu.com/members/zhang-jia-wei/followers?include=data%5B%2A%5D.following_count&limit=2&offset=0',
            'totals': 2262395,
            'identifier': 'zhang-jia-wei'
        },
        'data': [
        {
            'id': 'c69fe0f07b2f640c2829e572251065bb',
            'url_token': 'xia-xia-18-24',
            'name': '夏夏',
            'use_default_avatar': False,
            'avatar_url': 'https://pic4.zhimg.com/v2-cc413975144e318f7f2d72ca03133e92_is.jpg',
            'avatar_url_template': 'https://pic4.zhimg.com/v2-cc413975144e318f7f2d72ca03133e92_{size}.jpg',
            'is_org': False,
            'type': 'people',
            'url': 'https://www.zhihu.com/people/xia-xia-18-24',
            'user_type': 'people',
            'headline': '',
            'gender': -1,
            'is_advertiser': False,
            'vip_info':
            {
                'is_vip': False,
                'rename_days': '60'
            },
            'badge': [],
            'is_following': False,
            'is_followed': False,
            'follower_count': 0,
            'answer_count': 0,
            'articles_count': 0
        },]
    },
    'imike':
    {
        'paging':
        {
            'is_end': False,
            'is_start': True,
            'next': 'https://www.zhihu.com/members/imike/followers?limit=2&offset=2',
            'previous': 'https://www.zhihu.com/members/imike/followers?limit=2&offset=0',
            'totals': 860744,
            'identifier': 'imike'
        },
        'data': [
        {
            'id': 'c78a6368017b0da1ac95a0ba08b808b8',
            'url_token': 'twotk',
            'name': 'Mist',
            'use_default_avatar': False,
            'avatar_url': 'https://pic3.zhimg.com/v2-ee24360e1c36b01755fd224c0e27d00a_is.jpg',
            'avatar_url_template': 'https://pic3.zhimg.com/v2-ee24360e1c36b01755fd224c0e27d00a_{size}.jpg',
            'is_org': False,
            'type': 'people',
            'url': 'https://www.zhihu.com/people/twotk',
            'user_type': 'people',
            'headline': '正在牙牙学语',
            'gender': 1,
            'is_advertiser': False,
            'vip_info':
            {
                'is_vip': False,
                'rename_days': '60'
            }
        },
        {
            'id': 'c4fcea123c0bd07849031b78a4c3c7bf',
            'url_token': 'mimosa-81-23',
            'name': 'Mimosa',
            'use_default_avatar': False,
            'avatar_url': 'https://pic4.zhimg.com/v2-aa18ca0797f565abe8d416a3cbe4a487_is.jpg',
            'avatar_url_template': 'https://pic4.zhimg.com/v2-aa18ca0797f565abe8d416a3cbe4a487_{size}.jpg',
            'is_org': False,
            'type': 'people',
            'url': 'https://www.zhihu.com/people/mimosa-81-23',
            'user_type': 'people',
            'headline': '苦逼的留学生',
            'gender': 1,
            'is_advertiser': False,
            'vip_info':
            {
                'is_vip': False,
                'rename_days': '60'
            }
        },
        {
            'id': '5d80d77df933455265e2ec5887a6d023',
            'url_token': 'zhao-yin-xuan-8',
            'name': '赵梓荀',
            'use_default_avatar': False,
            'avatar_url': 'https://pic2.zhimg.com/v2-72aeaa6a0a6d7c9458da5c6b1f24e21d_is.jpg',
            'avatar_url_template': 'https://pic2.zhimg.com/v2-72aeaa6a0a6d7c9458da5c6b1f24e21d_{size}.jpg',
            'is_org': False,
            'type': 'people',
            'url': 'https://www.zhihu.com/people/zhao-yin-xuan-8',
            'user_type': 'people',
            'headline': '好奇大千世界',
            'gender': 0,
            'is_advertiser': False,
            'vip_info':
            {
                'is_vip': False,
                'rename_days': '60'
            }
        }]
    }
}
```

**Part of code:**
```
FUNC = ZHI.questions.log

FETCH_BODY = [{"identifier": 334583368}, ]
```
**Outputs:**
```
{
    334583368:
    {
        'identifier': 334583368,
        'html': '<!DOCTYPE html><html lang="zh-CN"><body></body></html>'
    }
}
```
## Others

*The following statements are translated by youdao*

The crawler is asynchronous multi-process crawler, efficient and easy to use, easy to expand

It is recommended to set up storage locally, and not to cause too much unnecessary pressure on the servers of zhihu

The crawler only warns of HTTP errors and does not stop running

Please use the browser to log in zhihu and manually pass the man-machine verification.

If you encounter a quick jump in the human-machine verification interface, please press Esc to stop

It is recommended to crawl the content in batches, and control 'task_count' of each batch within 100000

Some apis do not require cookie to simulate login, and this crawler USES cookie by default

If you have personalized requirements, you can directly modify the source code

Any Suggestions from the visitors are welcome

Star this repo if you think it`s OK~

zhihu[@stringstrange](https://www.zhihu.com/people/.people./activities).
