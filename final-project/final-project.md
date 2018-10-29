![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Final Project: Comprehensive Data Analytics Project

## Overview

The goal of this project is to give you an opportunity to demonstrate the skills you have built throughout this program. In this project, you will use Python, SQL, and Tableau to put together a complete analytics workflow, including:

* Data acquisition
* Data wrangling
* Data storage
* Data exploration and analysis
* Feature selection
* Machine learning model training
* Model evaluation
* Reporting and presentation of insights

You will be provided a list of data sets to choose from for this project. Using the knowledge you have acquired and your experience working with data, you will need to come up with a plan for what you are going to do and then design the project around the data set you have chosen.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. You will be working on this project over the course of 3-4 days (actual length of the project to be decided by your Lead Instructor). Below is the anticipated activities you should be performing on each day.

### Day 1

* Idea generation & planning
* Data gathering & cleaning
* Data storage

### Day 2

* Exploratory data analysis
* Data visualization

### Day 3

* Feature selection
* Model selection & comparison
* Model evaluation
* Prepare for presentation

### Day 4 (optional)

* Iterations on your modeling
* Model evaluation
* Prepare for presentation

If you finish the tasks for a day early, you can either perform the tasks for that day deeper (ex. deeper cleaning, exploration, modeling, etc.) or move on to the tasks for the next day.

---

## Project Instructions

### Day 1

On the first day of your project, you will be planning your project, choosing a data set, downloading and cleaning it, and storing it in a MySQL database.

To get started, evaluate and choose from one of the following data sets:

* [Telecom Customer Churn Data Set](https://www.kaggle.com/blastchar/telco-customer-churn)
* [Mental Health in Tech Survey Data Set](https://www.kaggle.com/osmi/mental-health-in-tech-survey)
* [Flight Delays and Cancellations Data Set](https://www.kaggle.com/usdot/flight-delays)
* [Craft Beers Data Set](https://www.kaggle.com/nickhould/craft-cans)
* [Human Resources Data Set](https://www.kaggle.com/rhuebner/human-resources-data-set)

These are all Kaggle data sets, so you can gain some context about them by looking at the field descriptions and the *Overview* tab for each data set. You can also get project ideas by looking at the different *Kernels* that people have created using the data sets and the approaches they have taken, but please **do not plagiarize or copy someone else's work.** Remember that the goal of this project is to demonstrate *your* skills, not someone else's.

#### Project Ideas

As you are evaluating the data sets and deciding which you would like to use for your project, think about the different types of information that could be extracted from each one and what problems you could potentially solve by applying supervised or unsupervised machine learning to the data. Below are some ideas for each data set to help get you started.

##### Telecom Customer Churn

This data set is great for practicing supervised machine learning. The most obvious supervised learning problem to model with this data set is attempting to predict churn (whether or not a customer is going to leave). Another supervised problem you can try to solve is predicting tenure, or how long a customer will end up staying with the company. There are also a lot of ways to slice, dice, and analyze this data set - for example, looking at how monthly charges increase or decrease depending on different types of contract, tenure, and services provided.

##### Mental Health in Tech

This data set is also good for supervised learning, where you would attempt to predict the whether the employee taking the survey has received treatment for mental health (treatment variable). You can also analyze how the other variables in the data set contribute to whether someone seeks treatment for mental health and explore what types of environments result in employees with the best mental heath states.

##### Flight Delays and Cancellations

This relational data set can help you practice your SQL joins as well as supervised learning as you attempt to predict which flights will be delayed and by how much time. There are also a variety of ways to explore this data set to determine which airlines are most efficient, what times of day there tends to be the most delays, which cities have more frequent delays than others, and how all this changes over time.

##### Craft Beers

This relational data set has fewer variables than the others, and that means that choosing it for your project will require you to apply some extra creativity. For example, you can create categorical variables out of the numeric abv and ibu variables to categorize a beer's strength and hopiness. You can also use  string operations on the style field to extract additional keyword-based categories (e.g. IPAs, American, English, Wheat, etc.). For modeling, you can attempt to predict the style of the beer or the probability that it falls into a particular style. Alternatively, you can attempt to compute similarity between beers to determine which ones are most like which other ones.

##### Human Resources

This is another relational data set where you can practice your SQL joins as well as data wrangling, analysis, and machine learning. As far as applying machine learning to this data set, you can attempt to cluster employees together into similar groups, you can attempt to predict performance scores or pay rate, or you can attempt to predict whether an employee will be terminated within a certain amount of time. Additionally, you can also analyze the relationship between pay and performance by position, department, and manager as well as employee demographics.

Once you have chosen a data set, you will need to download it. In order to do so, you will need to create a free Kaggle account if you don't already have one. Once you have downloaded the data, you should perform the steps below:

* Create a new MySQL database where your data will eventually be stored.
* Create a new Jupyter Notebook for your project.
* In the Jupyter Notebook, read the data files using Python.
* Perform any necessary data wrangling and cleaning using Python.
* Create a connection to your MySQL database using `pymysql` and `sqlalchemy` and write the clean version of the data to the database.

### Day 2

On the second day of your project, you will start with the clean data set you stored in your database on the previous day. You will explore, analyze, and visualize the data using Python and Tableau, applying the variety of techniques you learned throughout the program.

* In your Jupyter Notebook, read the clean data from your MySQL database.
* Using Pandas, generate summaries of the data and calculate descriptive statistics.
* Practice generating a few basic charts and graphs using `matplotlib` or `seaborn` as well.
* Export your clean data set to a CSV file.
* Open Tableau Public and load the CSV file.
* Explore the data in Tableau and look for interesting insights.
* Put together an annotated Tableau Story communicating the insights you have discovered.

### Day 3

On the third day of your project, you will be using the analysis you performed and the insights you discovered the previous day to help frame your machine learning problem, select and engineer appropriate features, train your models, and evaluate performance.

* If you are planning on doing supervised machine learning, identify the target variable you would like to train a model to predict. Also determine whether you will be doing regression (target variable is continuous) or classification (target variable is discrete).
* Perform feature selection/engineering to arrive at the features you feel best represent the problem you are trying to solve. During this stage, you may need to normalize or scale your variables.
* Train a couple machine learning models on the data.
* Evaluate the performance of the models.
* Prepare a presentation of your findings and results.

### Day 4

Should you have a fourth day of final project work, you should spend the day refining your machine learning models and your presentation. If you have time, you may also go back and perform additional data exploration and analysis.

* Continue iterating on your machine learning models with the objective of optimizing their performance.
* Organize your machine learning steps into a pipeline that performs feature selection/engineering, model training, model evaluation, and model storage.
* Further refine your presentation based on additional findings and results.

## Technical Requirements

The technical requirements for this project are as follows:

* You must demonstrate proficiency with every step of the analytics workflow.
* Python should be used to import/export, clean, wrangle, analyze, and perform machine learning on the data.
* MySQL should be used to store a clean version of your data set.
* Tableau should be used for data exploration, analysis, visualization, and storytelling.
* Your Python code should be stored in a Jupyter Notebook (.ipynb) file.
* You should also include a README.md file that describes the steps you took and your thought process throughout each stage of your project - from choosing your data set all the way through evaluating your machine learning models.

## Necessary Deliverables

The following deliverables should be pushed to your Github repo.

* A Jupyter Notebook (.ipynb) file containing all your Python code.
* A data folder containing your original data set and your clean data set in CSV format.
* A README.md file that provides a detailed description of what you did, how, and why.

## Useful Resources

Just about everything you need to complete this final project should have been covered in the lessons of this program. If you need to research any errors you are getting or how to do something extra, we have tried to reinforce that the places to look for answers are the Python/MySQL/Tableau documentation and StackOverflow (or other technical question-and-answer sites). This is how people who work with data in the real world find answers and overcome the obstacles they encounter on a daily basis, so it is important to get some practice at it.

## Project Feedback + Evaluation

* __Technical Requirements__: Did you deliver a project that met all the technical requirements? Given what the program has covered, did you build something that was reasonably complex?

* __Creativity__: Did you add a personal spin or creative element into your project submission? Did you incorporate domain knowledge or unique perspective into your analysis.

* __Code Quality__: Did you follow code style guidance and best practices covered in class?

* __Total__: Your instructors will give you a total score on your project between:

    **Score**|**Expectations**
    -----|-----
    0|Does not meet expectations
    1|Meets expectactions, good job!
    2|Exceeds expectations, you wonderful creature, you!

This will be useful as an overall gauge of whether you met the project goals, but __the more important scores are described in the specs above__, which can help you identify where to focus your efforts on future projects in the real world!

## Presentation Guideline and Criteria

### Format

* Presentation Time: 12 minutes
* Q & A: 3 minutes
* **Total Time:** 15 minutes

### Attire

* DRESS TO IMPRESS: [Smart casual](https://en.wikipedia.org/wiki/Smart_casual) would be great

### Outputs

* A presentation in [slides.com](https://slides.com/)
* A demo deployed on GitHub Pages
* The presentation and demo will be executed on a class computer (instead of your own)
* Get ready to explain some of your code in GitHub

### Things you might want to talk about

* Short presentation of yourself:
	* Who are you?
	* A hobby you have.
  * __Note: we are getting you ready for final presentation!__
* Elevator pitch:
  * Data set you chose.
  * Why did you chose that data set?
  * The most important thing you learned.
* One technical challenge you faced:
  * Explain the challenge.
  * Explain how and what you did to overcome it.
  * Show and explain code snippets in your presentation slides.
* Git:
  * Display a screenshot of your GitHub graphs to show your commit frequency and how much work you did.
* Final Project Walkthrough:
  * Walk the audience through the data set you chose, providing an overview of some of the fields and other information contained in the data.
  * Walk the audience through your process of cleaning, exploring, analyzing, and performing machine learning on your data including what tools and techniques you employed, what avenues you decided to pursue and why, what interesting insights you discovered, and what lessons you learned.

Below are a few videos of the Ironhack Hackshow where our graudates presented their final projects. Take a quick look on how our past students presented their projects.

* [Web Dev final project demo](https://www.youtube.com/watch?v=MnUxEL3iiig)
* [UX/UI final project demo](https://www.youtube.com/watch?v=oII8I2nl7WM) 
* [Hackshow diciembre 2017 - Madrid](https://www.youtube.com/watch?v=64Jav707V9E) (Spanish)

## 5 Tips for Successful Completion

* Generate a project idea that solves a data problem with practical values. Make sure the problem you try to solve is clearly defined. Make sure the scope of the problem is manageable so that you can complete within the project timeframe. Meanwhile, think beyond the problem itself - can your solution of the problem inform how to solve other bigger/deeper problems?

* Obtain timely feedback on your ideas, plans, progress, and products from the instructional staff. This ensures you stay on the right track and deliver impressive results.

* Be prepared for technical difficulties. Manage your time wisely and pace yourself. Stick to the project agenda strictly.

* Commit your codes and push to Github on regular basis. You should commit every time you complete a task and push at least once a day. This will help you avoid accidential data loss and is also the easiest way to document your iterative development process.

* Before final project presentation, test every component and step of your demo. Make sure your demo will run smoothly.

## May the force be with you!
