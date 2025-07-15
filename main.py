from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from InfoChatbot import router as infobot_router

app = FastAPI()



from fastapi import FastAPI
from InfoChatbot import router as infobot_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "ISL Chatbot running!"}

# Register the router
app.include_router(infobot_router, prefix="/infobot")
