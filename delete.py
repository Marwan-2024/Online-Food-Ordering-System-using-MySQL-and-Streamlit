import pandas as pd
import streamlit as st
from database import view_all_cust, view_only_customer_id, delete_cust
from database import view_all_rest, view_only_rest_id, delete_rest
from database import view_all_menu, view_only_menu_id, delete_menu
from database import view_all_order, view_only_order_id, delete_order
from database import view_all_items, view_only_items_id, delete_items
from database import view_all_del, view_only_del_id, delete_del


def delete(table):
    if table == "Customer":
        result = view_all_cust()
        # st.write(result) 
        df = pd.DataFrame(result, columns=["C_ID","Name","Address","Email","Username","Password","DOB","Contact"]) 
        with st.expander("View Customer"):
            st.dataframe(df)

        list_of_cust = [i[0] for i in view_only_customer_id()]
        selected_cust = st.selectbox("Customer to Delete", list_of_cust)
        st.warning("Do you want to delete customer:{}".format(selected_cust))
        
        if st.button("Delete"):
            delete_cust(selected_cust)
            st.success("Successfully deleted")

        new_result = view_all_cust()
        df = pd.DataFrame(new_result, columns=["C_ID","Name","Address","Email","Username","Password","DOB","Contact"]) 
        with st.expander("Updated Customer"):
            st.dataframe(df)

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
        selected_rest = st.selectbox("Customer to Delete", list_of_rest)
        st.warning("Do you want to delete restaurant:{}".format(selected_rest))
        
        if st.button("Delete"):
            delete_rest(selected_rest)
            st.success("Successfully deleted")

        new_result = view_all_rest()
        df = pd.DataFrame(new_result, columns=["R_ID", "Name", "Address", "Descp", "is Active", "Opening hrs", "Closing hrs", "Email", "Contact"]) 
        df["Opening hrs"] = df["Opening hrs"].values.astype('datetime64[ns]')
        df["Opening hrs"]=df["Opening hrs"].dt.strftime('%H:%M:%S')
        df["Closing hrs"] = df["Closing hrs"].values.astype('datetime64[ns]') 
        df["Closing hrs"]=df["Closing hrs"].dt.strftime('%H:%M:%S') 
        with st.expander("Updated Restaurant"):
            st.dataframe(df)

    elif table=="Menu":
        result = view_all_menu()
        df = pd.DataFrame(result, columns=["M_ID", "R_ID", "Item Name", "Price", "Type", "Descp"]) 
        with st.expander("View Menu"):
            st.dataframe(df)

        list_of_menu = [i[0] for i in view_only_menu_id()]
        selected_menu = st.selectbox("Menu Item to Delete", list_of_menu)
        st.warning("Do you want to delete menu item: {}".format(selected_menu))
        
        if st.button("Delete"):
            delete_menu(selected_menu)
            st.success("Successfully deleted")

        new_result = view_all_menu()
        df = pd.DataFrame(new_result, columns=["M_ID", "R_ID", "Item Name", "Price", "Type", "Descp"]) 
        with st.expander("Updated Menu"):
            st.dataframe(df)        

    elif table=="Order Details":
        result = view_all_order()
        df = pd.DataFrame(result, columns=["O_ID","C_ID","R_ID","Del_ID","Amount","Payment Mode","Payment Status","Date"]) 
        with st.expander("View Order Details"):
            st.dataframe(df)

        list_of_order = [i[0] for i in view_only_order_id()]
        selected_order = st.selectbox("Order to Delete", list_of_order)
        st.warning("Do you want to delete order: {}".format(selected_order))
        
        if st.button("Delete"):
            delete_order(selected_order)
            st.success("Successfully deleted")

        new_result = view_all_order()
        df = pd.DataFrame(new_result, columns=["O_ID","C_ID","R_ID","Del_ID","Amount","Payment Mode","Payment Status","Date"]) 
        with st.expander("Updated Order Details"):
            st.dataframe(df) 

    elif table=="Order Items":
        result = view_all_items()
        df = pd.DataFrame(result, columns=["OItems_ID","O_ID","M_ID","Quantity","Price"]) 
        with st.expander("View Order Items"):
            st.dataframe(df)

        list_of_items = [i[0] for i in view_only_items_id()]
        selected_items = st.selectbox("Order Item to Delete", list_of_items)
        st.warning("Do you want to delete order item: {}".format(selected_items))
        
        if st.button("Delete"):
            delete_items(selected_items)
            st.success("Successfully deleted")

        new_result = view_all_items()
        df = pd.DataFrame(new_result, columns=["OItems_ID","O_ID","M_ID","Quantity","Price"]) 
        with st.expander("Updated Order Items"):
            st.dataframe(df) 
    
    elif table=="Delivery":
        result = view_all_del()
        df = pd.DataFrame(result, columns=["Del_ID","C_ID","Del Status","Del Person Name","Del Person Contact","Date"]) 
        with st.expander("View Delivery Details"):
            st.dataframe(df)

        list_of_del = [i[0] for i in view_only_del_id()]
        selected_del = st.selectbox("Delivery Detail to Delete", list_of_del)
        st.warning("Do you want to delete Delivery Detail {}".format(selected_del))
        
        if st.button("Delete"):
            delete_del(selected_del)
            st.success("Successfully deleted")

        new_result = view_all_del()
        df = pd.DataFrame(new_result, columns=["Del_ID","C_ID","Del Status","Del Person Name","Del Person Contact","Date"]) 
        with st.expander("Updated Delivery Details"):
            st.dataframe(df) 