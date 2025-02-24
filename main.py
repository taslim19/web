import uvicorn
import os
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from akenoai import AkenoXToJs  # Import the class correctly

# Create FastAPI app
fast_app = FastAPI()

# Add CORS Middleware
fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Initialize AkenoXToJs instance with connect()
js = AkenoXToJs().connect()

# Ensure the downloader module is created
js.downloader.create()

# Fetch API Key correctly
api_key = os.getenv("akeno_aO3VrXPCLGlho0ul6gkfO7C5bC8zTFUm")  # Ensure you use the correct environment variable name


# Tiktok Downloader
async def TiktokDownloader(url: str):
    return await js.downloader.create(
        "dl/tiktok-dl",
        api_key=api_key,
        url=url
    )


# Facebook Downloader
async def FbDownloader(url: str):
    return await js.downloader.create(
        "dl/snapsave",
        api_key=api_key,
        url=url
    )


# Terabox Downloader
async def TeraboxDownloader(url: str):
    return await js.downloader.create(
        "dl/terabox-dl",
        api_key=api_key,
        url=url
    )


# API Endpoints
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
     return await js().randydev(  # Instantiate js before using
        "ai/cohere/command-plus",
        api_key=api_key,
        query=query,
        chatHistory=[],
        system_prompt="You are a helpful AI assistant designed to provide clear and concise responses."
    )


# Test API Route
@fast_app.get("/test")
async def example_json():
    async with js.fasthttp().ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            data = await response.json()
            title = data.get("title", "No Title Found")
    return {"message": title}


if __name__ == "__main__":
    uvicorn.run("main:fast_app", host="0.0.0.0", port=8000, reload=True)
