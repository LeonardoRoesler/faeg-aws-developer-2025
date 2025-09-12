import boto3

bucket_name = "leonardoroesler19"
# API de high Level = 
s3 = boto3.resource('s3')

bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    print(f"{obj.key} - Tamanho: {obj.size} bytes")
