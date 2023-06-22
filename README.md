# CSVRepo
CSVRepo is an AWS-based project that leverages various AWS services for efficient management of CSV files. It enables operations like uploading, downloading, and removing files. All files are stored in an `S3` bucket and managed using `DynamoDB`. The implementation utilizes `Lambda functions` and `API Gateway` for seamless operations. `SNS` and `SQS` services are employed for email notifications to users regarding specific actions. The system caters to three types of users, each with distinct permissions. Additionally, it incorporates registration and login functionalities. 

* The next diagram shows how system compnent and how they are integrate with each other  

![237532181-608b3b0e-76f1-4de7-b506-92beda18b29e](https://github.com/yaseen-asaliya/CSVRepo-With-AWS/assets/59315877/90223b1e-07ec-46be-9597-785527325578)

* users 
```
yaseen-full
Yaseen@2001

yaseen-read-add
Yaseen@2001

yaseen-read
Yaseen@2001
```
