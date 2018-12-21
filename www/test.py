import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop, user='root', password='888999', db='awesometest')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test finished!')
    loop.close()

'''
import orm
import asyncio,random,string
from models import User, Blog, Comment,next_id

def random_email():
    qq = random.randint(100000000, 999999999)
    return str(qq)+'@qq.com'

def random_name():
    return ''.join(random.sample(string.ascii_letters, 5))
async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='888999', db='awesometest')

    u = User(name='Rambo', email='1434284872@qq.com', passwd='123456', image='about:blank')

    #1. 测试插入方法
    # for x in range(100):
    #     u['id'] = next_id()
    #     u['email'] = random_email()
    #     u['name'] = random_name()
    #     await u.save()

    #2. 测试根据主键查询方法
    # u = await User.find('0015452734508517676e9987a094be6b017ef19f97e58db000')

    #3. 测试根据参数查询方法
    #u = await User.findAll(where='name like ?', args=['%a%'], orderBy='name asc', limit=(0, 10))

    #4. 测试findNumber方法，不知道这个方法有什么用
    #u = await User.findNumber('name')

    #5. 测试更新方法
    # u = await User.find('0015452734508517676e9987a094be6b017ef19f97e58db000')
    # u['passwd'] = '123'
    # await u.update()

    #6. 测试删除方法
    u = await User.find('0015452782688867d6a4740601d4022b048312d2511dee4000')
    await u.remove()

    print(u)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.run_forever()
'''
