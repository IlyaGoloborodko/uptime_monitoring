FROM python:3.12

WORKDIR /app

COPY backend/requirements.txt /app/backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/backend/requirements.txt

COPY . /app

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]