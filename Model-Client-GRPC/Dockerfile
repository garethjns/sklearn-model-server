FROM python:3.6
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt --trusted-host pypi.python.org
CMD ["python", "/code/run.py"]