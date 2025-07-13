from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

# Configure API key
genai.configure(api_key="AIzaSyBuP5FOn21QnUBZn_qIGWjlu5PB7oBXN54")

class Query(BaseModel):
    text: str

@router.post("/query")
async def infobot(query: Query):
    """
    Responds with informative answers about ISL.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"You are an expert in Indian Sign Language. Explain: '{query.text}'"
        response = model.generate_content(prompt)
        return {"infobot_response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
