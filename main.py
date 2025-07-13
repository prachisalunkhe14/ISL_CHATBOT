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

# Register the router
app.include_router(infobot_router, prefix="/infobot")

@app.get("/")
def root():
    return {"message": "ISL Chatbot running!"}
