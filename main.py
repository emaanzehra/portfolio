from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Your dynamic profile data
user_info = {
    "name": "Emaan Zehra Butt", 
    "role": "Software Engineer & BSAI Student", 
    "bio": "Driven by the transformative potential of AI, I am committed to building intelligent systems that automate complex decision-making.", 
    "email": "emaanzehrabutt@gmail.com", 
    "github": "https://github.com/emaanzehra", 
    "linkedin": "https://www.linkedin.com/in/emaanzehra/", 
    "skills": ["Python", "FastAPI", "AI/ML", "TensorFlow", "SQL", "Docker"], 
    "education": "BS in Artificial Intelligence (CGPA 3.56/4.00)", 
    "languages": "English (C1), Urdu (Native), German (A1)" 
}

@app.get("/")
async def home(request: Request):
    # CORRECT 
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"user": user_info}
)

@app.get("/download-cv")
async def download_cv():
    return FileResponse("static/Emaan_Zehra_CV.pdf", filename="Emaan_Zehra_CV.pdf")