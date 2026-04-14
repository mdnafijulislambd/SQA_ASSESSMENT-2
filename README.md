# 🧪 SQA Assessment 2 – Automation Test Suite

This repository contains automated test scripts for the **QAHarbor Jobs Portal** (`https://labsqajobs.qaharbor.com/`).  
The tests are written in **Python** using **Playwright** and **pytest**.

---

## 📁 Project Structure
SQA_ASSESMENT-2/
├── conftest.py
└── test/
    └── log_qa.py


- **`conftest.py`** – Contains the `page` fixture that launches and closes the browser for each test.
- **`test/log_qa.py`** – Contains all the test cases (`test_case_1`, `test_case_2`, etc.).

---

# SQA Automation Setup & Run Guide

## 1. Install Python

Download Python from:  
https://www.python.org/downloads/

During installation:  
**Add Python to PATH**

Verify installation:
```bash
python --version

## 2. Open Project Folder
cd SQA_ASSESMENT-2

## 3. Install Playwright
pip install playwright

## 4. Install Browser Drivers
playwright install

## 5. Install Pytest and Playwright Plugin
pip install pytest pytest-playwright
python -m pytest --version

## 7. Run Tests
python -m pytest test/log_qa.py -v
