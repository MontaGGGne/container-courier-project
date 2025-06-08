FROM python:3.10


COPY ./back /workdir
COPY ./.env /workdir/
COPY ./requirements.in /workdir/
WORKDIR /workdir

RUN python -m pip install pip-tools
RUN pip-compile
RUN pip-sync

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]