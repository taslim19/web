import uvicorn
import os
import asyncio
from akenoai import AkenoXToJs as js
from akenoai.runner import run_fast

fast_app = js.get_app()
js.add_cors_middleware()

api_key = os.environ.get("akeno_yzpYJoxvTIAK5t5pHDA0QcJNi7gQtcI4")


# Tiktok Downloader
async def TiktokDownloader(url: str):
    response = await js.randydev(
        "dl/tiktok",
        api_key=api_key,
        custom_dev_fast=True,
        url=url
    )
    return response


# Facebook Downloader
async def FbDownloader(url: str):
    response = await js.randydev(
        "dl/fb",
        api_key=api_key,
        custom_dev_fast=True,
        url=url
    )
    return response


# Terabox Downloader (100 max requests per hour)
async def TeraboxDownloader(url: str):
    response = await js.randydev(
        "dl/terabox",
        api_key=api_key,
        custom_dev_fast=True,
        url=url
    )
    return response


# API Endpoints for Downloaders
@fast_app.get("/api/download/tiktok")
async def tiktok_download(url: str):
    return await TiktokDownloader(url)


@fast_app.get("/api/download/facebook")
async def fb_download(url: str):
    return await FbDownloader(url)


@fast_app.get("/api/download/terabox")
async def terabox_download(url: str):
    return await TeraboxDownloader(url)


# Cohere AI API
@fast_app.get("/api/cohere")
async def cohere(query: str):
    return await js.randydev(
        "ai/cohere/command-plus",
        api_key="akeno_Azm11CohMaLg4LTWsUrE1RJjM68L5",
        custom_dev_fast=True,
        query=query,
        chatHistory=[],
        system_prompt="You are a helpful AI assistant designed to provide clear and concise responses."
    )


# Test API Route
@fast_app.get("/test")
async def example_json():
    async with js.fasthttp().ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            title = js.dict_to_obj(await response.json()).title
    return {"message": title}


if __name__ == "__main__":
    uvicorn.run("main:fast_app", host="0.0.0.0", port=8000, reload=True)
