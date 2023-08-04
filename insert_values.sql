
INSERT INTO CUSTOMER VALUES ("C1", "Riya Sharma", "#3091, Indiranagar, Bangalore", "riya34@gmail.com", "riyas23", "riya98!", "2001-06-23", "9801254763");
INSERT INTO CUSTOMER VALUES ("C2", "Josh Lobo", "1201, Skyline, Bell Road, Bangalore", "josh@gmail.com", "josh_lobo", "josh78", "2003-10-04", "8702469551");
INSERT INTO CUSTOMER VALUES ("C3", "Anushka Raj", "#4961, 80ft Road, Jaynager, Bangalore", "anu91@gmail.com", "anushka.19", "anu-raj3", "1998-02-27", "9760122485");


INSERT INTO DELIVERY VALUES ("D1", "C1", "Preparing your food", "Parth Joshi", "7510348567", "2022-11-21");
INSERT INTO DELIVERY VALUES ("D2", "C3", "On the way", "Sharan Bhat", "7824591140", "2022-11-21");
INSERT INTO DELIVERY VALUES ("D3", "C1", "Delivered", "Shravya Anand", "9842603357", "2022-11-19");
INSERT INTO DELIVERY VALUES ("D4", "C2", "At your doorstep", "Likith Arya", "9751023488", "2022-11-21");


INSERT INTO RESTAURANT VALUES ("R1", "McDonald's", "JP Nagar, Bangalore", "FastFood", "", "09:00:00", "00:30:00", "mcd@gmail.com", "8751304257");
INSERT INTO RESTAURANT VALUES ("R2", "Nandana", "Bhanshankari, Bangalore", "South Indian", "", "11:00:00", "23:30:00", "nandana@gmail.com", "8790224468");
INSERT INTO RESTAURANT VALUES ("R3", "Glens", "MG Road, Bangalore", "Bakery", "", "09:00:00", "22:59:00", "glens@gmail.com", "9741120539");


INSERT INTO MENU VALUES ("M1", "R1", "Panner wrap", 200, "Wraps", "Spicy paneer with creamy sauce");
INSERT INTO MENU VALUES ("M2", "R1", "Chicken Nuggets", 120, "", "8 pcs.");
INSERT INTO MENU VALUES ("M5", "R1", "Grilled Chicken Burger", 250, "Burgers", "Grilled chicken, cheese, jalapenos");
INSERT INTO MENU VALUES ("M3", "R2", "Ghee Rice", 190, "Veg Main Course", "");
INSERT INTO MENU VALUES ("M4", "R2", "Egg Fried Rice/Noodles", 250, "Non-Veg Main Course", "");
INSERT INTO MENU VALUES ("M8", "R3", "Red Velvet Cupcake", 50, "Dessert", "");
INSERT INTO MENU VALUES ("M9", "R3", "Red Pesto Pasta", 300, "Italian", "Veg red pesto macroni/penne pasta");
INSERT INTO MENU VALUES ("M10", "R2", "Chicken Biryani", 400, "Biryani", "Hyderabadi Dum Biryani");


INSERT INTO ORDER_DETAILS VALUES ("O1", "C1", "R3", "D1", "", "UPI", "Processing", "2022-11-21");
INSERT INTO ORDER_DETAILS VALUES ("O2", "C3", "R1", "D2", "", "Debit Card", "Pending", "2022-11-21");
INSERT INTO ORDER_DETAILS VALUES ("O3", "C1", "R1", "D3", "", "UPI", "Success", "2022-11-19");
INSERT INTO ORDER_DETAILS VALUES ("O4", "C2", "R2", "D4", "", "Cash On Delivery", "Pending", "2022-11-21");

INSERT INTO ORDER_ITEMS VALUES ("OI1", "O1", "M8", 6,"");
INSERT INTO ORDER_ITEMS VALUES ("OI2", "O1", "M9", 1,"");
INSERT INTO ORDER_ITEMS VALUES ("OI4", "O2", "M2", 3,"");
INSERT INTO ORDER_ITEMS VALUES ("OI5", "O2", "M5", 1,"");
INSERT INTO ORDER_ITEMS VALUES ("OI8", "O3", "M1", 2,"");
INSERT INTO ORDER_ITEMS VALUES ("OI15", "O4", "M3", 1,"");
INSERT INTO ORDER_ITEMS VALUES ("OI16", "O4", "M10", 2,"");