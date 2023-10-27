from fastapi import FastAPI
import uvicorn

from fruits import router

app = FastAPI()

app.include_router(router)

uvicorn.run("main:app", reload=True)
