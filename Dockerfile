FROM mandrx/azure-iot-sdk-python-arm 
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:ubuntu-raspi2/ppa
RUN apt-get update
RUN apt-get -y install libraspberrypi-dev
RUN apt-get -y install python3-pip libttspico-utils espeak 
RUN apt-get -y install software-properties-common python-software-properties
RUN apt-get -y install alsa-utils
RUN sudo pip3 install pyttsx3
WORKDIR /   
COPY *.py ./
ENTRYPOINT ["python3","-u","main.py"]