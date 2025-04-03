# 🚀 Startup Instructions  

Follow these steps to set up and start your PostgreSQL environment using Docker.  

## 1️⃣ Start Docker Desktop  
Ensure that **Docker Desktop** is running on your machine before proceeding. Then download the code from this code repository.

## 2️⃣ Create Docker Images and Containers  
Delete any other old containers from previous challenges that might be still running.
Run the following command to build and start the containers in **detached mode (-d)**:  

```
docker compose up --build -d
```  

- **`--build`**: Rebuilds images if there are changes.  
- **`-d`**: Runs containers in the background (detached mode).  

## 3️⃣ Access the PostgreSQL Container's Shell  
Once the containers are up, enter the PostgreSQL container using:  

```
docker exec -it inventory_db sh
```  

- **`docker exec`**: Runs a command inside a running container.  
- **`-it`**: Opens an interactive shell.  
- **`inventory_db`**: The name of the PostgreSQL container.  
- **`sh`**: Starts a shell session inside the container.  

## 4️⃣ Connect to PostgreSQL and Select the Database  
After accessing the container, connect to PostgreSQL and select the **inventory** database:  

```
psql -U postgres -d inventory
```  

- **`psql`**: PostgreSQL interactive terminal.  
- **`-U postgres`**: Connects as the `postgres` user.  
- **`-d inventory`**: Selects the `inventory` database.  

---

✅ **You're now connected to PostgreSQL and ready to run queries!**  
