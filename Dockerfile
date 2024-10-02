# Base image
FROM python:3.12-alpine

# Install Pipenv
RUN pip install pipenv gunicorn
COPY Pipfile.lock ./
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.app:app"]