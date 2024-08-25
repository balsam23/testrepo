import sqlite3

# Function to create the database and tables
def create_database():
    # Connect to SQLite database (it will create the database if it doesn't exist)
    conn = sqlite3.connect('boncafe.db')
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Create Product table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Product (
            ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
            SuplierID TEXT,
            StockQuantity INTEGER,
            WholesalePrice DECIMAL(10,2),
            SellPrice DECIMAL(10,2),
            ProductName TEXT NOT NULL,
            FOREIGN KEY (SuplierID) REFERENCES Suplier(SuplierID)
        )
    ''')

    # Create Categorie table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categorie (
            CategorieID TEXT PRIMARY KEY,
            ProductID INTEGER,
            Description TEXT,
            Name TEXT NOT NULL,
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        )
    ''')

    # Create Expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Expenses (
            ExpensesID INTEGER PRIMARY KEY,
            PriceAmount DECIMAL(10,0),
            Quantity TEXT,
            ExpensesTypeID INTEGER
        )
    ''')

    # Create Purchase table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Purchase (
            PurchaseID INTEGER PRIMARY KEY AUTOINCREMENT,
            SuplierID TEXT,
            PurchaseDate DATE,
            TotalAmount DECIMAL(10,0),
            FOREIGN KEY (SuplierID) REFERENCES Suplier(SuplierID)
        )
    ''')

    # Create PurchaseDetail table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PurchaseDetail (
            PurchaseDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
            PurchaseID INTEGER,
            ProductID INTEGER,
            Quantity DECIMAL(10,0),
            UnitPrice TEXT,
            FOREIGN KEY (PurchaseID) REFERENCES Purchase(PurchaseID),
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        )
    ''')

    # Create Sale table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sale (
            SaleID INTEGER PRIMARY KEY AUTOINCREMENT,
            SaleDate DATE,
            TotalAmount DECIMAL(10,0)
        )
    ''')

    # Create SaleDetail table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SaleDetail (
            SaleDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
            SaleID INTEGER,
            ProductID INTEGER,
            Quantity DECIMAL(10,0),
            UnitPrice TEXT,
            FOREIGN KEY (SaleID) REFERENCES Sale(SaleID),
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        )
    ''')

    # Create Suplier table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Suplier (
            SuplierID TEXT PRIMARY KEY,
            ContactNumber INTEGER,
            Name TEXT,
            Location TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Run the function to create the database and tables
create_database()

print("Database and tables created successfully!")