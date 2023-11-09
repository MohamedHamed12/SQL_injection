#  SQL Injection Attacks

## Overview

SQL injection is a serious threat to the security of your website, as it allows attackers to exploit vulnerabilities in your database queries. This README provides guidance on preventing SQL injection attacks and securing your website's database.
site for SQL injection vulnerabilities using tools like SQLmap or by manually inspecting input fields for unusual behavior.


When login with correct data it success if wrong it failed 

![image](https://github.com/MohamedHamed12/SQL_injection/assets/90472426/c313be73-6d68-4af8-9ac3-b219756ee83f)

When write  `' OR '1'='1' --`  in username failed without password it success

![image](https://github.com/MohamedHamed12/SQL_injection/assets/90472426/7e0818c7-65da-47ef-acfa-a9bca344dcb3)



This search box provided to usres so they can search and found result 

![image](https://github.com/MohamedHamed12/SQL_injection/assets/90472426/cef8457e-4fbe-47d1-a92c-893cdcd8c4f9)

`'  union select * from users --`
He can get all usernames and passwords 

![image](https://github.com/MohamedHamed12/SQL_injection/assets/90472426/0d7df40e-8788-405e-b4a1-43209eb0c77d)


But haker can use it to get important and sucre information from database 

![image](https://github.com/MohamedHamed12/SQL_injection/assets/90472426/3a894a92-ec45-4615-acd8-32645456320a)
