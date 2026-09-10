FROM python:3.14-slim

WORKDIR /crud

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /crud/
RUN python -m pip install -U pip
RUN pip install --no-cache-dir -U -r requirements.txt

COPY . /crud/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]