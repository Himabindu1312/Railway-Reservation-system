from tkinter import *
import sqlite3
conn = sqlite3.connect('PA3.db')
add_table_c = conn.cursor()

root = Tk()
root.title('Railway Reservation System')





def passenger_booked():
	passenger_booked_conn = sqlite3.connect('PA3.db')
	passenger_booked_cur = passenger_booked_conn.cursor()
	passenger_booked_cur.execute(" SELECT Train.'Train Name', Train.'Train Number', booked.Ticket_Type, Booked.Status from train join booked on Train.'Train Number' = Booked.Train_Number join passenger on passenger.SSN = Booked.Passanger_ssn where Passenger.last_name = ?  and passenger.first_name = ? ;",(last_name.get(),first_name.get(),))
	records = passenger_booked_cur.fetchall()
	print_records = " "
	for record in records:
		print_records += str("Train Name: "+record[0]+ "   " +"Train Number: "+ str(record[1]) + "   " +"Ticket Type: "+ record[2] + "   " +"Status: " + record[3]+ "\n")

	passenger_booked_conn_label = Label(root, text = print_records)
	passenger_booked_conn_label.grid(row = 7, column = 0, columnspan = 2)
	passenger_booked_conn.commit()
	passenger_booked_conn.close()

passenger_booked_button = Button(root, text = 'Passenger Booking Details', command = passenger_booked)
passenger_booked_button.grid(row = 5, column = 0, pady = 10, padx = 10)
	

def ViewConfirmedPassengers():
	ViewConfirmedPassengers_conn = sqlite3.connect('PA3.db')
	ViewConfirmedPassengers_cur = ViewConfirmedPassengers_conn.cursor()
	ViewConfirmedPassengers_cur.execute("SELECT distinct passenger.first_name, passenger.last_name, Booked.Ticket_Type, Booked.Status FROM Passenger, Booked,Train,Train_status Where passenger.SSN = Booked.Passanger_ssn and Booked.Train_Number = Train.'Train Number' And Booked.Status = 'Booked' AND Train_status.TrainDate = ? ;", (TrainDate.get(),))
	records = ViewConfirmedPassengers_cur.fetchall()
	print_records = '\n'.join([f"First Name:  {record[0]},    Last Name: {record[1]},     Ticket Type:  {record[2]}    Status:  {record[3]}" for record in records])

	ViewConfirmedPassengers_conn_label = Label(root, text = print_records)
	ViewConfirmedPassengers_conn_label.grid(row = 7, column = 1, columnspan = 2)
	ViewConfirmedPassengers_conn.commit()
	ViewConfirmedPassengers_conn.close()

ViewConfirmedPassengers_button = Button(root, text = 'View Confirmed Passengers', command = ViewConfirmedPassengers)
ViewConfirmedPassengers_button.grid(row = 5, column = 1, pady = 10, padx = 10)


def ViewPassengerAge():
	age_entry = age.get()
	ViewPassengerAge_conn = sqlite3.connect('PA3.db')
	ViewPassengerAge_cur = ViewPassengerAge_conn.cursor()
	query = """ SELECT t.'Train Number', t.'source station', t.'Destination station', p.first_name, p.last_name, p.Address, b.Ticket_Type, b.Status, strftime('%Y', 'now') - CAST('19'||substr(p.bdate, LENGTH(p.bdate)-1,2) as INTEGER) as ss 
	FROM Passenger as p 
	JOIN Booked as b ON Passanger_SSN = p.SSN 
	JOIN Train as t ON b.Train_Number=t.'Train Number' WHERE strftime('%Y','now')-CAST('19'||substr(p.bdate,LENGTH(p.bdate)-1,2) as INTEGER) BETWEEN 55 and 60; """
	ViewPassengerAge_cur.execute(query)
	record = ViewPassengerAge_cur.fetchall()
	#print_records = '\n'.join([f"Train Number: {record[0]}, Source station: {record[1]}, Destintion station: {record[2]}, First Name: {record[3]}, Last Name: {record[4]}, Address: {record[5]}, Ticket Type:{record[6]}, Status: {record[7]}, age: {record[8]}  "])
	ViewPassengerAge_conn_label = Label(root, text = record)
	ViewPassengerAge_conn_label.grid(row = 8, column = 0, columnspan = 2)
	ViewPassengerAge_conn.commit()
	ViewPassengerAge_conn.close()
ViewPassengerAge_button = Button(root, text = 'View passenger between Age 50 and 60', command = ViewPassengerAge)
ViewPassengerAge_button.grid(row = 5, column = 2, pady = 10, padx = 10)

def ViewPassengerList():
	ViewPassengerList_conn = sqlite3.connect('PA3.db')
	ViewPassengerList_cur = ViewPassengerList_conn.cursor()
	ViewPassengerList_cur.execute("SELECT Train.'Train Name', COUNT(Booked.Passanger_ssn) AS Passenger_Count FROM Train JOIN Booked ON Train.'Train Number' = Booked.Train_Number GROUP BY Train.'Train Name';")
	records = ViewPassengerList_cur.fetchall()
	print_records = '\n'.join([f"Train Name:{record[0]}      Count:{record[1]} " for record in records])

	ViewPassengerList_conn_label = Label(root, text = print_records)
	ViewPassengerList_conn_label.grid(row = 8, column = 1, columnspan = 2)
	ViewPassengerList_conn.commit()
	ViewPassengerList_conn.close()

