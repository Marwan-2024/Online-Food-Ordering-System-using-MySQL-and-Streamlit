import mysql.connector
from datetime import datetime
import streamlit as st


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ONLINE_FOOD_ORDERING_SYSTEM"
)

c = mydb.cursor()




def add_data_cust(C_id, name, address, email, username, password, dob, contact):
    if C_id=="":
        C_id=None
    c.execute('INSERT INTO CUSTOMER VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (C_id, name, address, email, username, password,dob, contact))
    mydb.commit()

def add_data_rest(R_id, name, address, descp, isActive, opening, closing, email, contact):
    if R_id=="":
        R_id=None
    opening = datetime.strptime(opening, '%H:%M:%S').time()    
    closing = datetime.strptime(closing, '%H:%M:%S').time() 
    c.execute('INSERT INTO RESTAURANT VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (R_id, name, address, descp, isActive, opening, closing, email, contact))
    mydb.commit()

def add_data_menu(M_id, R_id, item_name, price, _type, descp):
    if M_id=="":
        M_id=None
    c.execute('INSERT INTO MENU VALUES (%s,%s,%s,%s,%s,%s)',
              (M_id, R_id, item_name, price, _type, descp))
    mydb.commit()

def add_data_order(O_id, C_id, R_id, Del_id, amount, payment_mode, payment_stat, date):
    if O_id=="":
        O_id=None
    c.execute('INSERT INTO ORDER_DETAILS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (O_id, C_id, R_id, Del_id, amount, payment_mode, payment_stat, date))
    mydb.commit()

def add_data_items(OI_id, O_id, M_id, quant, price):
    if OI_id=="":
        OI_id=None
    c.execute('INSERT INTO ORDER_ITEMS VALUES (%s,%s,%s,%s,%s)',
              (OI_id, O_id, M_id, quant, price))
    mydb.commit()

def add_data_del(Del_id, C_id, stat, name, contact, date):
    if Del_id=="":
        Del_id=None
    c.execute('INSERT INTO DELIVERY VALUES (%s,%s,%s,%s,%s,%s)',
              (Del_id, C_id, stat, name, contact, date))
    mydb.commit()





def view_all_cust():
    c.execute('SELECT * FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_all_rest():
    c.execute('SELECT * FROM RESTAURANT')
    data = c.fetchall()
    
    return data

def view_all_menu():
    c.execute('SELECT * FROM MENU ORDER BY R_ID')
    data = c.fetchall()
    return data

def view_all_order():
    c.execute('SELECT * FROM ORDER_DETAILS')
    data = c.fetchall()
    return data

def view_all_items():
    c.execute('SELECT * FROM ORDER_ITEMS ORDER BY O_ID')
    data = c.fetchall()
    return data

def view_all_del():
    c.execute('SELECT * FROM DELIVERY')
    data = c.fetchall()
    return data





def view_only_customer_id():
    c.execute('SELECT C_ID FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_only_rest_id():
    c.execute('SELECT R_ID FROM RESTAURANT')
    data = c.fetchall()
    return data

def view_only_menu_id():
    c.execute('SELECT M_ID FROM MENU')
    data = c.fetchall()
    return data

def view_only_order_id():
    c.execute('SELECT O_ID FROM ORDER_DETAILS')
    data = c.fetchall()
    return data

def view_only_items_id():
    c.execute('SELECT OItems_ID FROM ORDER_ITEMS')
    data = c.fetchall()
    return data

def view_only_del_id():
    c.execute('SELECT Del_ID FROM DELIVERY')
    data = c.fetchall()
    return data




def get_customer(id):
    c.execute("select * from CUSTOMER where C_ID='{}'".format(id))
    data = c.fetchall()
    return data

def get_rest(id):
    c.execute("select * from RESTAURANT where R_ID='{}'".format(id))
    data = c.fetchall()
    return data

def get_menu(id):
    c.execute("select * from MENU where M_ID='{}'".format(id))
    data = c.fetchall()
    return data

def get_order(id):
    c.execute("select * from ORDER_DETAILS where O_ID='{}'".format(id))
    data = c.fetchall()
    return data

def get_items(id):
    c.execute("select * from ORDER_ITEMS where OItems_ID='{}'".format(id))
    data = c.fetchall()
    return data

def get_del(id):
    c.execute("select * from DELIVERY where Del_ID='{}'".format(id))
    data = c.fetchall()
    return data




def edit_data_cust(new_C_id, new_name, new_address, new_email,new_username,new_password, new_dob, new_contact, 
                        C_id, name, address, email, username, password,dob, contact):
    c.execute("UPDATE CUSTOMER SET C_ID=%s, Name=%s, Address=%s, Email=%s,  Username=%s, Password=%s, DOB=%s, Contact=%s where C_ID=%s and Name=%s and Address=%s and Email=%s  and Username=%s and Password=%s and DOB=%s and Contact=%s",
                                    (new_C_id, new_name, new_address,new_email,new_username,new_password, new_dob, new_contact, C_id, name, address, email, username,password, dob, contact))
    mydb.commit()
    c.execute("select C_ID from CUSTOMER")
    data = c.fetchall()
    return data

def edit_data_rest(new_R_id, new_name, new_address, new_descp, new_isActive, new_opening, new_closing, new_email, new_contact,
                                R_id, name, address, descp, isActive, opening, closing, email, contact ):
    print(new_opening)
    new_opening = datetime.strptime(new_opening, '%H:%M:%S').time()    
    new_closing = datetime.strptime(new_closing, '%H:%M:%S').time() 

    c.execute("UPDATE RESTAURANT SET R_ID=%s, Name=%s, Address=%s, Descp=%s,  isActive=%s, Opening_hrs=%s, Closing_hrs=%s, Email=%s, Contact=%s where R_ID=%s and Name=%s and Address=%s and Descp=%s and isActive=%s and Opening_hrs=%s and Closing_hrs=%s and Email=%s  and Contact=%s",
                                (new_R_id, new_name, new_address, new_descp, new_isActive, new_opening, new_closing, new_email, new_contact, R_id, name, address, descp, isActive, opening, closing, email, contact))
    mydb.commit()
    c.execute("select R_ID from RESTAURANT")
    data = c.fetchall()
    return data

def edit_data_menu(new_M_id, new_R_id, new_item_name, new_price, new_type, new_descp, M_id, R_id, item_name, price, _type, descp):
    c.execute("UPDATE MENU SET M_ID=%s, R_ID=%s, Item_Name=%s, Price=%s,  Type=%s, Descp=%s where M_ID=%s and R_ID=%s and Item_Name=%s and Price=%s and Type=%s and Descp=%s",
                                (new_M_id, new_R_id, new_item_name, new_price, new_type, new_descp, M_id, R_id, item_name, price, _type, descp))
    mydb.commit()
    c.execute("select M_ID from MENU")
    data = c.fetchall()
    return data

def edit_data_order(new_O_id, new_C_id, new_R_id, new_Del_id, new_amount, new_payment_mode, new_payment_stat, new_date,
                                O_id, C_id, R_id, Del_id, amount, payment_mode, payment_stat, date):
    c.execute("UPDATE ORDER_DETAILS SET O_ID=%s, C_ID=%s, R_ID=%s, Del_ID=%s, Amount=%s, Payment_Mode=%s, Payment_Status=%s, Date=%s where O_ID=%s and C_ID=%s and R_ID=%s and Del_ID=%s  and Amount=%s and Payment_Mode=%s and Payment_Status=%s and Date=%s",
                                (new_O_id, new_C_id, new_R_id, new_Del_id, new_amount, new_payment_mode, new_payment_stat, new_date, O_id, C_id, R_id, Del_id, amount, payment_mode, payment_stat, date))
    mydb.commit()
    c.execute("select O_ID from ORDER_DETAILS")
    data = c.fetchall()
    return data

def edit_data_items(new_OI_id, new_O_id, new_M_id, new_quant, new_price, OI_id, O_id, M_id, quant, price):
    c.execute("UPDATE ORDER_ITEMS SET OItems_ID=%s, O_ID=%s, M_ID=%s, Quantity=%s, Price=%s where OItems_ID=%s and O_ID=%s and M_ID=%s and Quantity=%s  and Price=%s", 
                                    (new_OI_id, new_O_id, new_M_id, new_quant, new_price, OI_id, O_id, M_id, quant, price))
    mydb.commit()
    c.execute("select OItems_ID from ORDER_ITEMS")
    data = c.fetchall()
    return data

def edit_data_del(new_Del_id, new_C_id, new_stat, new_name, new_contact, new_date, Del_id, C_id, stat, name, contact, date):
    c.execute("UPDATE DELIVERY SET Del_ID=%s, C_ID=%s, Del_Status=%s, Del_Person_Name=%s, Del_Person_Contact=%s, Date=%s where Del_ID=%s and C_ID=%s and Del_Status=%s and Del_Person_Name=%s and Del_Person_Contact=%s and Date=%s",
                                (new_Del_id, new_C_id, new_stat, new_name, new_contact, new_date, Del_id, C_id, stat, name, contact, date))
    mydb.commit()
    c.execute("select Del_ID from DELIVERY")
    data = c.fetchall()
    return data




def delete_cust(id):
    c.execute('DELETE FROM CUSTOMER WHERE C_ID="{}"'.format(id))
    mydb.commit()

def delete_rest(id):
    c.execute('DELETE FROM RESTAURANT WHERE R_ID="{}"'.format(id))
    mydb.commit()

def delete_menu(id):
    c.execute('DELETE FROM MENU WHERE M_ID="{}"'.format(id))
    mydb.commit()

def delete_order(id):
    c.execute('DELETE FROM ORDER_DETAILS WHERE O_ID="{}"'.format(id))
    mydb.commit()

def delete_items(id):
    c.execute('DELETE FROM ORDER_ITEMS WHERE OItems_ID="{}"'.format(id))
    mydb.commit()

def delete_del(id):
    c.execute('DELETE FROM DELIVERY WHERE Del_ID="{}"'.format(id))
    mydb.commit()




def execute_query(q):
    c.execute(q)
    data = c.fetchall()
    return data
