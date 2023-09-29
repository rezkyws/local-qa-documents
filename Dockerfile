FROM python:3.10.9

RUN mkdir app
COPY ./ /app
WORKDIR /app
RUN pip install -r ./requirements/base.txt

CMD ["python3", "server.py", "build_ext", "--inplace"]