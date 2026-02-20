import requests

BASE_URL = 'http://localhost:5000'

# 1. Test the Welcome Route
print("Welcome Route Test")
response = requests.get(f'{BASE_URL}/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")
print()

# 2. Test the About Route
print("About Route Test")
response = requests.get(f'{BASE_URL}/about')
print(f"Status Code: {response.status_code}")
data = response.json()
print(f"Name: {data['name']}")
print(f"Course: {data['course']}")
print(f"Semester: {data['semester']}")
print()

# 3. Test the Greeting Route
print("Greeting Route Test")
name = "Elisheva"
response = requests.get(f'{BASE_URL}/greet/{name}')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")
if name in response.text:
    print(f"Response contains the name '{name}'")
else:
    print(f"Response does NOT contain the name '{name}'")
print()

# 4. Test the Calculator Route
print("Calculator Route Test")
# Test addition
response = requests.get(f'{BASE_URL}/calculate?num1=10&num2=5&operation=add')
print(f"Addition - Status Code: {response.status_code}")
print(f"Addition - Result: {response.json()}")

# Test multiply
response = requests.get(f'{BASE_URL}/calculate?num1=4&num2=3&operation=multiply')
print(f"Multiply - Status Code: {response.status_code}")
print(f"Multiply - Result: {response.json()}")
print()

# 5. Test the Echo Route (POST)
print("Echo Route Test (POST)")
payload = {"message": "Hello", "name": "Elisheva"}
response = requests.post(f'{BASE_URL}/echo', json=payload)
print(f"Status Code: {response.status_code}")
data = response.json()
print(f"Response: {data}")
if data.get('echoed') == True:
    print("Response includes 'echoed': true")
else:
    print("Response does NOT include 'echoed': true")
print()

# 6. Test Different Status Codes
print("Status Codes Test")
for code in [200, 404]:
    response = requests.get(f'{BASE_URL}/status/{code}')
    print(f"Requested: {code} - Status Code: {response.status_code} - Response: {response.text}")
print()

# 7. Test Custom Headers
print("Custom Headers Test")
response = requests.get(f'{BASE_URL}/')
custom_header = response.headers.get('X-Custom-Header')
print(f"Custom Header: {custom_header}")
if custom_header == 'FlaskRocks':
    print("X-Custom-Header is present and correct")
else:
    print("X-Custom-Header is missing or incorrect")
print()

# 8. Test Error Handling (Division by Zero)
print("Error Handling Test (Division by Zero)")
response = requests.get(f'{BASE_URL}/calculate?num1=10&num2=0&operation=divide')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
if response.status_code == 500:
    print("Server returned 500 for division by zero")
else:
    print("Unexpected status code for division by zero")