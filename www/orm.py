
__author__ = 'superman'

import asyncio, logging, aiomysql

'''
创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据连接。
使用连接池好处是不必频繁打开和关闭数据库连接，而是能复用就复用
'''
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('Create database connection on pool...')
    global __pool #连接池由全局变量__pool存储
    __pool = yield from aiomysql.create_pool(
        host = kw.get('host', 'localhost'),
        port = kw.get('port', 3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('autocommit', True),
        maxsize = kw.get('maxsize', 10),
        misize = kw.get('minsize', 1),
        loop = loop
    )