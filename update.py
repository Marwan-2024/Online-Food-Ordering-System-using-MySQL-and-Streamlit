import pandas as pd
import streamlit as st
from database import view_all_cust,  view_only_customer_id, get_customer, edit_data_cust
from database import view_all_rest, view_only_rest_id, get_rest, edit_data_rest
from database import view_all_menu, view_only_menu_id, get_menu, edit_data_menu
from database import view_all_order, view_only_order_id, get_order, edit_data_order
from database import view_all_items, view_only_items_id, get_items, edit_data_items
from database import view_all_del, view_only_del_id, get_del, edit_data_del



def update(table):
    # st.write(result) 
    if table=="Customer":
        result = view_all_cust()
        df = pd.DataFrame(result, columns=["C_ID","Name","Address","Email","Username","Password","DOB", "Contact"]) 
        
        with st.expander("View Customer"):
            st.dataframe(df)

        list_of_cust = [i[0] for i in view_only_customer_id()]
        selected_cust = st.selectbox("Edit Customer", list_of_cust)
        selected_result = get_customer(selected_cust)

        if selected_result:
            C_id =selected_result[0][0]
            name = selected_result[0][1]
            address = selected_result[0][2]
            email = selected_result[0][3]   
            username=selected_result[0][4]
            password = selected_result[0][5]
            dob = selected_result[0][6]
            contact = selected_result[0][7]

            col1, col2 = st.columns(2)
            with col1:
                new_C_id = st.text_input("ID", C_id)
                new_name = st.text_input("Name", name)
                new_address = st.text_input("Address",address)
                new_email = st.text_input("Email",email)

            with col2:
                new_username = st.text_input("Username",username)
                new_password = st.text_input("Password",password)
                new_dob= st.date_input("DOB",dob)
                new_contact= st.text_input("Contact",contact)

            if st.button("Update"):
                    edit_data_cust(new_C_id, new_name, new_address, new_email, new_username,new_password, new_dob, new_contact, 
                                        C_id, name, address, email, username,password, dob, contact )
                    st.success("Successully updated Customer: {} ".format(new_name))   


        result2 = view_all_cust()
        df2 = pd.DataFrame(result2, columns=["C_ID","Name","Address","Email","Username","Password","DOB","Contact"])
        with st.expander("Updated Customer"):
            st.dataframe(df2)

    
    elif table=="Restaurant":
        result = view_all_rest()
        df = pd.DataFrame(result, columns=["R_ID", "Name", "Address", "Descp", "is Active", "Opening hrs", "Closing hrs", "Email", "Contact"]) 
        df["Opening hrs"] = df["Opening hrs"].values.astype('datetime64[ns]')
        df["Opening hrs"]=df["Opening hrs"].dt.strftime('%H:%M:%S')
        df["Closing hrs"] = df["Closing hrs"].values.astype('datetime64[ns]') 
        df["Closing hrs"]=df["Closing hrs"].dt.strftime('%H:%M:%S')
        with st.expander("View Restaurant"):
            st.dataframe(df)

        list_of_rest = [i[0] for i in view_only_rest_id()]
        selected_rest = st.selectbox("Edit Restaurant", list_of_rest)
        selected_result = get_rest(selected_rest)

        if selected_result:
            R_id =selected_result[0][0]
            name = selected_result[0][1]
            address = selected_result[0][2]
            descp=selected_result[0][3]
            isActive = selected_result[0][4]
            opening = selected_result[0][5]
            closing = selected_result[0][6]
            email = selected_result[0][7]             
            contact = selected_result[0][8]

            col1, col2 = st.columns(2)
            with col1:
                new_R_id = st.text_input("Restaurant ID",R_id)
                new_name = st.text_input("Name",name)
                new_address = st.text_input("Address",address)
                new_descp = st.text_input("Description",descp)

            with col2:
                new_isActive = st.selectbox("is Active",["Yes", "No"])
                new_opening = st.text_input("Opening hours",opening)
                new_closing = st.text_input("Closing hours",closing)
                new_email= st.text_input("Email",email)
                new_contact= st.text_input("Contact",contact)

            if st.button("Update"):
                    edit_data_rest(new_R_id, new_name, new_address, new_descp, new_isActive, new_opening, new_closing, new_email, new_contact,
                                R_id, name, address, descp, isActive, opening, closing, email, contact )
                    st.success("Successully updated Restaurant: {} ".format(new_name))   


        result2 = view_all_rest()
        df2= pd.DataFrame(result2, columns=["R_ID", "Name", "Address", "Descp", "is Active", "Opening hrs", "Closing hrs", "Email", "Contact"])
        df2["Opening hrs"] = df2["Opening hrs"].values.astype('datetime64[ns]')
        df2["Opening hrs"]=df2["Opening hrs"].dt.strftime('%H:%M:%S')
        df2["Closing hrs"] = df2["Closing hrs"].values.astype('datetime64[ns]') 
        df2["Closing hrs"]=df2["Closing hrs"].dt.strftime('%H:%M:%S')
        with st.expander("Updated Restaurant"):
            st.dataframe(df2)

    elif table=="Menu":
        result = view_all_menu()
        df = pd.DataFrame(result, columns=["M_ID", "R_ID", "Item Name", "Price", "Type", "Descp"]) 
        
        with st.expander("View Menu"):
            st.dataframe(df)

        list_of_menu = [i[0] for i in view_only_menu_id()]
        selected_menu = st.selectbox("Edit Menu Item", list_of_menu)
        selected_result = get_menu(selected_menu)

        if selected_result:
            M_id = selected_result[0][0]
            R_id =selected_result[0][1]
            item_name = selected_result[0][2]
            price = selected_result[0][3]
            _type = selected_result[0][4]
            descp=selected_result[0][5]
            
            col1, col2 = st.columns(2)
            with col1:
                new_M_id = st.text_input("Menu Item ID",M_id)
                new_R_id = st.text_input("Restaurant ID",R_id)
                new_item_name = st.text_input("Item name",item_name)
            
            with col2:           
                new_price = st.text_input("Price",price)
                new_type = st.text_input("Type",_type)
                new_descp = st.text_input("Description",descp)

            if st.button("Update"):
                    edit_data_menu(new_M_id, new_R_id, new_item_name, float(new_price), new_type, new_descp,
                                M_id, R_id, item_name, price, _type, descp)
                    st.success("Successully updated Menu Item: {} for Restaurant: {} ".format(new_M_id,new_R_id))   


        result2 = view_all_menu()
        df2 = pd.DataFrame(result2, columns=["M_ID", "R_ID", "Item Name", "Price", "Type", "Descp"])
        with st.expander("Updated Menu"):
            st.dataframe(df2)

    elif table=="Order Details":
        result = view_all_order()
        df = pd.DataFrame(result, columns=["O_ID","C_ID","R_ID","Del_ID","Amount","Payment Mode","Payment Status","Date"]) 
        
        with st.expander("View Order Details"):
            st.dataframe(df)

        list_of_order = [i[0] for i in view_only_order_id()]
        selected_order = st.selectbox("Edit Order", list_of_order)
        selected_result = get_order(selected_order)

        if selected_result:
            O_id = selected_result[0][0]
            C_id = selected_result[0][1]
            R_id =selected_result[0][2]
            Del_id = selected_result[0][3]
            amount = selected_result[0][4]
            payment_mode = selected_result[0][5]
            payment_stat = selected_result[0][6]
            date = selected_result[0][7]

            
            col1, col2 = st.columns(2)
            with col1:
                new_O_id = st.text_input("Order ID",O_id)
                new_C_id = st.text_input("Customer ID",C_id)
                new_R_id = st.text_input("Restaurant ID",R_id)
                new_Del_id = st.text_input("Delivery ID",Del_id)

            with col2:            
                new_amount = st.text_input("Amount",amount)
                new_payment_mode = st.selectbox("Payment Mode",["Credit Card", "Debit Card", "UPI", "Cash on Delivery"])
                new_payment_stat = st.selectbox("Payment Status",["Pending", "Processing", "Success","Failed"])
                new_date = st.date_input("Date",date)

            if st.button("Update"):
                    edit_data_order(new_O_id, new_C_id, new_R_id, new_Del_id, float(new_amount), new_payment_mode, new_payment_stat, new_date,
                                O_id, C_id, R_id, Del_id, amount, payment_mode, payment_stat, date)
                    st.success("Successully updated Order Detail:  ".format(new_O_id))   


        result2 = view_all_order()
        df2 = pd.DataFrame(result2, columns=["O_ID","C_ID","R_ID","Del_ID","Amount","Payment Mode","Payment Status","Date"])
        with st.expander("Updated Order Details"):
            st.dataframe(df2)

    elif table=="Order Items":
        result = view_all_items()
        df = pd.DataFrame(result, columns=["OItems_ID","O_ID","M_ID","Quantity","Price"]) 
        
        with st.expander("View Order Items"):
            st.dataframe(df)

        list_of_items = [i[0] for i in view_only_items_id()]
        selected_items = st.selectbox("Edit Order Item", list_of_items)
        selected_result = get_items(selected_items)

        if selected_result:
            OI_id = selected_result[0][0]
            O_id = selected_result[0][1]
            M_id =selected_result[0][2]
            quant = selected_result[0][3]
            price = selected_result[0][4]
            
            col1, col2 = st.columns(2)
            with col1:
                new_OI_id = st.text_input("Order Item ID",OI_id)
                new_O_id = st.text_input("Order Details ID",O_id)
                new_M_id = st.text_input("Menu ID",M_id)
            with col2:            
                new_quant= st.text_input("Quantity",quant)
                new_price= st.text_input("Price",price)

            if st.button("Update"):
                    edit_data_items(new_OI_id, new_O_id, new_M_id, int(new_quant),float(new_price),
                                OI_id, O_id, M_id, quant, price)
                    st.success("Successully updated Order Item: {} ".format(new_OI_id))   


        result2 = view_all_items()
        df2 = pd.DataFrame(result2, columns=["OItems_ID","O_ID","M_ID","Quantity","Price"])
        with st.expander("Updated Order Item"):
            st.dataframe(df2)

    elif table=="Delivery":
        result = view_all_del()
        df = pd.DataFrame(result, columns=["Del_ID","C_ID","Del Status","Del Person Name","Del Person Contact","Date"]) 
        
        with st.expander("View Delivery Details"):
            st.dataframe(df)

        list_of_del = [i[0] for i in view_only_del_id()]
        selected_del = st.selectbox("Edit Delivery ", list_of_del)
        selected_result = get_del(selected_del)

        if selected_result:
            Del_id = selected_result[0][0]
            C_id =selected_result[0][1]
            stat = selected_result[0][2]
            name = selected_result[0][3]
            contact = selected_result[0][4]
            date = selected_result[0][5]
            
            col1, col2 = st.columns(2)
            with col1:
                new_Del_id = st.text_input("Delivery ID",Del_id)
                new_C_id = st.text_input("Customer ID",C_id)
                new_stat = st.selectbox("Delivery Status",["Order placed", "Preparing your food", "delivery agent has picked up your order", "On the way", "At your doorstep", "Delivered"])
            
            with col2:           
                new_name = st.text_input("Delivery Person Name",name)
                new_contact = st.text_input("Delivery Person Contact",contact)
                new_date = st.date_input("Date",date) 

            if st.button("Update"):
                    edit_data_del(new_Del_id, new_C_id, new_stat, new_name, new_contact, new_date,
                                Del_id, C_id, stat, name, contact, date)
                    st.success("Successully updated Delivery Details: {}".format(new_Del_id))   


        result2 = view_all_del()
        df2 = pd.DataFrame(result2, columns=["Del_ID","C_ID","Del Status","Del Person Name","Del Person Contact","Date"])
        with st.expander("Updated Delivery Details"):
            st.dataframe(df2)