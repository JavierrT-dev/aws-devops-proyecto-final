import boto3

s3 = boto3.client('s3')

buckets = s3.list_buckets()

print("📦 Buckets en la cuenta:\n")

for bucket in buckets['Buckets']:
    print(f"- {bucket['Name']}")
    print("  Objetos:")
    objects = s3.list_objects_v2(Bucket=bucket['Name'])
    
    if 'Contents' in objects:
        for obj in objects['Contents']:
            print("   ", obj['Key'])
    else:
        print("   (vacío)")
    print("-" * 30)

