FROM python:3

WORKDIR /django

# Don't silence django output
ENV PYTHONUNBUFFERED 1

# Copy the requirements
COPY requirements.txt .

# and install the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy every other file / directory
COPY ./backend ./backend

# Run the server
CMD python backend/manage.py runserver 0.0.0.0:8000
