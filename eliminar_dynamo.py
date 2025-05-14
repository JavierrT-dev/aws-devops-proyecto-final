import boto3

dynamodb = boto3.client('dynamodb')

# Eliminar usuario
dynamodb.delete_item(
    TableName='UsuariosLuis',
    Key={'usuario_id': {'S': 'u001'}}
)

print("✅ Usuario eliminado correctamente.")

