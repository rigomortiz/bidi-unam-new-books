# API for find books of the National Autonomous University of Mexico (UNAM)
*Api not official, site web of [libraries of UNAM](http://bibliotecas.unam.mx/)* 

## Run
Build
``` 
sam build --template bidi-unam-new-books.yaml --use-container
```
Run local
```
sam local invoke --template .aws-sam/build/template.yaml --event lambda-event.json 
```
Deploy
```
sam deploy --guided --template-file .aws-sam/build/template.yaml
```
```
sam package --template-file .aws-sam/build/template.yaml --output-template-file .aws-sam/build/packaged-temp-template.yaml --s3-bucket cansecorigoberto
```
```
sam deploy --template-file .aws-sam/build/packaged-temp-template.yaml --stack-name <YOUR STACK NAME>
```

## URL
https://gzirtfkx59.execute-api.us-east-1.amazonaws.com/default/bidi-unam-new-books

## Documentation
AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html  
AWS SAM: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html  
AWS Lambda: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html  
AWS Lambda Python: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html

## License
This code uses the MIT License.  
https://opensource.org/licenses/MIT

[Library Request](https://3.python-requests.org/u)  
https://www.apache.org/licenses/LICENSE-2.0