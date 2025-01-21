# Lambda-fucntion-to-Read-data-from-s3-and-write-it-in-DynamoDB

1. Create a DynamoDB Table and add partition key as id.
2. Create two S3 Buckets
3. Add .CSV Files into those s3 buckets.
4. Create Lambda fucntion and Create a new IAM Role.
5. Add policies to access DynamoDB,S3  and a custom policy which will allow only the data from s3 bucket 1.
6. Test the fucntion by creating a Test event as S3 PUT.
7. Replace the bucket name in the event
8. Add .csv file name as key_name
9. Create step fucntions
10. Add Lmabda invoke and select the lambda fucntion
11. Execute the step fucntion
12. Give input and then Execute 
