from akenoai import AkenoXToJs as js
from akenoai.runner import run_fast

fast_app = js.get_app()
js.add_cors_middleware()

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

@fast_app.get("/test")
async def example_json():
    async with js.fasthttp().ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            title = js.dict_to_obj(await response.json()).title
    return {"message": title}

run_fast(build=fast_app)
