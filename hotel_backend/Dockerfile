FROM python:3.12

WORKDIR /usr/src/hotel_backend

# Install dependencies
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/hotel_backend/entrypoint.sh
RUN chmod +x /usr/src/hotel_backend/entrypoint.sh
RUN ./entrypoint.sh
# Copy application code
COPY . .

# Expose the application port
EXPOSE 8000

# Run the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
