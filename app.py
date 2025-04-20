from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import random

app = FastAPI()

# Endpoint to roll a standard 6-sided die
@app.get("/roll-dice/", response_class=JSONResponse)
async def roll_dice():
    outcome = random.randint(1, 6)
    return {"dice_type": "6-sided", "outcome": outcome}

# Endpoint to roll a custom-sided die (e.g., 10-sided)
@app.get("/roll-dice/{sides}", response_class=JSONResponse)
async def roll_custom_dice(sides: int):
    if sides < 2:
        return JSONResponse(
            status_code=400,
            content={"error": "Dice must have at least 2 sides."}
        )
    outcome = random.randint(1, sides)
    return {"dice_type": f"{sides}-sided", "outcome": outcome}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)