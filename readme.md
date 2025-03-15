### 1. Add .env file

### 2. Build Container
docker build -t uptime_app .
### 3. Run Container
docker run -d --name uptime_app_container -p 80:80 uptime_app