
#!/bin/bash
docker-compose down
git checkout HEAD~1
docker-compose up -d
