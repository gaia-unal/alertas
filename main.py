from fastapi import FastAPI
from routers import sessions, session_collection, beacons, beacon_collection

app = FastAPI()

app.include_router(sessions.router)
app.include_router(session_collection.router)
app.include_router(beacons.router)
app.include_router(beacon_collection.router)
