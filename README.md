Python Expense Tracker with MySQL Integration

A Expense Management System developed using Python,designed to help users seamlessly record,track,and analyze their financial activities in real-time.

Developer: Saravana Perumal T
Tech Stack: Python, MySQL (XAMPP), Pandas, Matplotlib
Core Skills Showcased: CRUD operations, Data Visualization, Input Validation, Database Handling

Project Overview:

This application enables expense tracking with simple forms and powerful data analytics.You can store your spending history inside a MySQL database and generate visual reports with just a click.

Perfect for demonstrating strong foundation knowledge as a fresher developer.

Key Features:
Feature:         	Description:
1)Add Expense-          Insert expense details like date, category, and amount
2)View All Expenses-	Retrieve database records in neat tabular format
3)Update Expense-	Modify existing records using expense ID
4)Delete Expense-	Remove unwanted entries safely
5)Search Filters-	Search by date, category, or date range
6)Analytics-	        Category-wise and monthly spending insights
7)Charts-       	Bar chart & trend chart using Matplotlib
8)Export to Excel-	Generates business-friendly report files
9)Input Validation- 	Prevents incorrect data entries
10)Smooth Exit- 	Ensures DB connection closure and data safety


Database Schema:

Database Name: expense_db
Table Name: expenses

Column Name:	Type:
expense_id	INT (Primary Key, Auto Increment)
date	        DATE
category	VARCHAR(255)
amount	        DECIMAL(10,2)

How to Run the Project

1)Install XAMPP and start MySQL service

2)Create the database using MySQL:

   CREATE DATABASE expense_db;
   USE expense_db;
   CREATE TABLE expenses (
   expense_id INT AUTO_INCREMENT PRIMARY KEY,
   date DATE,
   category VARCHAR(255),
   amount DECIMAL(10,2) );

3)Install the Python libraries:
 
   pip install mysql-connector-python pandas matplotlib

4)python expense_tracker.py:

5)Project Folder Structure:
  
   Expense-Tracker:
   expense_tracker.py
   generated_reports (Excel files saved here)
   README.md