ViewPassengerList_button = Button(root, text = 'View Passenger List', command = ViewPassengerList)
ViewPassengerList_button.grid(row = 6, column = 0, pady = 10, padx = 10)

def TrainPassengerList():
	TrainPassengerList_conn = sqlite3.connect('PA3.db')
	TrainPassengerList_cur = TrainPassengerList_conn.cursor()
	TrainPassengerList_cur.execute("SELECT Passenger.first_name, Passenger.last_name, Booked.Ticket_Type FROM Booked, passenger, train where Booked.Train_Number = Train.'Train Number' and Booked.Passanger_ssn = Passenger.SSN and Train.'Train Name' = ? AND Booked.Status = 'Booked';", (TrainName.get(),))
	records = TrainPassengerList_cur.fetchall()
	# print_records = ' '
	# for record in records:
	# 	print_records += str(record[0] + ' ' + record[1] + ' '+ record[2] + ' ' + record[3] + '\n')
	print_records = '\n'.join([f"{record[0]} {record[1]} " for record in records])

	TrainPassengerList_conn_label = Label(root, text = print_records)
	TrainPassengerList_conn_label.grid(row = 9, column = 0, columnspan = 2)
	TrainPassengerList_conn.commit()
	TrainPassengerList_conn.close()

TrainPassengerList_button = Button(root, text = 'Train Passenger List', command = TrainPassengerList)
TrainPassengerList_button.grid(row = 6, column = 1, pady = 10, padx = 10)


def cancelTicket():
    conn = sqlite3.connect('PA3.db')
    cur = conn.cursor()
    
    # Retrieve the passenger and the booked ticket
    cur.execute("SELECT * FROM Booked, passenger WHERE passenger.ssn = ? AND Booked.Train_Number = ? AND Booked.Status = 'Booked'", (ssn.get(), TrainNumber.get(),))
    records = cur.fetchall()
    print_records = '\n'.join([f"{record[0]} {record[1]} {record[2]} {record[3]}" for record in records])
    print(f"Records to be cancelled:\n{print_records}")
    
    # Display the records in a label
    conn_label = Label(root, text=print_records)
    conn_label.grid(row=9, column=1, columnspan=2)

    # Cancel the booked ticket
    # cur.execute("DELETE FROM Booked WHERE Passanger_SSN = ? AND Train_Number = ? AND Status = 'Booked'", (ssn.get(), TrainNumber.get(),))
    


    # cancel the booked ticket
    cur.execute("""DELETE FROM booked where Passanger_Ssn = ? and Train_Number = ?""", ( ssn.get(),TrainNumber.get(),))
    cur.execute('''UPDATE Booked SET Status='Booked'
                 WHERE Passanger_SSN IN (
                 SELECT Passanger_SSN FROM Booked
                 WHERE Train_Number=? AND Status='WaitL'
                 ORDER BY Passanger_SSN ASC LIMIT 1
                  )''', (TrainNumber.get(),))
    cur.execute('')
    conn.commit()
    conn.close()

cancelTicket_button = Button(root, text='Cancel Ticket', command=cancelTicket)
cancelTicket_button.grid(row=6, column=2, pady=10, padx=10)



welcome_label = Label(root, text="Welcome to Railway Reservation System!")
welcome_label.grid(row = 0, column = 0)

first_name_label = Label(root, text = 'First Name: ')
first_name_label.grid(row = 1, column = 0)
first_name = Entry(root, width = 30)
first_name.grid(row = 1, column = 1, padx = 20)

last_name = Entry(root, width=30)
last_name.grid(row = 1, column =3, padx=20)
last_name_label = Label(root, text = 'Last Name: ')
last_name_label.grid(row = 1, column = 2)


ssn = Entry(root,width=30)
ssn.grid(row = 2, column =1, padx= 20)
ssn_label = Label(root, text = 'SSN: ')
ssn_label.grid(row = 2, column = 0)



TrainDate = Entry(root,width=30)
TrainDate.grid(row = 2, column =3, padx= 20)
TrainDate_label = Label(root, text = 'Train Date: ')
TrainDate_label.grid(row = 2, column = 2)

age = Entry(root,width=30)
age.grid(row = 3, column =1, padx= 20)
age_label = Label(root, text = 'Age: ')
age_label.grid(row = 3, column = 0)

TrainName= Entry(root,width=30)
TrainName.grid(row = 3, column =3, padx= 20)
TrainName_label = Label(root, text = 'Train Name: ')
TrainName_label.grid(row = 3, column = 2)

TrainNumber = Entry(root,width=30)
TrainNumber.grid(row = 4, column =1, padx= 20)
TrainNumber_label = Label(root, text = 'Train Number: ')
TrainNumber_label.grid(row = 4, column = 0)


root.mainloop()