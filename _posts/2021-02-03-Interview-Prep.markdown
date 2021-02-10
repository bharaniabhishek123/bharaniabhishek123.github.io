---
layout: post
title: Interview preparation
---

Experience Learn and Grow Model 

## Introduce Yourself 
<br>
Hi, I am a data engineer currently working for vmware. 
I am part of Data Architecture team responsible to design & manage data systems to get insights from customer data.

Our product "Skyline" help customers avoid problems in their environments.
Skyline uses machine learning to analyze customer data against vmware best practices and give proactive insights to customers.

Skyline advisor let customer view potentional issues and findings and help them to act proactively remediate. 
Log bundle transfer process which is safe and secure. 

we follow ceip and gdpr regulations when collecting data.

I am really excited about using data to help customers, particulary by using data engineering. 
I have helped skyline product base to grow from **2k customer to 10k** customers in the span of 2 years.
</br>

## Tell me about a time when you improved business and engineering team process via data architecture ?
<br>
Sure, last year I gave an idea of doing **cohort anaylsis** between support request (SR) filed by customer on VMware support portal and Skyline collected data. 

Now to give you some context, support request (SR) are logged by customers and they attach log bundles.
Like an aws customer logs a ticket with aws support mentioning the problem faced and product customer is using.

Since, skyline collects customer environment data such as data center topology hostname or virtual machine name. 

**I created the data architecture and the data pipline** for this business problem and compared host/virtual machine names from log-bundle's data and compare with skyline monitored host/virtual machine name. 

The missing data helped our marketing team. They reached out to individual customers to turn-on skyline monitoring on the set of host/virtual machines.

This helped in increasing our customer base (2k to 10k) at the same time engineering support team received less SR's (**helping them reduce by 20% volume**). 
</br>

## Why you want to work at Amazon 
<br>
- answer why amazon fits into career path
Amazon prime video collects huge amount of data, ranging from customer clicks or navigation on prime video app to most watched genre. 
As a data engineer it gives unique opportunity to answer questions with very large dataset. 

I would like to contribute towards refinning and developing data solutions and help meet business goals
by making the data easily available to appropriate teams.

I want to build soltion which impact thousands of customers across the world and learn and grow professionally while working at amazon.
</br>


## Tell me about a time when you were faced with a problem that had a number of possible solutions. What was the problem and how did you determine the course of action? What was the outcome of that choice?

