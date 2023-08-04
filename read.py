import pandas as pd
import streamlit as st
from database import view_all_cust
from database import view_all_rest
from database import view_all_menu
from database import view_all_order
from database import view_all_items
from database import view_all_del




def read(table):
    if table =="Customer":
        result = view_all_cust()
        df = pd.DataFrame(result, columns=["C_ID","Name","Address","Email","Username","Password","DOB","Contact"])    
        with st.expander("View all Customers"):
            st.dataframe(df)
    
    elif table == "Restaurant":
        result = view_all_rest()
        df = pd.DataFrame(result, columns=["R_ID", "Name", "Address", "Descp", "is Active", "Opening hrs", "Closing hrs", "Email", "Contact"])  
        df["Opening hrs"] = df["Opening hrs"].values.astype('datetime64[ns]')
        df["Opening hrs"]=df["Opening hrs"].dt.strftime('%H:%M:%S')
        df["Closing hrs"] = df["Closing hrs"].values.astype('datetime64[ns]') 
        df["Closing hrs"]=df["Closing hrs"].dt.strftime('%H:%M:%S')
        with st.expander("View all Restaurants"):
            st.dataframe(df)

    elif table == "Menu":
        result = view_all_menu()
        df = pd.DataFrame(result, columns=["M_ID", "R_ID", "Item Name", "Price", "Type", "Descp"])        
        with st.expander("View all Menu Items"):
            st.dataframe(df)

    elif table == "Order Details":
        result = view_all_order() 
        df = pd.DataFrame(result, columns=["O_ID","C_ID","R_ID","Del_ID","Amount","Payment Mode","Payment Status","Date"])        
        with st.expander("View all Order Details"):
            st.dataframe(df)

    elif table == "Order Items":
        result = view_all_items() 
        df = pd.DataFrame(result, columns=["OItems_ID","O_ID","M_ID","Quantity","Price"])        
        with st.expander("View all Order Items"):
            st.dataframe(df)
        
    elif table == "Delivery":
        result = view_all_del() 
        df = pd.DataFrame(result, columns=["Del_ID","C_ID","Del Status","Del Person Name","Del Person Contact","Date"])        
        with st.expander("View all Delivery Details"):
            st.dataframe(df)
