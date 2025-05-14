import boto3

dynamodb = boto3.client('dynamodb')

# Crear tabla
tabla = dynamodb.create_table(
    TableName='UsuariosLuis',
    KeySchema=[
        {'AttributeName': 'usuario_id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'usuario_id', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("✅ Tabla 'UsuariosLuis' creada correctamente.")

