# Backend Engineering Take-Home Challenge For Eikon Therapeutics

### Requirements
- Docker

### Steps:
1. Need to run the Postgres docker container first with this command:
	docker run -itd -e POSTGRES_USER=robin -e POSTGRES_PASSWORD=lee123 -e POSTGRES_DB=postgres_db --net=host --name postgresql postgres

2. Need to build the Docker Image:
	docker build --tag python-application .
	
3. Run the docker image:
	docker run -itd --net host --name python python-application


docker network create net
docker network connect net python
docker network connect net postgresql

docker exec -it python curl localhost:8080/db/init 


4. Access Application:
	1. Load the Database 							-> http://localhost/db/init
	2. Total experiments a user ran.				-> http://localhost/user/<user>/experiments/
	3. Average experiments amount per user. 		-> http://localhost/user/<user>/average_experiments/
	4. User's most commonly experimented compound. 	-> http://localhost/user/<user>/compound/

## Useful commands:
To visualize the DB:
docker exec -it postgresql psql -U robin -d postgres_db -c "SELECT * FROM Users;"
docker exec -it postgresql psql -U robin -d postgres_db -c "SELECT * FROM User_Experiments;"
docker exec -it postgresql psql -U robin -d postgres_db -c "SELECT * FROM Compounds;"