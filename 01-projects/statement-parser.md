# Project Title: statement-parser

## Overview

We want to write script to extract financial details from documents such as account statement, credit card bill. Documents can be in different format.

**Goals:**

- Extract key information from  documents ( account statement), such as transactions, account details, opening / closing balance.
- Information extracted from documents should be returnable in different format. (csv, xls, dataframe ), which will help in further processing and analyzing.

## Project Folder Structure

> Not final structure just for reference

```plaintext
FinExtract/
├── .gitignore
├── .env
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── docs/
│   └── ...
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── utils.py
│   └── parsers/
│   	├── __init__.py
│       ├── abstract_class.py
│       ├── bank1.py
|		├── bank2.py
|		└── ...
│   └── extractors/
│   	├── __init__.py
│       ├── abstract_class.py
│       ├── bank1.py
|		├── bank2.py
|		└── ...
│   └── image_optimizers/
│       ├── __init__.py
│       ├── abstract_class.py
│       ├── bank1.py
|		└── bank2.py
|	└── normalizers/
│       ├── __init__.py
│       ├── abstract_class.py
│       ├── bank1.py
|		└── bank2.py
|		└── ...
└── scripts/
    ├── setup.py
    └── script2.py
```

## Feature Tasks

- [x] Initialize git repo for project
- [x] Create new project using python poetry for better dependency management
- [x] Create MakeFile for project, to create custom commands
- [x] Create abstract abstract class for extractor
- [x] Create class for image optimizer
- [x] Function to extract account statement information
- [x] Function to extract transaction information
- [ ] Extrating opening balance from icici statement 
- [ ] function to validate all rows in transaction data frame
- [ ] Function to clean final transaction tables for any impurities, eg duplicate rows, missing information

## Refactors Tasks

- [ ] Update extract table function to extract tables by passed headers, it should combine header tables as well
- [ ] Standardize module imports for python
- [ ] Code refactoring for each module
- [ ] Add better log to know progress in terminal

## Issues

- [ ] Not recognizing table from last page with single row ( ICICI Statement )
- Need to consider statement might have multiple account related transactions
        -- Should not worry about is as current goal is to extract only bank account transactions
        - [x] Write function to detect table with account transactions only, title matching works for ICICI statement since it contains partial account no as well as account type ("Savings Account")

- [ ] Need to test each statement with following type of account statements
        - multiple 1 month statement of each bank : Union, IDBI, ICICI, SBI, Need to verify using xls statements
        - multiple 3 month statement of each bank : Union, IDBI, ICICI, SBI, Need to verify using xls statements

- [x] Need to write validator to remove and incorrectly captured transaction, currently statement may capture some transactions twice
    -- we confirm it by check if date, withdrawal, deposit is equal and if balance for both is same then its potential duplication row

- [ ] Final transaction table has some rows values in both deposit and withdrawal column, this is due to its reading adjacent rows as single row. Possible solution here is better image optimization

## Extracting information from PDF documents

Considering we are only aiming at bank statements at this point, extracting information from PDF is hard, specially tables. To solve this we will convert PDF documents into images and then we will use OCR library to extract information from these images. Each bank will have its information in different layout in PDF we will  need to write function for each bank's extractor. In order to increase accuracy we will store all account information in env variables which we can use to verify extracted info.

### ICICI Extractor

ICICI bank statement has its statement related information on first page. We can extract it as table, this information contains partial account no ( last few digits ), It also contains account type and closing balance.

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

- For handling missing rows from statement or any impurities in statement, one of the solution is to have multiple image conversions and use those images to extract multiple data frames for single pdf, then we validate rows coming from each of this data frame to increase chances of correct rows.
- Validating rows will be easy since combination of date, withdrawal and balance will form unique hash for each row. Eg each unique row will have some different combination of all fields which are non duplicate for that statement.


## References

**Resources and Links:**  
Include any relevant resources, articles, or references.

- [Reference 1](URL): Short description of what the reference is about.
- [Reference 2](URL): Short description of what the reference is about.

---

**Created on:** 2024-08-01  
**Last Modified on:** 2024-08-01
