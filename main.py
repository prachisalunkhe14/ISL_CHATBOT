'''
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

'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from InfoChatbot import router as infobot_router

# ✅ Define your system prompt here
system_prompt = """
You are a helpful and knowledgeable AI chatbot designed to provide information about Indian Sign Language (ISL). You will be asked a variety of questions related to ISL. For each question, follow the instructions regarding the level of detail and the number of lines expected in your response.

1. What is Indian Sign Language? Provide a clear definition and explain its significance. Answer in a simple manner using 3 lines.
2. How is Indian Sign Language different from American Sign Language? Mention one key difference with a brief explanation in 3 lines.
3. Who are the primary users of ISL in India? Describe the user base in 2 simple lines.
4. When was ISL officially recognized in India? Provide a factual response in 2 lines.
5. What are the core components of ISL communication? Explain hand gestures, facial expressions, and body posture in medium detail using 4 lines.
6. What is fingerspelling in ISL? Describe its purpose and when it is used in 3 lines.
7. How is the English alphabet represented in ISL? Provide a general overview in 2 lines.
8. How do you sign the word “Thank you” in ISL? Describe the gesture in a clear and simple way using 3 lines.
9. How would you sign “My name is Priya” in ISL? Break the sentence into parts and explain each in 4 lines.
10. How are the numbers 1 to 5 signed in ISL? Provide a brief description for each number using 5 lines.
11. Why are facial expressions important in ISL? Give two examples to support your explanation in 3 lines.
12. What are five commonly used ISL signs in daily life? List and briefly describe each one in 5 lines.
13. How is ISL taught in schools for the deaf in India? Describe the teaching approach in 3 lines.
14. Name three digital platforms or mobile applications where users can learn ISL. Mention each with a short description in 3 lines.
15. What is the Indian Sign Language Research and Training Centre (ISLRTC)? Explain its mission and activities in 3 lines.
16. How can artificial intelligence support ISL communication? Provide one practical example in 3 lines.
17. What challenges does AI face in recognizing ISL gestures? Mention two key issues in 3 lines.
18. What is the ISL sign for the word “Friend”? Describe the hand shape and motion clearly in 2 lines.
19. How are emotions like “Happy” and “Sad” expressed in ISL? Explain each with one sentence in 4 lines total.
20. How does this AI chatbot assist the deaf and hard-of-hearing community? Provide a summary of its benefits in 4 lines.
"""

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

app.include_router(infobot_router, prefix="/infobot", dependencies=[Depends(lambda: system_prompt)])
