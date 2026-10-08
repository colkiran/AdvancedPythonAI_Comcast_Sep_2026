Key Stages of Machine learning workflow



1\. Problem definition

\---------------------



Data Scientist for the bank

\---------------------------

Customer Details

\-----------------

1\. Name

2\. Age

3\. Monthly / Annual Income

4\. Employment Type (employee, self employed)

5\. Credit score

6\. Requested Loan Amount

7\. Loan Duration

8\. Exiting Loans

9\. Number of dependents



b. What are the problems faced by the bank



&#x09;Problem01 - Large number of applications

&#x20;

&#x09;The bank needs a system that can automatically assist in evaluating 	applications



&#x09;Problem02 - Time Consuming



&#x09;A machine learning system could provide an initial prediction within 	seconds.



&#x09;Problem03 - Human Subjectivity



&#x09;The bank wants a data driven and consistent prediction process



&#x09;Problem04 - Identifying the Risk

&#x09;

&#x09;Historical loan data can be uses to learn patterns associated with 	previous approval decision.



b. The Actual Machine Learning Problem



Convert the Business problem into machine learning problem



Age	Income	    Credit\_Score    Loan\_amount	  Existing\_Loans    Emplyr



25	30000		620	    200000		2	      self



35	60000		720	    300000		1	     Salaried



45	90000		780	    400000    		0	     Salaried



29	40000		650	    250000		2	     Self   



New Applicant

&#x20;    |

Machine Learning Model

&#x20;    |

Accepted / Rejected



C. Define the Objective clearly



Develop a machine learning classification model that predicts whether a new loan application is likely to be approved or rejected based on historical applicant and loan information



What exactly are we trying to predict



Loan\_status -> 1 - Approved or 0 - Rejected



Features -> Machine Learning Algorithm -> Loan status



X -> Model -> Y



X - Applicant Features



Y - Loan Status



Why is this Supervised Learning

\-------------------------------



Applicant A - Approved

Applicant B - Rejected

Applicant C - Rejected

Applicant D - Approved



Historical Data  -> Known Answers -> Supervised Learning



And because the answer has only two categories



Approved

Rejected



it is specifically



Supervised Learning -< Classification -> Binary Classification



What would be the new prediction after the training



Name		- XYZ

Age		- 37

Income		- 75000

Employment 	- Salaried

Credit score	- 735

Loan Amount 	- 300000	

Loan Duration	- 10 years

Exiting Loans	- 1

Dependents	- 2





Applicant -> 



&#x09;1. Income	  |

&#x09;2. Credit Score   | -> ML Model -> Prediction -> 1. Approved

&#x09;3. Loan Amount    |				 2. Rejected



Approved Probability -> 82%

Rejected Probability -> 18%



VERY IMPORTANT (what the Model should NOT DO)

\---------------------------------------------



ML Model -> Prediction / Risk Score -> Bank's Business Rules -> Human / Automated decision process



Success Criteria

\----------------

Technical Metrics



a. Accuracy



&#x20;   accuracy = TP + TN / TP + TN + FP + FN



b. Precision

c. Recall

d. F1 Score

e. Confusion matrix



\------------------------------------------------------------------------



Problem Definition



A bank receives a large number of loan applications every day. Each application contains information about the applicant, such as age, income, credit score, employment type, requested loan amount, loan term, existing loans, and number of dependents.



Currently, loan applications are evaluated manually by loan officers. As the number of applications increases, this process becomes time-consuming and may result in inconsistent decisions.



The bank wants to use historical loan application data to build a machine-learning model that can predict whether a new loan application is likely to be approved or rejected.



The historical dataset contains applicant information along with the actual loan decision made for each application. These historical decisions act as labels from which the machine-learning model can learn patterns.



Machine Learning Objective



Build a supervised machine-learning classification model that predicts the loan status of a new applicant.



Target Variable



Loan\_Status



1 → Approved

0 → Rejected



Input Features

Age

Income

Credit Score

Loan Amount

Loan Term

Existing Loans

Employment

Dependents



Type of Machine Learning



* Supervised Learning
* Classification
* Binary Classification



Expected Output



For a new loan application, the model should produce a prediction such as:



Approved



or



Rejected



The model may also provide a probability score, such as:



Approved = 82%



Rejected = 18%



Success Criteria



The model should provide reliable predictions on previously unseen loan applications. Its performance will be evaluated using appropriate classification metrics such as accuracy, precision, recall, F1-score, and a confusion matrix.



The business objective is to help the bank make faster, more consistent, and data-driven loan assessment decisions while recognizing that the ML prediction is only one component of the overall lending decision process.







2\. Data Collection



Mock Data







3\. Data Processing and Cleaning



&#x09;1. null values



&#x09;2. check for duplicates





4\. EDA (Exploratory data analysis)



5\. Feature Engineering



6\. Model Training



7\. Model Evaluation and tuning



8\. Deployment



9\. Monitoring and Maintenance







