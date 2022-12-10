import aiohttp
import asyncio

async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        # session.post('https://www.httpbin.org/post', data=b'data')
        # session.put('https://www.httpbin.org/put', data=b'data')
        # session.delete('https://www.httpbin.org/delete')
        # session.head('https://www.httpbin.org/get')
        # session.options('https://www.httpbin.org/get')
        # session.patch('https://www.httpbin.org/patch', data=b'data')
        async with session.get('https://www.httpbin.org/get', params=params) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())