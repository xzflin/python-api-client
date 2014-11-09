# Cloud Academy API client

## API Keys
You can find your API keys at https://cloudacademy.com/settings/#developers

## Inizialization
```
>>> import cloudacademy
>>> access="YjlhZWFkMDEwNmM3ZDZiZjFkMzk5ODI3MmY2M2Q5ZTEyZGNmODZmNA"
>>> secret="MDM3YTZjYzFhNzdhNDA1MmFhZjVjMDgzNWE0NWMxOTFhM2Q0ZjU2Mw"
>>> ca = cloudacademy.CloudAcademy(access,secret)
>>> print ca
<cloudacademy.CloudAcademy object at 0x10cf74110>
```

## First call
```
>>> tags=ca.tags.get(chars="aws")
>>> tags
{u'items': [{u'parent': None, ... u'name': u'AWS General'}], u'tot': 2}
```

## Listing courses
```
>>> amazon_aws_courses=ca.courses.get(provider="5242fc36af1762274b68951f")
>>> for course in amazon_aws_courses['items']: 
...     print course['title']
...
Load Balancing with ELB
Introduction to IAM
Databases on AWS - part 2
Databases on AWS - part 1
Understanding VPC
How to install and run Wordpress on AWS
How to use the AWS Command Line Interface
AWS Automation: how to use CloudFormation
```

## Quiz Example

```
aws = "5242fc36af1762274b68951f"
exit=False

while not exit:
    quiz = ca.quiz.get(provider_id=aws)
    print quiz['description']
    for answer in quiz['answers']:
        print " [%(id)s] %(description)s" % answer
    print
    
    user_answer = None
    while not user_answer:
        try:
            user_answer = int(raw_input("Your answer: "))
        except KeyboardInterrupt:
            exit=True
            break
        except:
            user_answer = None
            
        if user_answer not in [a['id'] for a in quiz['answers']]:
            user_answer = None
            
    if not exit:
        result = ca.quiz_answer.post(
                    quiz_id=quiz['_id'],
                    action="answer",
                    answer_id=user_answer)
        print result['msg']
        print
```