# Video-Service
A self serving api that converts all your video needs.
Ideas: 
- take videos, display kaleidoscope
- take videos from cloud sources (google drive, apple icloud)
- add watermarks
- put it on YouTube with API


### Launch locally
```
docker-compose up
```

## localstack setup
```
aws configure
AWS Access Key ID [None]: not
AWS Secret Access Key [None]: real
Default region name [None]: us-west-2
Default output format [None]: json
```

### create s3 bucket
```
aws --endpoint-url=http://localhost:4566 s3 mb s3://video-service
```

###  list s3 buckets
```
aws --endpoint-url=http://localhost:4566 s3 ls
```