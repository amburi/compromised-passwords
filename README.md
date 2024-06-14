# Compromised Password Checker

This project is a simple web service that checks if a given password is compromised. The service is built using Python and `http.server` and can be easily containerized using Docker.

## Business Requirement

In today's digital age, security is paramount. Users often choose weak or compromised passwords, which can lead to data breaches and unauthorized access. This project aims to provide a simple API service that businesses can integrate into their systems to check if a password is compromised. This service helps enhance security measures by preventing the use of known compromised passwords, thereby reducing the risk of data breaches and ensuring better protection of user accounts.

## Functional Requirements

1. **Password Checking Endpoint:**
   - The service should provide an endpoint to check if a password is compromised.
   - The endpoint should accept a POST request with a JSON body containing the password.

2. **Responses:**
   - **200 OK:** If the password is compromised, return a message indicating so.
   - **204 No Content:** If the password is not compromised, return no content.
   - **400 Bad Request:** If the password is not provided or the request body is invalid, return an appropriate error message.
   - **404 Not Found:** If an invalid endpoint is accessed, return an error message.
   - **405 Method Not Allowed:** If a method other than POST is used, return an error message.

3. **Error Handling:**
   - The service should handle invalid JSON in the request body and return a proper error message.
   - The service should handle cases where no password is provided in the request body.

4. **Security:**
   - The service should not log or store the passwords being checked.
   - Ensure that the service is only accessible over secure channels (e.g., HTTPS in a production environment).

## Requirements

- Python 3.9+
- Docker (optional, for containerization)

## Installation

### Using Python

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/compromised-password-checker.git
    cd compromised-password-checker
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```sh
    python app.py
    ```

The server will start on port 8080 by default.

### Using Docker

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/compromised-password-checker.git
    cd compromised-password-checker
    ```

2. **Build the Docker image:**
    ```sh
    docker build -t compromised-password-checker .
    ```

3. **Run the Docker container:**
    ```sh
    docker run -p 8080:8080 compromised-password-checker
    ```

The server will be available on port 8080.

Docker image: https://hub.docker.com/repository/docker/amburi/compromised-passwords

## Usage

### Endpoint

- **POST** `/compromised`

### Request Body

- `password` (string): The password to check.

### Example Request

```sh
curl -X POST http://localhost:8080/compromised -H "Content-Type: application/json" -d '{"password": "password123"}'
```

### Responses

- **200 OK**: Password is compromised.
    ```json
    {
      "message": "Password is compromised!"
    }
    ```

- **204 No Content**: Password is not compromised.

- **400 Bad Request**: Password not provided or invalid JSON.
    ```json
    {
      "message": "Password not provided!"
    }
    ```

- **404 Not Found**: Invalid endpoint.
    ```json
    {
      "message": "Not found!"
    }
    ```

- **405 Method Not Allowed**: Method other than POST used.
    ```json
    {
      "message": "Method Not Allowed"
    }
    ```

## Development

### Adding More Compromised Passwords

To add more compromised passwords, update the `COMPROMISED_PASSWORDS` set in `app.py`.

```python
COMPROMISED_PASSWORDS = {'password123', '123456', 'qwerty', 'letmein'}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Amburi Roy](https://www.linkedin.com/in/amburi/).
