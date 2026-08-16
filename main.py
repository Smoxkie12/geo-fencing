from pathlib import Path
import json
import math
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "database.json"
HTML_FILE = BASE_DIR / "index.html"
# CSS_FILE = BASE_DIR / "style.css"
# SCRIPT_FILE = BASE_DIR / "script.js"

app = FastAPI()

class LocationPayload(BaseModel):
    latitude: float
    longitude: float
    accuracy: int
    timestamp: str


def default_database() -> dict:
    return {
        "office": {
            "latitude": 18.491256079845726,
            "longitude": 73.85505103564057,
            "radius": 60
        },
        "locations": []
    }


def load_database() -> dict:
    if not DATA_FILE.exists():
        save_database(default_database())

    try:
        with DATA_FILE.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (json.JSONDecodeError, OSError):
        data = default_database()
        save_database(data)

    if "office" not in data or "locations" not in data:
        data = default_database()
        save_database(data)

    return data


def save_database(data: dict) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371000.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


@app.get("/")
async def read_index():
    if not HTML_FILE.exists():
        raise HTTPException(status_code=404, detail="geo.html not found")
    return FileResponse(HTML_FILE)


@app.post("/api/check-location")
async def check_location(payload: LocationPayload):
    data = load_database()
    office = data["office"]

    distance_m = haversine_distance(
        payload.latitude,
        payload.longitude,
        office["latitude"],
        office["longitude"],
    )
    inside = distance_m <= office["radius"]
    record = {
        "latitude": payload.latitude,
        "longitude": payload.longitude,
        "accuracy": payload.accuracy,
        "timestamp": payload.timestamp,
        "distance_m": round(distance_m, 2),
        "radius_m": office["radius"],
        "inside": inside,
    }

    data["locations"].append(record)
    save_database(data)

    return {
        "inside": inside,
        "distance_m": round(distance_m, 2),
        "radius_m": office["radius"],
        "message": "Permit" if inside else "Denied"
    }
