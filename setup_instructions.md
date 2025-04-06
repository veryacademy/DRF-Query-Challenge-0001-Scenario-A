# 🚀 Startup Instructions  

Follow these steps to set up and start your **PostgreSQL Django DRF** environment using Docker.  

## **1️⃣ Start Docker Desktop**  
Ensure that **Docker Desktop** is running on your machine before proceeding.  
Then, **clone or download** the code from this repository.  

## **2️⃣ Build and Start Docker Containers**  
Before running the project, **delete any old containers** from previous challenges that might still be running.  
Then, build and start the containers using the following command:  

```sh
docker compose up --build -d
```

### **Explanation of Flags:**  
- **`--build`** → Rebuilds images if changes were made.  
- **`-d`** → Runs containers in the background (detached mode).  

## **3️⃣ Start the Django Challenge**  
Once the containers are up and running, you're ready to begin the challenge!  

- Implement your solution in the challenge_app **`views.py`** inside the provided **ViewSet**.
- You **do not** need to manually add a URL—the system will automatically detect the ViewSet.  
- Open your browser and navigate to:  
  👉 **[`http://localhost:8000/apps`](http://localhost:8000/apps)** to test your queries.  

---

✅ **Good Luck!** 🚀  
