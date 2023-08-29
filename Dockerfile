FROM python:3.8

COPY ./ /
RUN pip install --no-cache-dir -r ./requirements/base.txt
# WORKDIR /app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3345", "--workers", "5"]
CMD ["python3", "server.py", "build_ext", "--inplace"]
