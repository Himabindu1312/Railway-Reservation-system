# Railway-Reservation-system

## Scenario:
You are hired by a Railway Company, you are asked to design a system which provides 
information to passengers about the trains available on the bases of source and destination, other 
information like status of the train, status of passenger ticket, how many seats are available etc.
Suppose you are given the following requirements for a simple database for the Railway 

## Reservation System:
This system helps to maintain the records of different trains, the train’s status, and passengers.
The database consists of 4 tables: 
• Train: Train Number, Train Name, Premium Fair, General Fair, Source Station, 
Destination Station
• Train_Status: TrainDate, TrainName, PremiumSeatsAvailable, GenSeatsAvailable, 
PremiumSeatsOccupied, GenSeatsOccupied
• Passenger: first_name, last_name, address, city, county, phone, SSN, bdate
• Booked: Passanger_ssn, Train_Number, Ticket_Type, Status


Note: As the system is very large and is not feasible to develop therefore there are some 
assumptions that need to be considered, for example:
• Only two categories of tickets are available: Premium and General Ticket
• The total number of tickets can be booked in each category (Premium and General) is 10
• Number of tickets in waiting list is 2
• Total Number of trains are 5
• Any stops made by a train before its destination and their bookings are not considered.

##Create a GUI for the RRS database SQL Queries:
##Railway Reservation Application: 
Create a simple and friendly GUI interface that would be able to perform the following tasks. 
You may use JAVA programming using JDBC, or C/C++/C# programming with ODBC/Oracle 
or Python programming or PHP/MySQL or other programming languages to develop a GUI 
interface. The user will have to type or select the query’s input parameters and post the question 
to your program. The program needs to return all result’s rows. 

## Query/GUI TASK:
1. User input the passenger’s last name and first name and retrieve all trains they are booked on.
2. User input the Date and list of passengers travelling on entered day with confirmed tickets 
displays on UI.
3. User input the age of the passenger (50 to 60) and UI display the train information (Train 
Number, Train Name, Source and Destination) and passenger information (Name, Address, 
Category, ticket status) of passengers who are between the ages of 50 to 60. 
4. List all the train name along with count of passengers it is carrying.
5. Enter a train name and retrieve all the passengers with confirmed status travelling in that 
train. 
6. User Cancel a ticket (delete a record) and show that passenger in waiting list get ticket 
confirmed.
