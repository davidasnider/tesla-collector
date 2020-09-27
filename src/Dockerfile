FROM python:3.8-buster as BUILD

COPY requirements.txt /requirements.txt
RUN useradd -m -u 10001 tesla
USER 10001
RUN pip install --user -r requirements.txt


FROM python:3.8-slim-buster as FINAL

RUN useradd -m -u 10001 tesla
USER 10001
COPY --from=BUILD /home/tesla/.local /home/tesla/.local

COPY get_stats.py /get_stats.py
ENV PATH=/home/tesla/.local/bin:$PATH

CMD [ "python3", "/get_stats.py"]
