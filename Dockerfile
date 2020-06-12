# Most of the time, Alpine is a great base image to start with.
# If we're building a container for Python, we use something different.
# Learn why here: https://pythonspeed.com/articles/base-image-python-docker-images/
# TLDR: Alpine is very slow when it comes to running Python!

# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

# STEP 2: Install required dependencies.
RUN pip install flask
RUN pip install Jinja2
RUN pip install requests
RUN pip install python-dotenv

### NOTE these were not needed!
###ERROR: Could not find a version that satisfies the requirement os (from versions: none)
###ERROR: No matching distribution found for os
###ERROR: Could not find a version that satisfies the requirement json (from versions: none)
###ERROR: No matching distribution found for json
# RUN pip install json
# RUN pip install os

# STEP 3: Copy the source code in the current directory to the container.
# Store it in a folder named /app.
ADD . /app

# STEP 4: Set working directory to /app so we can execute commands in it
WORKDIR /app

# STEP 5: Declare environment variables
ENV TENOR_API_KEY=CIKSZWLE8R9M

# STEP 6: Expose the port that Flask is running on
EXPOSE 5000

# STEP 7: Run Flask!
CMD ["flask", "run", "--host=0.0.0.0"]