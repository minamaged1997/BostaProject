FROM python

WORKDIR /app

COPY python_etl/etl.py .
COPY data /app/data

RUN pip install pandas sqlalchemy psycopg2-binary

CMD ["python", "etl.py"]
