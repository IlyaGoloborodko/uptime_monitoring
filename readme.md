### 1. DB
The database must be located separately
### 2. Add .env file

### 3. Build Container
docker build -t uptime_app .
### 4. Run Container
docker run -d --name uptime_app_container -p 80:80 uptime_app