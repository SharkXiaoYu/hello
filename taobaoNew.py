# 安装问题：raise SSLError(e, request=request)requests.exceptions.SSLError: HTTPSConnectionPool(host='translate.google.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: SysCallError(10054, 'WSAECONNRESET')",),))
# 解决方法：pip install -U pyopenssl


import pyppeteer
import requests
from pyquery import PyQuery as pq

import asyncio
from pyppeteer import launch


# 接下来我们测试下基本的页面渲染操作，这里我们选用的网址为：
# http://quotes.toscrape.com/js/，这个页面是 JavaScript 渲染而成的，
# 用基本的 requests 库请求得到的 HTML 结果里面是不包含页面中所见的条目内容的。
# url = 'http://quotes.toscrape.com/js/'
# response = requests.get(url)
# doc = pq(response.text)
# print('Quotes:', doc('.quote').length)



# 案例一
# 自动下载浏览器地址：
# C:\Users\hasee\AppData\Local\pyppeteer\pyppeteer\local-chromium\575458
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('http://quotes.toscrape.com/js/')
#     doc = pq(await page.content())
#     print('Quotes:', doc('.quote').length)
#     await browser.close()

# 获取EventLoop:  asyncio.get_event_loop()
# 执行corountine:   run_until_complete(main())
# asyncio.get_event_loop().run_until_complete(main())



# 案例二
# async def main():
    # headless参数设为False，则变成有头模式
    # browser = await launch(headless=False, args=['--disable-infobars'])
    # page = await browser.newPage()
    # await page.goto('http://quotes.toscrape.com/js/')
    # await page.screenshot(path='example.png')
    # await page.pdf(path='example.pdf')
    # dimensions = await page.evaluate('''() => {
    #     return {
    #         width: document.documentElement.clientWidth,
    #         height: document.documentElement.clientHeight,
    #         deviceScaleFactor: window.devicePixelRatio,
    #
    #     }
    # }''')

    # print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    # await browser.close()

# asyncio.get_event_loop().run_until_complete(main())


# 案例三，淘宝(1)
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())


# (2)
# width, height = 1366, 768
#
# async def main():
#     browser = await launch(headless=False,
#                            args=[f'--window-size={width},{height}'])
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())


# (3)
width, height = 1366, 768
async def main():
    browser = await launch(headless=False, userDataDir='./userdata', args=[f'--window-size={width},{height}','--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    # await page.goto('https://www.taobao.com')
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
