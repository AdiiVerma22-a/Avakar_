FROM python:3.7

RUN pip install Flask gunicorn

RUN pip install Flask==1.1.2

RUN pip install Flask-Uploads

RUN pip install gunicorn==19.9.0

RUN pip install itsdangerous==1.1.0

RUN pip install Jinja2==2.10.1

RUN pip install MarkupSafe==1.1.1

RUN pip install Werkzeug==0.15.5

RUN pip install numpy==1.18.5

RUN pip install scipy==1.5.0

RUN pip install scikit-learn==0.23.1

RUN pip install matplotlib==3.2.2

RUN pip install pandas==1.0.5

RUN pip install librosa==0.7.2

RUN pip install numba==0.48

RUN pip install tensorflow==2.1.0

RUN pip install keras==2.3.1

COPY src/ app/
WORKDIR /app

ENV PORT 8080

CMD exec guniccorn --bind :$PORT --workers 1 --threads 8 app:app

