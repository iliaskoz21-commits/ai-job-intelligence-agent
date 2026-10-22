from fastapi import FastAPI

app = FastAPI(
    title="AI Job Intelligence Agent",
    description="An AI-powered assistant for job analysis and career matching.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Job Intelligence Agent is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
