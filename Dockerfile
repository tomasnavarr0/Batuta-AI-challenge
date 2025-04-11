FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "chainlit run app.py -w --root-path"]
