# Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
# файле, название которого соответствует названию изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и
# асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через
# аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.


import asyncio
import aiohttp
import time
import aiofiles
from sys import argv


urls_im = ['https://cdn21vek.by/img/galleries/6342/650/preview_b/20om204_krugozor_01_60069054f35ee.jpeg',
        'https://cdn21vek.by/img/galleries/343/568/preview_b/artmotionsnow31720555r1691t_belshina_56cac9bb56595.jpeg',
        'https://cdn21vek.by/img/galleries/6259/885/preview_b/vc5420nnts_lg_60068953065d3.jpeg',
        'https://cdn21vek.by/img/galleries/5926/734/preview_b/dx700_deerma_5e6f4339f11ff.png',
        'https://cdn21vek.by/img/galleries/6038/186/preview_b/demf628s_deerma_5eea07ecdf291.jpeg',
        'https://cdn21vek.by/img/galleries/6999/983/preview_b/electrictoothbrushp20c_infly_63ae968ad6259.jpeg',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            start_l = time.time()
            if response.status == 200:
                content = await response.read()
                filename = url.split('/')[-1]
                async with aiofiles.open(filename, 'wb') as f:
                    await f.write(content)
                    print(f"Downloaded {filename} in  {time.time() - start_l} seconds")



async def main(urls):
    start_prog = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Program end in  {time.time() - start_prog} seconds")


if __name__ == '__main__':
    asyncio.run(main(urls_im))
    res = argv
    no, *urls = res
    asyncio.run(main(urls))