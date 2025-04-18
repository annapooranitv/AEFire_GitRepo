# pull python base image
FROM python:3.10-slim

# copy application files
ADD /AEFire_model_api /AEFire_model_api/

# specify working directory
WORKDIR /AEFire_model_api

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# expose port for application
EXPOSE 9001

# start fastapi application
CMD ["python", "app/main.py"]
