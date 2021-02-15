FROM python:3
MAINTAINER "chengchaos@outlook.com"
ENV PIPURL "https://pypi.tuna.tsinghua.edu.cn/simple"
WORKDIR /Projects

COPY ["requirements.txt", "*.py", "./"]
RUN pip --no-cache-dir install -i ${PIPURL} --upgrade pip && \
    pip --no-cache-dir install -r requirements.txt -i ${PIPURL}

#COPY *.py ./
#CMD gunicorn  -c gun.conf app:app
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]