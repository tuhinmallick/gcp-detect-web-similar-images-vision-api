FROM python:3.9-slim
ENV PYTHONUNBUFFERED True

WORKDIR "/demo"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 80

CMD python ./ui.py
