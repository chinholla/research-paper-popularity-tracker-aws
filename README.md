
# Research Paper Popularity Tracker
#### Project Overview

The **Research Paper Popularity Tracker** is an innovative project designed to track the popularity of research papers in real time. By utilizing **Python** for web scraping, the system extracts essential details like the title of the **paper**, **author name(s)**, and **abstract** from various research sources. These details are dynamically retrieved through an **HTTP API** powered by **AWS API Gateway**, which triggers AWS Lambda functions to handle the backend logic. The use of **BeautifulSoup** for scraping ensures scalability, allowing the system to gather data from multiple sources. The project's frontend is built using **Streamlit**, providing users with an intuitive interface to visualize the research paper's popularity trends and track metrics such as citation count, views, and downloads. With this serverless architecture, the tracker efficiently handles real-time requests and offers a smooth, scalable solution for research monitoring.

# Technology Stack
 
**Backend:** Python, AWS Lambda

**Frontend:** Streamlit

**Cloud Services:** AWS Lambda, API Gateway

**API Integration:** arXiv



# Architecture


-   API Gateway handles HTTP requests and routes them to AWS Lambda functions.

- AWS Lambda executes Python code that fetches and processes popularity data.
- External APIs (arXiv) provide real-time paper data.
- Streamlit provides the frontend for visualizing research paper popularity.

# Features

- **Real-Time Popularity Tracking:** Monitors research paper statistics such as citations, views, or downloads.
- **Serverless Architecture:** Utilizes AWS Lambda and API Gateway for efficient, scalable backend services.
- **Streamlit Dashboard:** Provides a visually appealing and interactive interface for tracking paper trends.
- **API Integration:** Fetches data from external APIs like arXiv, etc.
- **Scalable and Efficient:** Automatically scales to handle traffic.


# Installation

### Setup Instructions

 #### 1. Clone the repository
    git clone git clone https://github.com/chinholla/research-paper-popularity-tracker-aws.git

 #### 2. Get your API keys:
Sign up on arXiv and retrieve your API keys.

 #### 3.  Deploy the Python code to AWS Lambda:
 Package your Python code and deploy it using the AWS CLI or the AWS Console.

 #### 4. Set up AWS API Gateway:
- Create an API Gateway to expose the Lambda functions as HTTP endpoints.
- Integrate the API Gateway with Lambda functions and test the endpoints.

#### 5. Run Streamlit for the Frontend:
    streamlit run app.py

    

# Usage

#### Track Research Papers: 
- Enter a research paper's title or ID in the Streamlit dashboard to track its popularity.
- View real-time statistics, including citations, views, downloads, and trends.

#### Interface:
- The Streamlit dashboard displays popularity metrics, allowing users to visualize trends, filter papers, and set alerts.

#### Search Functionality:
- Users can search for specific papers and track their popularity metrics through the API Gateway.


# Screenshots

### Lambda Function:

#### Lambda Function - Backend Logic
The **AWS Lambda function** acts as the core backend for the Research Paper Popularity Tracker. It processes the scraping requests and handles the data. In this function, we implemented the logic to scrape research paper data using Python.

![1](https://github.com/user-attachments/assets/f93ed90e-abb2-4295-980f-ca8712ad40d2)




#### Web Scraping with BeautifulSoup
BeautifulSoup is used for scraping relevant details from the research paper's webpage. This includes extracting information such as:
- **Title of the paper**
- **Author name(s)**
- **Abstract**

These details are gathered from the website URL provided in the request, making the backend function dynamic and scalable for multiple research sources.

![2](https://github.com/user-attachments/assets/48479dbc-09ec-4ce7-8905-b77b933855a3)


#### API Gateway - HTTP API
- The app interacts with AWS Lambda via an HTTP API, which is created using AWS API Gateway. This API allows the frontend (or any external service) to request data from the Lambda function.
- The API is designed as a GET method, which is ideal for retrieving data from the web. It ensures that the scraped information is passed back efficiently without modifying the server-side data.
- The **Lambda handler** is the main entry point for a lambda function. It's the funstcion that is triggered by an event, such as **API Gateway request**. It is responsible for processing incoming requests and returning requests.

![3](https://github.com/user-attachments/assets/2dfd4129-f30c-4fe6-9633-0fe596472afb)


#### Overall Backend Workflow:
**The backend processes are neatly tied together:** the API Gateway handles HTTP requests, AWS Lambda triggers the scraping function written in Python, and the scraped data is then processed and returned. **The GET API method** ensures that only data retrieval operations occur, maintaining simplicity and speed.

![getmethod](https://github.com/user-attachments/assets/288c4450-adfe-447a-91d3-99ecc46cc296)

#### Code Overview - app.py
- The screenshot of app.py from VS Code shows the implementation of the web scraping logic, API integration, and data handling. This code ties the Lambda function and API Gateway together, ensuring smooth communication between the frontend and backend.
- The script's main task is to handle incoming HTTP requests, trigger the scraping function, and return the research paper details to the requesting client.

![Screenshot 2024-09-22 203533](https://github.com/user-attachments/assets/08dfad51-1dfa-44b7-82b5-ca2cfa3004e2)











# Authors

- [Chinholla](https://github.com/chinholla)
- [Chaithu2653](https://github.com/Chaithu2653)



