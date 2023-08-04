import streamlit as st
from database import add_data_cust
from database import add_data_rest
from database import add_data_menu
from database import add_data_order
from database import add_data_items
from database import add_data_del


def create(table):
    if table=='Customer':
        col1, col2 = st.columns(2)
        with col1:
            C_id = st.text_input("Customer ID")
            name = st.text_input("Name")
            address = st.text_input("Address")
            email = st.text_input("Email")
        with col2:            
            username = st.text_input("Username")
            password = st.text_input("Password")
            dob = st.date_input("DOB")
            contact= st.text_input("Contact")
            
        if st.button("Add"):
            add_data_cust(C_id, name, address, email, username, password, dob, contact)
            st.success("Successfully added customer: {}".format(name))

    elif table=='Restaurant':
        col1, col2 = st.columns(2)
        with col1:
            R_id = st.text_input("Restaurant ID")
            name = st.text_input("Name")
            address = st.text_input("Address")
            descp = st.text_input("Description")
        with col2:            
            isActive = st.selectbox("is Active",["Yes", "No"])
            opening = st.text_input("Opening hours")
            closing = st.text_input("Closing hours")
            email= st.text_input("Email")
            contact= st.text_input("Contact")
             
        if st.button("Add"):
            add_data_rest(R_id, name, address, descp, isActive, opening, closing, email, contact)
            st.success("Successfully added restaurant: {}".format(name))


    elif table=='Menu':
        col1, col2 = st.columns(2)
        with col1:
            M_id = st.text_input("Menu Item ID")
            R_id = st.text_input("Restaurant ID")
            item_name = st.text_input("Item name")
        
        with col2:           
            price = st.text_input("Price")
            _type = st.text_input("Type")
            descp = st.text_input("Description") 


        if st.button("Add"):
            add_data_menu(M_id, R_id, item_name, float(price), _type, descp)
            st.success("Successfully added menu item: {} for restaurant: {} ".format(M_id,R_id))

    elif table=='Order Details':
        col1, col2 = st.columns(2)
        with col1:
            O_id = st.text_input("Order ID")
            C_id = st.text_input("Customer ID")
            R_id = st.text_input("Restaurant ID")
            Del_id = st.text_input("Delivery ID")

        with col2:            
            amount = st.text_input("Amount")
            payment_mode = st.selectbox("Payment Mode",["Credit Card", "Debit Card", "UPI", "Cash on Delivery"])
            payment_stat = st.selectbox("Payment Status",["Pending", "Processing", "Success","Failed"])
            date = st.date_input("Date")

            
        if st.button("Add"):
            add_data_order(O_id, C_id, R_id, Del_id, float(amount), payment_mode, payment_stat, date)
            st.success("Successfully added order detail: {}".format(O_id))


    elif table=='Order Items':
        col1, col2 = st.columns(2)
        with col1:
            OI_id = st.text_input("Order Item ID")
            O_id = st.text_input("Order Details ID")
            M_id = st.text_input("Menu ID")
        with col2:            
            quant= st.text_input("Quantity")
            price= st.text_input("Price")

        if st.button("Add"):
            add_data_items(OI_id, O_id, M_id, int(quant), float(price))
            st.success("Successfully added order item: {}".format(O_id))

    elif table=='Delivery':
        col1, col2 = st.columns(2)
        with col1:
            Del_id = st.text_input("Delivery ID")
            C_id = st.text_input("Customer ID")
            stat = st.selectbox("Delivery Status",["Order placed", "Preparing your food", "Delivery agent has picked up your order", "On the way", "At your doorstep", "Delivered"])
        
        with col2:           
            name = st.text_input("Delivery Person Name")
            contact = st.text_input("Delivery Person Contact")
            date = st.date_input("Date") 

        if st.button("Add"):
            add_data_del(Del_id, C_id, stat, name, contact, date)
            st.success("Successfully added delivery details: {}".format(Del_id))