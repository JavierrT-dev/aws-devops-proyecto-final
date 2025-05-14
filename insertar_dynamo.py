import boto3

dynamodb = boto3.client('dynamodb')

# Insertar un usuario
dynamodb.put_item(
    TableName='UsuariosLuis',
    Item={
        'usuario_id': {'S': 'u001'},
        'nombre': {'S': 'Luis Tamez'},
        'correo': {'S': 'luis@example.com'}
    }
)

print("✅ Usuario insertado correctamente.")

