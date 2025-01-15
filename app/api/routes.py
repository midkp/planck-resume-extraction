from fastapi import FastAPI
from app.controller.year_controller import check_leap_year, check_prime
from app.controller.string_controller import string_split_join
from app.dependencies.schema import YearRequest

app = FastAPI()

# Route for checking leap year
@app.post("/check-leap-year/")
async def check_leap_year(request: YearRequest):
    return await check_leap_year(request)

# Route for checking prime year
@app.post("/check-prime/")
async def check_prime(request: YearRequest):
    return await check_prime(request)

# Route for string split and join
@app.post("/string-split-join/")
async def string_split_join(request: YearRequest):
    return await string_split_join(request)

