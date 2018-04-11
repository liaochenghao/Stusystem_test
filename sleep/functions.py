import requests
import logging

from SleepTest.settings import APP_ID, APP_SECRET
from rest_framework import exceptions

logger = logging.getLogger('django')


def code_authorize(code):
    """用code获取认证"""
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    params = {
        'appid': APP_ID,
        'secret': APP_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }
    response = requests.get(url, params)
    if response.status_code != 200:
        logger.info('WxInterface code_authorize response: %s' % response.text)
        raise exceptions.ValidationError('连接微信服务器异常')
    res = response.json()
    if not (res.get('access_token') and res.get('openid')):
        raise exceptions.ValidationError('无效的code值, 微信网页认证失败')
    return res


def get_user_info(access_token, openid):
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" % (access_token, openid)
    res = requests.get(url, params={})
    return res.json()
