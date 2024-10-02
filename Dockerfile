# Base image
FROM python:3.12

# Install Pipenv
RUN pip install pipenv gunicorn

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application
COPY . .

# Run the app using Gunicorn
CMD ["pipenv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.app:app"]