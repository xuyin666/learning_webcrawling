import aiohttp
import asyncio

async def main():
    timeout = aiohttp.ClientTimeout(total=3)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://www.httpbin.org/get') as response:
            print('status:', response.status)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())