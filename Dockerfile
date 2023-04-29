# Use the official AWS Lambda base image for Python
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory in the container
WORKDIR /var/task

# Copy the Python code and dependencies to the container
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./

# Set the Lambda handler
CMD ["entry.handler"]
