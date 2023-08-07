# Use the official Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Define a volume at /app
VOLUME /app 

# Install curl and other dependencies
RUN apt-get update && apt-get install -yq curl \
    wget \
    gnupg \
    unzip

# Install any necessary Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -yq google-chrome-stable

# Fetch the latest version of ChromeDriver that is compatible with the installed version of Google Chrome
RUN CHROME_VERSION=$(google-chrome-stable --product-version | awk -F'.' '{ print \$1 "." \$2 }') \
    && CHROME_DRIVER_VERSION=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}) \
    && wget -q --show-progress -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver_linux64.zip

# Set the command to run your Python application
CMD ["python", "loop.py"]

#  114.0.5735.199