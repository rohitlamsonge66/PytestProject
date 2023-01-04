FROM selenium/standalone-chrome
#RUN apt-get update
#RUN apt-get upgrade

# Update apt packages
RUN sudo apt update
RUN sudo apt upgrade -y

# Install vim
RUN sudo apt install vim -y

RUN sudo apt install software-properties-common -y
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt install python3.7 -y

# Make python 3.7 the default
RUN sudo echo "alias python=python3.7" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.7
RUN sudo /bin/bash -c "source ~/.bashrc"

# Install pip
RUN sudo apt install python3-pip -y
RUN sudo apt update
RUN python3 -m pip install --upgrade pip

# # Install python 3
 RUN python3 --version

# Install Selenium
RUN pip3 install selenium

#Install pytest
RUN sudo pip3 install pytest

# Install Webdriver Manager
RUN pip3 install webdriver-manager

#  Install  pytest parellel execution mode
RUN pip3 install pytest-xdist

RUN echo "******************************************************************************"

# Run the complete project with the thread coun
# #WORKDIR /home/excellarate/PycharmProjects
#
# RUN pwd
# RUN cd /home
# RUN pwd
# RUN ls -a
RUN sudo mkdir /home/PythonPageObjectModel
COPY Config /home/PythonPageObjectModel/Config
COPY Pages /home/PythonPageObjectModel/Pages
COPY Tests /home/PythonPageObjectModel/Tests

RUN pytest --version

WORKDIR /home/PythonPageObjectModel/Tests

RUN pwd

RUN pytest
