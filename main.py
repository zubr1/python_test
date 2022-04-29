from fastapi import FastAPI, Query, HTTPException
import random


app = FastAPI()


@app.get("/")
async def get_random_number(range: str | None = Query('1-1000', regex="^[0-9]+-[0-9]+$")):
  range_values = range.split('-');
  if int(range_values[0]) > int(range_values[1]):
    raise HTTPException(status_code=400, detail="Second range value must be greater than or equal to the first one.")
  random_number = random.randint(int(range_values[0]), int(range_values[1]));
  return {"random_number": random_number}
