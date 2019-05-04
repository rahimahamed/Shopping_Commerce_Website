import sqlite3

connection = sqlite3.connect("ecommerce.db")

connection.execute('''CREATE TABLE Item (
  Name VARCHAR(45),
  ArticleID INT,
  ItemType VARCHAR(45),
  Price DOUBLE,
  SellerID INT,
  Image TEXT,
  PRIMARY KEY (ArticleID))
''')

connection.execute('''CREATE TABLE Customer (
  CustomerID INT,
  PhoneNumber VARCHAR(45),
  FirstName VARCHAR(45),
  LastName VARCHAR(45),
  EmailID VARCHAR(45),
  Password TEXT,
  Address VARCHAR(100),
  PRIMARY KEY (CustomerID));
''')

connection.execute('''CREATE TABLE Payment (
  OrderID INT  ,
  PaymentType VARCHAR(45),
  CardNumber INT  ,
  CardExpirationDate DATE,
  PRIMARY KEY (OrderID, CardNumber));
''')

connection.execute('''CREATE TABLE Shipment(
  ShipmentID INT  ,
  ShipmentType VARCHAR(45),
  PhysicalAddress VARCHAR(45),
  ShipmentCharge DOUBLE,
  ShipmentDetails VARCHAR(100),
  OrderID INT UNIQUE ,
  PRIMARY KEY (ShipmentID));

''')

connection.execute('''CREATE TABLE Orders (
  OrderID INT  ,
  TotalPrice DOUBLE NULL,
  PlacedOn DATE NULL,
  PRIMARY KEY (OrderID));

''')

connection.execute('''CREATE TABLE Reviews (
  ArticleID INT,
  SellerID INT,
  CustomerID INT,
  Ratings INT,
  DetailedReview VARCHAR(100),
  PRIMARY KEY (ArticleID, SellerID, CustomerID),
  FOREIGN KEY (CustomerID)
    REFERENCES Customer(CustomerID),
  FOREIGN KEY (ArticleID)
    REFERENCES Item(ArticleID),
 FOREIGN KEY (SellerID)
    REFERENCES Item(SellerID));
''')

connection.execute('''CREATE TABLE Employee(
  EmployeeID INT,
  Role VARCHAR(45) ,
  DateJoined DATE,
  SupervisorID INT,
  PRIMARY KEY (EmployeeID));
''')

connection.execute('''CREATE TABLE ShoppingCart(
  ArticleID INT,
  CustomerID INT,
  ShoppingCartID INT,
  TotalPrice DOUBLE,
  PricePerItem VARCHAR(100),
  QuantityOfItems VARCHAR(100),
  ItemsBought VARCHAR(100),
  PRIMARY KEY (CustomerID, ArticleID),
  FOREIGN KEY (CustomerID)
    REFERENCES Customer(CustomerID),
  FOREIGN KEY (ArticleID)
    REFERENCES Item(ArticleID));
''')

connection.execute('''CREATE TABLE Inventory(
  ItemID INT,
  ItemName VARCHAR(45),
  Quantity INT,
  Price DOUBLE,
  SellerID INT ,
  PRIMARY KEY (ItemID));
''')

connection.execute('''CREATE TABLE _adds_item_to_cart_ (
  Quantity INT,
  CustomerID INT,
  ShoppingCartID INT,
  ArticleID INT,
  SellerID INT,
  PRIMARY KEY (ArticleID, ShoppingCartID, CustomerID),
  FOREIGN KEY (CustomerID)
    REFERENCES Customer(CustomerID),
  FOREIGN KEY (ArticleID)
    REFERENCES Item(ArticleID),
  FOREIGN KEY (ShoppingCartID)
    REFERENCES ShoppingCart(ShoppingCartID),
  FOREIGN KEY (SellerID)
    REFERENCES Item(SellerID));
''')

connection.execute('''CREATE TABLE _has_ (
  ArticleID INT ,
  SellerID INT,
  CustomerID INT,
  PRIMARY KEY (ArticleID, SellerID, CustomerID),
  FOREIGN KEY (ArticleID)
    REFERENCES Item(ArticleID),
  FOREIGN KEY (SellerID)
    REFERENCES Item(SellerID),
  FOREIGN KEY (CustomerID)
    REFERENCES Customer(CustomerID));
''')

connection.execute('''CREATE TABLE  _contains_(
  ArticleID INT,
  ShoppingCartID INT,
  PRIMARY KEY (ArticleID, ShoppingCartID),
  FOREIGN KEY (ArticleID)
    REFERENCES Item(ArticleID),
  FOREIGN KEY (ShoppingCartID)
    REFERENCES ShoppingCart(ShoppingCartID));
''')

connection.execute('''CREATE TABLE _maintains_(
  EmployeeID INT,
  ItemID INT,
  PRIMARY KEY (EmployeeID, ItemID),
    FOREIGN KEY (EmployeeID)
    REFERENCES Employee(EmployeeID),
    FOREIGN KEY (ItemID)
    REFERENCES Inventory(ItemID));
''')

connection.execute('''CREATE TABLE _creates_ (
  CustomerID INT,
  OrderID INT,
  PRIMARY KEY (CustomerID, OrderID),
  FOREIGN KEY (CustomerID)
    REFERENCES Customer (CustomerID),
  FOREIGN KEY (OrderID)
    REFERENCES Orders (OrderID));
''')

connection.execute('''CREATE TABLE _payed_by_ (
  CustomerID INT,
  OrderID INT,
  CardNumber INT,
  PRIMARY KEY (CustomerID, CardNumber, OrderID),
  FOREIGN KEY (CustomerID)
    REFERENCES Customer (CustomerID),
  FOREIGN KEY (OrderID)
    REFERENCES Orders (OrderID),
  FOREIGN KEY (CardNumber)
    REFERENCES Payment (CardNumber)
   );
''')

connection.execute('''CREATE TABLE _shipped_ (
  ShipmentID INT ,
  OrderID INT,
  PRIMARY KEY (ShipmentID),
  FOREIGN KEY (ShipmentID)
    REFERENCES Shipment(ShipmentID),
  FOREIGN KEY (OrderID)
    REFERENCES Orders(OrderID)
   );
''')

connection.execute('''CREATE TABLE _carries_ (
  OrderID INT,
  ShoppingCartID INT,
  PRIMARY KEY (OrderID),
  FOREIGN KEY (OrderID)
    REFERENCES Orders (OrderID),
  FOREIGN KEY (ShoppingCartID)
    REFERENCES ShoppingCart (ShoppingCartID)
   );
''')

connection.execute('''CREATE TABLE _verifies_ (
  EmployeeID INT,
  CardNumber INT,
  ShipmentID INT,
  PRIMARY KEY (EmployeeID, CardNumber, ShipmentID),
  FOREIGN KEY (EmployeeID)
    REFERENCES Employee(EmployeeID),
  FOREIGN KEY (CardNumber)
    REFERENCES Payment (CardNumber),
  FOREIGN KEY (ShipmentID)
    REFERENCES Shipment(ShipmentID)
   );
''')

crsr = connection.cursor()

crsr.execute("SELECT * FROM Item")

ans = crsr.fetchall()

for i in ans:
    print(i)

connection.commit()

connection.close()