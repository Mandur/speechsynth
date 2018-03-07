FROM vjrantal/azure-iot-sdk-python 
RUN apt-get -y install python3-pip libttspico-utils espeak 
RUN apt-get update
RUN pip3 install pyttsx3
RUN mkdir app
COPY * app/
WORKDIR app
ENTRYPOINT ["python3","main.py"]