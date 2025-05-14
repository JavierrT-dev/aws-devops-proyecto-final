import boto3

# Parámetros
bucket_name = 'bucket-luis-devops'  # cámbialo si tu bucket se llama diferente
archivo_local = 'archivo-ejemplo.txt'
nombre_en_s3 = 'archivos/archivo-ejemplo.txt'

# Cliente S3
s3 = boto3.client('s3')

# Subir archivo
s3.upload_file(archivo_local, bucket_name, nombre_en_s3)

print(f'Archivo subido como {nombre_en_s3} en el bucket {bucket_name}')