<br>
SITUATION - Recently I was working on a project to ETL topological data using Spark. 
The data here comes from collectors of virtual machines running at customer end and sending via telemetry client. So, assume a big data center which customer is having and this dataset contains all the hostmachines, network devices, storage devices information.  
At each customer end, we run the collector 2-3 times a day.so, we collect **around 200gb** and format is compressed json (so, when you unzip and read it to make it querable it's more than 1tb).

Now, Problem is we have find optimal etl solution so that this data is querable. I had to pick from 5 different possible solutions and choose one which is optimal.

TASK -  Data comes from telemetry service to S3 and each file name is prefixed with customer-id-typeof-product-uuid.
The file is json array with first element as header and remaining elements as body. So consider an array [header, body1, body2, .......body100th].

The ETL process will read all the each json gziped files, extract each body element and store the body part in parquet format.

The ETL should store the data in partitioned manner with structure as below 
  - product-type
    - type-of-payload 
      - customer-id
        - collector-id
          - year-month 
            - <body1.parquet>

I need to compare all 5 solutions and choose the one which is optimal ETL, take less resources and less time to run and is simple enough to present.

ACTION - I started with first solution which took almost 24 hours to finish on EMR clusder with 10 core nodes with r5.4xlarge instances. 
Clearly, it was not acceptable. 
Either I try remaining 4 ETL solutions and do comparision or debug and see what's wrong the first code. 

I started looking into first code explain plan and noticed an expensive operation of dataframe explode.
The explode functions expands an iterable object into multiple rows and same logic was present in other 4 ETL solution as we were just prototyping.

I corrected the code to use reduce operation instead of costly explode operation and then compared with run times of other 4 etl solutions.

RESULT - In the end I got the optimal ETL solution which took close to **2 hours** to run. I shared the learning with my team.
I learned how to optimize and avoid costly operations. I was able to bring down ETL run time by 90% which is a lot of saving.
</br>

## When did you take a risk, make a mistake, or fail? How did you respond, and how did you grow from that experience?Describe a time you took the lead on a project.

<br>
I was working with internal machine learning team to extract support request (SR) data from salesforce. so that, they can train natural language based ml model on it. I made a mistake of not asking about the what distribution of data they need as it was my first time directly working with ml engineer. 



They trained the model on highly skewed data and model accuracy was good on certain set of products but it was not good on other set of products.  In the root cause analysis we got to know that we need rightly distributed data for model training to be successful.
I learned that quality dependes on training data, tunning parameters and it requires constantly evaluate and combine new libraries for same task. We are optimizing for metrics in ML unlike traditional software.

I responded by asking more clarifying questions to the team and learned that in accuracy sensitive projects where success of whole project is dependent on accuracy of model. It's is really important to ask questions about data needs like distribution of data to be pulled etc.


Took Deployment risk 

Overcommiting to a deadline to make deliverables.
I was working on an project to create data pipeline to get data from salesforce. I overcommited to a deadline of 2 week but the actual work took longer.
</br>


## Tell me about a time when you went Above and beyond your role?
<br>
I was working on new support portal project which uses IBM watson on customer description to route cases to appropriate team. Since we had few members on team, I was given additional responisiblity to manage the deployment process of ML models apart from data engineering work as we had no ML engineer on the team. The team was working with consultants from IBM Watson team.

Additonal work was to develop CI/CD pipeline to migrate ml model between environments. I have to add stages to test the ml model accuracy before deploying to production. If accuracy is not more than threshold, then rollback the deployment.

This was my first encounter to developed a CI/CD pipeline for a project from scratch. I learned everything on my own and took guidance IBM engineers. I learned how to create stages in pipeline, store the api keys and expose it in code, add dependencies between stages incase deployment failes how to rollback.

I created run books so that other engineers on team know what actions to perform incase of outages.

I got appreciation for single handedly managing the devops work on new project.
</br>



## What did you do when you needed to motivate a group of individuals or promote collaboration on a particular project?
<br>
We onboarded new data enigneers within my team. 
To bring them upto speed with current project work I created interdependent tasks.
This will 
Creating Inside vmware we have office of CTO and I was reading one whitepaper on differential programming language based on rust and how it's more efficient that Java. 
</br>


## Tell me about a time where you sought out perspectives other than your own to make a product/service/project better?
<br>
I was working on customer facing portal, and as data engineer I was asked to build complex data pipeline to pull data from salesforce and share with data scientists. After I shared the first phase of data for the model training, I asked the feedback about dataset shared. This is to confirm whether I correctly extracted data, in the feedback I got back the data scientist made few suggestions (to gather equally distributed data, and mostly independent features to avoid training erros). I changed my data pipeline accordingly and was able to deliver better dataset from next sprint.
</br>


## How have you leveraged data to develop a strategy?
<br>
explain skyline cohort analysis 

</br>

## Tell me about a goal that you set that took a long time to achieve or that you are still working towards. How do you keep focused on the goal given the other priorities you have?

<br>
I always wanted to sing and create music. In my college I was playing guitar but wasn't able to sing while playing. 
In 2016, I started rehearshing again and whatever way i was performing I used to record. 

In about 2 months, I was able to perform on stage with my own voice and music. 
I am still working towards polishing music side of mine. 
I do this in small incremental chunks, setting a small goal of playing a blue rythym or start of song rather than focusing on bigger part in one go.

</br>

## calculated risk and constraints bring resourcefulness
<br>
I am working on my current project from start.Our project is not heavily funded and we are short on budget. 
The tools we use are more open source and we try to optimize our ETL workloads so that we use less EMR resources.

And while choosing the ETL framework the senior architects in my team emphasised on using Glue ETL.

Although it's does have additional funnctionality with dynamic frame and all but it's was not cost effective for us to run our etl using glue etl.

I was critical to that decision and took the risk to create a working data-pipeline on EMR and demo it to the team.
I was able to demostrate that we can do all the work on doing everything on emr v/s glue etl and was able to onboard senior architects.

Also, We saved a lot of $$ using spot instances v/s on demand instances.
</br>

## Give me an example of a time you used customer feedback to drive improvement or innovation. What was the situation and what action did you take?
<br>
Business wanted to know what part of skyline advisor customer uses the most. The feedback from customer comes via click stream data.
I create data architecture to get one view of customer transaction across different vmware portal.
Let's say you had problem and you went to kb.vmware.com and them you submited a ticket on support.vmware.com

We track user ananymous id on browser to help improve kb documentation. 
monitor customer behavior using click stream data. generate analytics like most clicked kbs and write rules for them.

</br>



## Tell me about a time when you linked two or more problems together and identified an underlying issue? Were you able to find a solution?
```
We right rules and fire them on data collected via skyline to generate findings.

```
## What three things you are you working on to improve your overall effectiveness?
```
Especially in the pandemic focusing on eliminating interruptions, 
Plan and set clear architectural goals/success criteria.
Unlearn and Learn new , master one every quarter.
```


## Give me an example of when you took an unpopular stance in a meeting with peers and your leader and you were the outlier. What was it, why did you feel strongly about it, and what did you do?
```

```

## Tell me about a time you wouldn’t compromise on achieving a great outcome when others felt something was good enough. What was the situation?
```

```

## Tell me about a time you made a hard decision to sacrifice short term gain for a longer term goal.
```
Creating a working architecture is important than making optimized one in first go.
```

## How do you drive adoption for your vision/ideas? How do you know how well your idea or vision has been adopted by other teams or partners? Give a specific example highlighting one of your ideas.
```
rules should be written based on most files sr cases.
```

## Tell me about a time when you realized you needed to have a deeper level of subject matter expertise to do your job well?
```
dataset versioning issue with internal ml team.
```

## Tell me about a time when you had to analyze facts quickly, define key issues, and respond immediately to a situation. What was the outcome?
```
pendo collector version usecase
```

In answering the questions I would recommend using the STAR or SOAR method to tell a compelling and concise story that accurately answers the question(s) asked to you. In my own preparation for the onsite interviews I personally printed off the leadership principles and came up with 2-3 examples for each principle. When the questions were asked of me I had specific examples to share with them using the STAR or SOAR method of answering to explain each situation. Remember that using the same situation for each principle will not give us a well-rounded view of your experience.
 

DATE_SUB('2012-06-12', INTERVAL 29 DAY) last 30 days 


ML platform should be able to integrate with data, support data versioning, monitoring, governance across data pipeline.

collabration functions to enable sharing code, data, features, experiments with other team securely.

