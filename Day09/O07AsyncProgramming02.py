
import asyncio

async def download_file(filename, delay):
    print(f"Starting to download the file: {filename}")
    await asyncio.sleep(delay)
    print(f"Finished download: {filename}")
    return f"{filename} downloaded"

async def process_file(filename):
    print(f"Started processing the file :{filename}")
    await asyncio.sleep(2)
    print(f"Completed processing fiel :{filename}")
    return f"{filename} processed"

async def main():
    download_task1 = asyncio.create_task(download_file("myfile1.txt", 2))
    download_task2 = asyncio.create_task(download_file("myfile2.txt", 3))

    result1 = await download_task1
    result2 = await download_task2

    processed1 = await process_file("myfile1.txt")
    processed2 = await process_file("myfile2.txt")

    print("Summary".center(60,"-"))
    print(result1)
    print(result2)
    print(processed1)
    print(processed2)

asyncio.run(main())