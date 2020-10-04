echo "Starting sync"
aws s3 sync /opt/factorio/saves s3://ryan-factorio-bucket/saves
echo "Finished Sync"
