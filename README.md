
# Lenme Task    

- ## Use case
One of Lenme’s borrowers submitted a loan request for $5,000 to pay them back in 6 months. They received an offer from one of the investors on the platform with a 15% Annual Interest Rate. A $3.00 Lenme fee will be added to the total loan amount to be paid by the investor.

- ## Requirements:
    - You are required to develop a Django REST project to be able to build the following flow-through its APIs;
    - The borrower submits a loan request for $5,000 `loan amount` and 6 months `loan period`
    - The investor will submit an offer to the borrower with 15% `Annual Interest Rate`
    - The borrower will accept the offer
    - Check if the investor has sufficient balance in their account to fund the `Total Loan Amount` (Loan Amount + Lenme Fee)
    - The loan will be funded successfully and the loan status will be `Funded`
    - Six monthly payments will be scheduled from the day the loan was funded successfully (Note: Developing an external scheduler is not required)
    - Once all the payments are successfully paid back to the investor, the loan status will be changed to `Completed`

## Installation

First you have to clone the project the navigate to lenme folder and run the following commands:
```bash
  pipenv install
  pipenv shell
  pip install -r requirments.txt
```

The you have to open Three terminals and make sure that pipenv is activated
```bash
pipenv shell
```

First terminal we will run DRF server as follows:
```bash
python manage.py runserver
```
Second terminal we will start Celery worker to start our Tasks Queue using the following command:
```bash
celery -A lenme worker -l debug
```
Third terminal we will start celery beat to get the scheduled periodic tasks as follows:
```bash
celery -A lenme beat -l debug
```


## Tech Stack
- Django Rest Framework to build main API's.
- Celery Task Queue and Scheduler.
- SQLlite3 as main Database.
- Redis key value pair memory cache for celery workers.
- Postman for API Documentation
## Database Diagram
![Database ER diagram (Lenme)](https://user-images.githubusercontent.com/23037901/209165258-c3c37d05-1cd6-4489-867b-b3c001a652a5.png)

## API Reference

#### Register Borrower

```http
  POST /accounts/api/register/borrower
```

Body 
```json
{
    "username": "joeshindy",
    "email": "shindi.joe@gmail.com",
    "password": "Password@123"
}
```

#### Login Borrower

```http
  Post /accounts/api/auth/borrower/login/
```

Body 
```json
{
    "username": "joeshindy",
    "email": "shindi.joe@gmail.com",
    "password": "Password@123"
}
```

#### Register Investor

```json
  POST /accounts/api/register/investor
```

Body 
```json
{
    "username": "joeshindy",
    "email": "shindi.joe@gmail.com",
    "password": "Password@123"
}
```

#### Login Investor

```http
  Post /accounts/api/auth/investor/login/
```

Body 
```json
{
    "username": "joeshindy",
    "email": "shindi.joe@gmail.com",
    "password": "Password@123"
}
```

#### Create Loan Request

```http
  Post /loan/api/create
```

Body 
```json
{
    "borrower": 13,
    "amount": 5000,
    "period": 6
}
```
#### Create Loan Offer Request

```http
  Post /loan/api/offer
```

Body 
```json
{
    "loan": 11,
    "investor": 14,
    "annual_interest": 15
}

```
#### Accept Loan Offer Request

```http
  Post /loan/api/offer/accept
```

Body 
```json
{
    "offer": 9,
    "loan": 11
}
```
#### Reject Loan Offer Request

```http
  Post /loan/api/offer/reject
```

Body 
```json
{
    "offer": 9,
    "loan": 11
}
```
#### Settle Loan Payment

```http
  Post /loan/api/payment/settle
```

Body 
```json
{
    "payment": 2
}
```

#### Get Loans

```http
  GET /loan/api/list

  Gets loan requests based on user token sent in authorization request
```

#### Get Loan Offers

```http
  GET /loan/api/list/<int:loan_id>/offers
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `loan_id`      | `integer` | **Required**. Id of loan to its offers |

#### Get Loan Payments

```http
  GET /loan/api/list/<int:loan_id>/payments
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `loan_id`      | `integer` | **Required**. Id of loan to its payments |



You can find detailed documentation through this link:

[API Documentation](https://documenter.getpostman.com/view/12485266/2s8Z6u5FMq)

