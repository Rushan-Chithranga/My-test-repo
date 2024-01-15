import csv

def read_customer_info(csv_file_name):
	customer_info = []
	with open(csv_file_name, 'r') as file:
		csvreader = csv.reader(file)
		next(csvreader)
		for row in csvreader:
			customer_info.append(row)
	return customer_info

def read_crm_users(csv_file_name):
	crm_users_dict = {}
	with open(csv_file_name, 'r') as file:
		csvreader = csv.reader(file)
		next(csvreader)
		for row in csvreader:
			crm_users_dict[row[2].strip()] = row[3]
	return crm_users_dict	

def transform_customer_info(customer_info, crm_users_dict):
	new_table = []
	new_table_headers = ["first_name","last_name","email_address", "mobile_no", "address" ,"contact_owner_id"]
	new_table.append(new_table_headers)

	for row in customer_info:
		first_name = row[0].split()[0]
		last_name = row[0].split(' ', 1)[-1]
		email_address = ''
		mobile_no = row[1]
		address = ', '.join(row[2:6])
		contact_owner_id = crm_users_dict[row[6].strip()]
		new_table.append([first_name, last_name, email_address, mobile_no, address, contact_owner_id])
	return new_table

def write_to_csv(new_table):
	with open('customer_data.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(new_table)
	print("CSV file created successfully!")

customer_info = read_customer_info("Customer_Info_CSV.csv")
crm_users_dict = read_crm_users("CRM_USERS_CSV.csv")
new_table = transform_customer_info(customer_info, crm_users_dict)
write_to_csv(new_table)