import boto3

dynamodb = boto3.client('dynamodb')

# Actualizar correo del usuario
dynamodb.update_item(
    TableName='UsuariosLuis',
    Key={'usuario_id': {'S': 'u001'}},
    UpdateExpression='SET correo = :nuevo',
    ExpressionAttributeValues={':nuevo': {'S': 'nuevo@mail.com'}}
)

print("✅ Usuario actualizado correctamente.")

