# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- team member 1 Michael Wasson

Main source: https://aws.amazon.com/what-is/restful-api/ (linked in lab directions)

## Lab Question Answers

Answer for Question 1: Systems that implement REST APIs can scale efficiently because of optimized client server interactions. For example, server load is eliminated because there is no need to retain past client request information. Other client server interactions are reduced due to well managed caching. Since increasing clients has minimal effect, scalability is optimized. 

Question 2: The main resource that is given by the server in this instance is the json file that is needed to act as a data base for all the mail. When the client interacts with the server, it triggers operations within the server code that stores, retrieves, and manipulates data within the json file. The client has no direct interaction with this process.

Question 3: The server does not have a PUT method. The reason it does not have this is because the saving function is used internally by the server. To implement a PUT method, the save_mail function would need to be called by the client, and would save stuff to the json file.

Question 4: 
Main source used for this question.

https://cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:text=API%20keys%20provide%20project%20authorization,-To%20decide%20which&text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20the%20API.

API keys are good for identifying which application is making a call to an API and then determining whether that application has authorization to call the API. This is in contrast to authentication schemes that can check which specific user is calling an API and whether that user has authentication to do so.

API keys are best used in the following situations:
1) Suppose we want to block anonymous traffic. API keys will give information about an application's traffic.
2) They are useful if we want to limit the number of calls made to the API.
3) They can help identify usage patterns in API traffic.
