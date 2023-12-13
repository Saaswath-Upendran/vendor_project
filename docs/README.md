# This is a Assignment of FatMug for Django Developer 
Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

As Per the PDF shared I have done all my API Endpoints and the calculation for Historical Performance in this code


Here is the list of API endpoints 

● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor.

● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
metrics.


For initializing and running this code in the computer 

1. Create a vitural environement using venv or using conda 
2. Install the requirements file given using this command pip install -r requiements.txt
3. After installing run the server using python manage.py runserver
4. Now you can use postman or any other tool/browser to test the api calls
5. Create a user using python manage.py createsuperuser