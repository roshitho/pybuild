FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt ./ 
#RUN pip3 install --no-cache-dir -r 
RUN  pip install -r requirements.txt
COPY ./app /app
