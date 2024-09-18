FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY MainScores.py /app/
COPY Scores.txt /app/Scores.txt
RUN pip install --no-cache-dir flask
EXPOSE 5000
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python", "-m", "flask", "run"]