from typing import Optional

from fastapi import FastAPI, Request
from typing import Any, Dict
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import pandas as pd
import pickle
import numpy as np
from sklearn.tree import DecisionTreeRegressor
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post('/models/WC_RZM7N59B/v4.1/predictrtw')
async def predictrtw(request: Request):
  data = await request.json()
  #test_json = request.get_json()
  json_test = pd.DataFrame(data)
  from predictrtw import predictrtw
  df = predictrtw(json_test)
  return JSONResponse(df, status_code=200, headers=None,media_type='application/json')
  




@app.post('/models/WC_RZM7N59B/v5.1/predictrtw')
async def predictrtw(request: Request):  
  data = await request.json()
  json_test = pd.DataFrame(data)
  from predictrtw import predictrtw
  df = predictrtw(json_test)
  return JSONResponse(df,status_code=200, headers=None,media_type='application/json')




@app.post('/models/WC_VSJPE6X4/v9.1/predictrtw')
async def predictrtw(request: Request):  
  data = await request.json()
  json_test = pd.DataFrame(data)
  from predictrtw import predictrtw
  df = predictrtw(json_test)
  return JSONResponse(df,status_code=200, headers=None,media_type='application/json')


