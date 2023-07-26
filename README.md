# Backend Engineering Take-Home Challenge For Eikon Therapeutics

### Requirements
- Docker

### Steps:
1. Build the docker images via docker-compose:

	docker-compose build

3. Need to run the Docker Compose:

	docker-compose up -d

4. Access Application:
	1. Load the Database 							-> http://localhost:8080/db/init
	2. Total experiments a user ran.				-> http://localhost:8080/user/{user}/experiments/
	3. Average experiments amount per user. 		-> http://localhost:8080/user/{user}/average_experiments/
	4. User's most commonly experimented compound. 	-> http://localhost:8080/user/{user}/compound/

### Useful commands:
#### To visualize the DB:
1. First get the db name via:
	##### docker ps -a:
<p>
test-postgres-1
</p>

2. Execute the cmd below 

	docker exec -it test-postgres-1 psql -U robin -d postgres_db -c "SELECT * FROM Users;"

	docker exec -it test-postgres-1 psql -U robin -d postgres_db -c "SELECT * FROM User_Experiments;"

	docker exec -it test-postgres-1 psql -U robin -d postgres_db -c "SELECT * FROM Compounds;"

3. To stop the docker-compose:

	docker-compose kill