from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks, document
from fastapi import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(challenge.router, prefix="/api")
app.include_router(webhooks.router, prefix="/webhooks")
app.include_router(document.router)

@app.middleware("http")
async def add_student_id_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "BSCS23031"
    return response
