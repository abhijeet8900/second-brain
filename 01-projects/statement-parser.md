# Project Title: statement-parser

## Overview

We want to write script to extract financial details from documents such as account statement, credit card bill. Documents can be in different format.

**Goals:**

- Extract key information from  documents ( account statement), such as transactions, account details, opening / closing balance.
- Information extracted from documents should be returnable in different format. (csv, xls, dataframe ), which will help in further processing and analyzing.

## Action Items

**Tasks:**

- [ ] Extract information from documents in data frame.
- [ ] Standardize extracted information
- [ ] Consolidate information from multiple source. eg Account statements from multiple accounts.

## Extracting information from PDF documents

Considering we are only aiming at bank statements at this point, extracting information from PDF is hard, specially tables. To solve this we will convert PDF documents into images and then we will use OCR library to extract information from these images.

`Convert PDF into images -> Optimize image for OCR -> Extract information using OCR`

## Extracting Account Statements

We can to extract transaction and account information form account statement. We want to create data frame with all details of transaction and account details. This information needs to be standardized in common format ( column name, currency, sorting )

- We can extract account related information as well as transactions from bank statements.
- Account statements are generally divided into multiple pages, we will need to extract information from all pages and combine it in sensible manner
- Every bank has its own format for statement document. This causes problem where one solution is not working for every file.
	> We can handle it by having generic class for extracting information and extending this class for each bank document type ( account statement, credit card statement ).
- Column names for transaction table are different for each bank.
	> This will be handled since we will be having separate class for each bank.
- For each of bank statement page we need to remove total row, which indicates total of column for that page.
- Major issue with OCR is its ability to extract information. Its not 100% accurate, for each bank statement we need to tweak image optimization as well as extraction logic to get higher accuracy, goal is to get all major information.
	> We can search for information that we can extract consistently which we can use to verify our data frame. Eg Account opening and closing balance, date.
- Account statement document has extra information about sub accounts connected to primary account eg PPF account, RD account. We need to check if details for these accounts are important or not.

## Dataframe Standardization

We want to standardize data frame data ensuring that we get same structure of data frame regardless differences in documents

### What we want in each data frame 

> `Dataframe` here indicates panda's data frame which includes transactions for givens statement.

We want to ensure that for different banks we application outputs following information consistently

- Statement Information
	- Account number
	- Bank name
	- Opening Balance
	- Closing Balance
	- Date range of account statement
- Transaction information
	- Date of transaction
	- Description of transaction
	- Amount of transaction
	- Balance after transaction ( just be cause its available there )

## Notes

**Additional Information:**  
Any extra observations or thoughts related to the project.

- Note 1: Briefly explain or elaborate.
- Note 2: Briefly explain or elaborate.

## References

**Resources and Links:**  
Include any relevant resources, articles, or references.

- [Reference 1](URL): Short description of what the reference is about.
- [Reference 2](URL): Short description of what the reference is about.

---

**Created on:** 2024-08-01  
**Last Modified on:** 2024-08-01
