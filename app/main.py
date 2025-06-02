from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import habits, users

app = FastAPI(
  title=settings.APP_NAME,
  version=settings.APP_VERSION,
)

app.include_router(
  habits.router,
)
app.include_router(
  users.router,
)

@app.get("/")
def root():
  return {"message": "Welcome to HabitApp!"}