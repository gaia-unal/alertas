from fastapi import FastAPI
from routers import session, session_collection, beacon_collection

app = FastAPI()

app.include_router(session.router)
app.include_router(session_collection.router)
app.include_router(beacon_collection.router)
