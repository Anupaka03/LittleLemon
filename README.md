## Endpoints to test either via Insomnia Client, Postman, Browsable API interface in browser or any other testing tool

### Base url (localhost)

http://127.0.0.1:8000/

### Home page (static content)

restaurant

### Menu related

restaurant/menu

restaurant/menu/\<int:pk>

### Booking related

restaurant/booking/tables 

restaurant/booking/tables\<int:pk>

### Authentication and djoser related

restaurant/api-token-auth

auth/users

auth/token/login

auth/token/logout