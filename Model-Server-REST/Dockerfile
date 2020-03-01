FROM python:3.6
EXPOSE 8000
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt --trusted-host pypi.python.org
CMD ["/code/run.sh"]
