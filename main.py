from fastapi import FastAPI
from pydantic import BaseModel
import requests
from task1_price_gap_pair import find_price_gap_pair   # we’ll reuse your Task 1 function

app = FastAPI()


class PriceGapInput(BaseModel):
    nums: list[int]
    k: int


@app.post("/api/price-gap-pair")
def price_gap_pair(data: PriceGapInput):
    pair = find_price_gap_pair(data.nums, data.k)
    if pair is None:
        return {"pair": None}
    i, j = pair
    return {"pair": [i, j], "values": [data.nums[i], data.nums[j]]}


@app.get("/api/movies")
def get_movies(q: str):
    api_key = "demo"  
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": q}
    r = requests.get(url, params=params)
    if r.status_code != 200:
        return {"error": "API failed"}
    data = r.json()
    movies = [{"title": m.get("title")} for m in data.get("results", [])]
    return {"results": movies}
