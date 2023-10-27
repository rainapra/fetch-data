# fetch-data
write a small application that can read from an AWS  SQS Queue, transform that data, then write to a Postgres database

Steps to execute full code (python files, container on docker)
Install the required Python packages using pip:
pip install -r requirements.txt

Set up the local development environment using Docker Compose:
docker-compose up -d

Read a message from the queue using awslocal:(not working in my case due to aws cli not recognised error)
awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue

Connect to the PostgreSQL database and verify the table is created:
psql -d postgres -U postgres -p 5432 -h localhost -W

Run the following SQL command:
SELECT * FROM user_logins;

Following are some of the files in this project:
app: The main application folder containing the source code in Python for the ETL pipeline.
main.py: The main script in Python for executing the ETL pipeline.
masking.py: Module responsible for masking PII data.
postgres.py: Module responsible for connecting to the PostgreSQL database and inserting records.
sqs.py: Module responsible for reading messages from the SQS Queue.
docker-compose.yml: Docker Compose configuration file to set up the local development environment.
