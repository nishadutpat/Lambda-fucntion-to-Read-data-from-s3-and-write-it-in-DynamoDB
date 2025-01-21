import boto3
import json

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TaskTable")

def lambda_handler(event, context):
  
    print("Received event:", json.dumps(event))  

 
    if 'Records' not in event or not event['Records']:
        print("No records found in the event.")
        return {"status": "error", "message": "No records found in the event."}
    
    for record in event['Records']:
        
        bucket_name = record['s3']['bucket']['name']
        s3_file_name = record['s3']['object']['key']
        
    
        if bucket_name == 'taskbuck2':
            print(f"Access Denied: Lambda is not allowed to process files from {bucket_name}")
            raise Exception(f"Access Denied: Lambda is not allowed to process files from {bucket_name}")
        
        
        if bucket_name == 'taskbucket123':
            try:
                
                resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
                data = resp['Body'].read().decode("utf-8")
                
             
                students = data.split("\n")
                
               
                for stud in students:
                    if not stud.strip():  
                        continue
                    stud_data = stud.split(",")
                    if len(stud_data) == 3:  
                        table.put_item(
                            Item={
                                "id": stud_data[0],
                                "name": stud_data[1],
                                "Subject": stud_data[2]
                            }
                        )
                    else:
                        print(f"Skipping invalid record: {stud}")
            except Exception as e:
                print(f"Error processing file from bucket '{bucket_name}': {str(e)}")
                return {"status": "error", "message": str(e)}
    
    return {"status": "success", "message": "Processed successfully"}
