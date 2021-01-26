# PollWorldBackend
Server-side django application for PollWorld project

To run current released version of app from any place without repository files:  
docker pull dani6666/poll_world_server  
docker run -d -p 8000:8000 dani6666/poll_world_server python manage.py runserver 0.0.0.0:8000  

Then server will listen on port 8000
