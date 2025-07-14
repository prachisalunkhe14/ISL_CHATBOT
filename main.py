from fastapi import FastAPI
from InfoChatbot import router as infobot_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from ISL Chatbot!"}



# Register the router
app.include_router(infobot_router, prefix="/infobot")

@app.get("/")
def root():
    return {"message": "ISL Chatbot running!"}
