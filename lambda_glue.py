import json
import boto3

def lambda_handler(event, context):
    
    glue_client = boto3.client('glue')
    job_name = 'sombra-bovespa_glue-job'
    
    try:

        response = glue_client.start_job_run(JobName=job_name)
        
        job_run_id = response['JobRunId']
        print(f'Started Glue job {job_name} with JobRunId: {job_run_id}')
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'{job_name} started with JobRunId: {job_run_id}')
        }
    
    except Exception as e:
        print(f'Error starting job: {e}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error starting job: {str(e)}')
        }
