# FastAPI MVC Project

This project demonstrates a FastAPI application structured using the MVC (Model-View-Controller) pattern. The application includes an endpoint to perform addition on input lists of integers using Python's multiprocessing pool, with appropriate error handling and logging.

## Project Structure

fastapi_mvc_project/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models/
│ │ ├── init.py
│ │ └── item.py
│ ├── views/
│ │ ├── init.py
│ │ └── addition.py
│ ├── controllers/
│ │ ├── init.py
│ │ └── addition_controller.py
│ └── utils/
│ ├── init.py
│ └── addition_worker.py
├── tests/
│ ├── init.py
│ ├── test_addition.py
│ └── test_main.py
├── requirements.txt
└── README.md



## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/venkatesh1229/EY_Assignment.git
    cd fastapi_mvc_project
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server**:
    ```sh
    uvicorn app.main:app --reload
    ```

2. **API Endpoint**:
    - **URL**: `/api/v1/add`
    - **Method**: `POST`
    - **Request Body**:
      ```json
      {
        "batched": "id0101",
        "payload": [[1, 2], [3, 4]]
      }
      ```
    - **Response**:
      ```json
      {
        "batched": "id0101",
        "response": [3, 7],
        "status": "complete",
        "started_at": "2024-06-18T12:00:00Z",
        "completed_at": "2024-06-18T12:00:01Z"
      }
      ```

## Project Components

### Models

#### app/models/item.py
- **Item**: Defines the request structure with `batched` and `payload`.
- **Result**: Defines the response structure with `batched`, `response`, `status`, `started_at`, and `completed_at`.

### Views

#### app/views/addition.py
- **addition**: Handles POST requests to `/add`, processes the input using the controller, and returns a response.

### Controllers

#### app/controllers/addition_controller.py
- **add_numbers**: Handles the business logic by calling the utility function.

### Utils

#### app/utils/addition_worker.py
- **add_numbers_worker**: Adds the numbers in a single list.
- **add_numbers**: Uses a multiprocessing pool to handle the addition operation concurrently.

### Unit Tests

#### tests/test_addition.py
- Tests for different scenarios and edge cases:
  - **test_addition**: Validates correct addition and response structure.
  - **test_addition_empty**: Ensures correct handling of an empty payload.
  - **test_addition_invalid_input**: Ensures proper error handling for invalid input.

#### tests/test_main.py
- **test_read_main**: Tests the root endpoint to ensure it returns a 404 status.

## Running Tests

1. **Run the tests**:
    ```sh
    pytest tests
    ```

## Logging and Error Handling

- **Logging**: Configured in `app/utils/addition_worker.py` using Python's logging module.
- **Error Handling**: Exceptions are caught and handled appropriately in the views, with detailed error messages returned to the client.

