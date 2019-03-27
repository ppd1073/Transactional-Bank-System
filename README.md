# Transactional-Bank-System
Developed a transactional banking system around Postgre in a Docker container. Implemented python scripts using virtualenv, to establish ODBC connection with the container and populated the database with realistic mock data. Performed PSQL queries on the data.

For this project I used my personal desktop which is Windows 10 OS. Since my version of windows is not enterprise or pro, docker is not compatible. So for previous version docker toolbox was recommended. I installed docker toolbox on my system.

Once docker toolbox was installed, I created the docker file in windows command prompt using command type NUL > Dockerfile, this file installs the latest postgres image and expose the port 5432. In the docker toolbox terminal to build the image through dockerfile, run the command docker build.  , after that with this command:
docker run --name postgres-0 -e POSTGRES_PASSWORD=password -d postgres  the image is given a name as per user along with the password. Here, I have given the image name as postgres-0 and password as the password. To start psql do the following commands: 
docker exec -it postgres-0 bash
psql -U postgres 
This is the process which I carried out to install Postgres. Inside the psql I created and connected to the database with the following command: CREATE DATABASE bank1db;
\c bank1db;  <- this command is for connected to the database

Once docker and Postgres were installed and ready, I shifted towards connectivity between docker and local psql. This was again I struggled a bit. For establishing the connection, the server/ host address was required. To find the docker container’s IP address I used the following command: docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-0 
This command showed the IP address as 172.17.0.2. I initially tried with this address to connect to the server from local psql. However, I was unsuccessful. For cross reference I installed ODBC data sources to connect to the docker container, here as well I failed. On many trial and errors and searches, I found that this is not the address used to connect to the server, it was docker bridge address.

After establishing the connection, I installed virtualenv in anaconda prompt using pip install virtualenv , here first I created a folder named demoVenv in desktop, then through Anaconda command prompt changed the directory to the directory which I created and there run the command virtualenv venv , thus a new virtual environment named venv is created, once the virtual environment is created, to activate it use the following command: C:\Users\Prajakta\Desktop\demoVenv\venv\Scripts\activate . There simply use the command: python test.py 1000 10  to run the python script, where 1000 and 10 are command line arguments.
