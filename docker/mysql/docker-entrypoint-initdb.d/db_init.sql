CREATE TABLE IF NOT EXISTS Customers(
	id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL,
)

CREATE TABLE IF NOT EXISTS Vehicles(
	id INT AUTO_INCREMENT PRIMARY KEY,
	category_id INT NOT NULL,
	in_use BOOLEAN NOT NULL,
	CONSTRAINT FK_Vehicles_CATEGORY
	FOREIGN KEY (category_id)
		REFERENCES VehicleCategories(id)
		ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS Bookings(
	id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id int NOT NULL,
	vehicle_id int NOT NULL,
	hire_date TIMESTAMP NOT NULL,
	return_date TIMESTAMP NOT NULL,
	status TINYINT(1) NOT NULL,
	created_at TIMESTAMP NOT NULL,
	CONSTRAINT FK_Bookings_Customer
	FOREIGN KEY (customer_id)
		REFERENCES Customers(id),
		ON DELETE CASCADE
	CONSTRAINT FK_Bookings_Vehicle
	FOREIGN KEY (vehicle_id)
		REFERENCES Vehicles(id)
		ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS VehicleCategories(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	capacity INT NOT NULL,
)

INSERT INTO VehicleCategories (name, capacity) VALUES(
	("small", 4),
	("family", 7),
	("van", 12)
)
