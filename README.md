\# QA Automation Assessment



This project demonstrates end-to-end automation skills using Python, Pytest, Selenium, and Postman.



Task 1: API Automation Using Requests



File: api\_tests/api\_automation.py

Fetches posts from JSONPlaceholder API, validates structure, and saves the first 5 posts locally.

Run: python api\_tests/api\_automation.py





Task 2: Pytest Test Suite



File: api\_tests/test\_api\_suite.py

Covers:

Status code \& response time

JSON schema validation

Parameterized endpoints testing

Run: pytest -v api\_tests/test\_api\_suite.py





Task 3: Postman Automation



Folder: postman/

Import API\_Automation\_Collection.json into Postman.

Covers:

GET /posts – validate status 200

POST /posts – validate created post matches

DELETE /posts/{id} – validate deletion





Task 4: Selenium with Pytest Automation



File: selenium\_tests/test\_selenium\_practice.py

Covers UI validations on:

https://rahulshettyacademy.com/AutomationPractice/

Run: pytest -v selenium\_tests/test\_selenium\_practice.py





Task 5: Strategy \& Leadership



File: docs/Strategy\_and\_Leadership.md

Contains written answers on handling flaky tests, process improvements, and QA strategy.

