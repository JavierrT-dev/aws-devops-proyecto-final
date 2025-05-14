import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')

# Obtener instancias
instances = ec2.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        print(f"📊 Reporte para la instancia: {instance_id}")

        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=datetime.utcnow() - timedelta(hours=1),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=['Average']
        )

        datapoints = metrics['Datapoints']
        if datapoints:
            for point in datapoints:
                print("Uso promedio de CPU:", round(point['Average'], 2), "%", "→ Tiempo:", point['Timestamp'])
        else:
            print("No hay datos de CPU disponibles.\n")

