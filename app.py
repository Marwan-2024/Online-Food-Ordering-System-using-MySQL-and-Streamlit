import streamlit as st
from create import create
from delete import delete
from read import read
from update import update
from queries import query

def main():
    st.title("ONLINE FOOD ORDER")
    menu = ["Add", "View", "Update", "Delete","Query"]
    table_names= ["Customer", "Restaurant","Menu","Order Details","Order Items","Delivery"]
    
    table = st.sidebar.selectbox("Table", table_names)
    choice = st.sidebar.selectbox("Action", menu)

    if choice == "Add":
        if table=="Customer":
            st.subheader("Enter Customer Details:")
            create(table)
        elif table=="Restaurant":
            st.subheader("Enter Restaurant Details:")
            create(table)
        elif table=="Menu":
            st.subheader("Enter Menu Details:")
            create(table)
        elif table=="Order Details":
            st.subheader("Enter Order Details:")
            create(table)
        elif table=="Order Items":
            st.subheader("Enter Order Items Details:")
            create(table)
        elif table=="Delivery":
            st.subheader("Enter Delivery Details:")
            create(table)
        
    
    elif choice == "View":
        if table=="Customer":
            st.subheader("View Customer Details:")
            read(table)
        elif table=="Restaurant":
            st.subheader("View Restaurant Details:")
            read(table)
        elif table=="Menu":
            st.subheader("View Menu Details:")
            read(table)
        elif table=="Order Details":
            st.subheader("View Order Details:")
            read(table)
        elif table=="Order Items":
            st.subheader("View Order Items Details:")
            read(table)
        elif table=="Delivery":
            st.subheader("View Delivery Details:")
            read(table)
    
    elif choice == "Update":
        if table=="Customer":
            st.subheader("Upddate Customer Details:")
            update(table)
        elif table=="Restaurant":
            st.subheader("Upddate Restaurant Details:")
            update(table)
        elif table=="Menu":
            st.subheader("Upddate Menu Details:")
            update(table)
        elif table=="Order Details":
            st.subheader("Upddate Order Details:")
            update(table)
        elif table=="Order Items":
            st.subheader("Upddate Order Items Details:")
            update(table)
        elif table=="Delivery":
            st.subheader("Upddate Delivery Details:")
            update(table)
    
    elif choice == "Delete":
        if table=="Customer":
            st.subheader("Delete Customer Details:")
            delete(table)
        elif table=="Restaurant":
            st.subheader("Delete Restaurant Details:")
            delete(table)
        elif table=="Menu":
            st.subheader("Delete Menu Details:")
            delete(table)
        elif table=="Order Details":
            st.subheader("Delete Order Details:")
            delete(table)
        elif table=="Order Items":
            st.subheader("Delete Order Items Details:")
            delete(table)
        elif table=="Delivery":
            st.subheader("Delete Delivery Details:")
            delete(table)
    
    elif choice=='Query':
        st.subheader("Enter Query:")
        query()


if __name__ == '__main__':
    main()