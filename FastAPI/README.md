# FastAPI Tea CRUD Application with MongoDB

A simple FastAPI application that provides CRUD operations for a tea collection using MongoDB Atlas.

## Features

- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ MongoDB Atlas integration with async/await
- ✅ Environment variable configuration for security
- ✅ Pydantic v2 data validation
- ✅ Auto-generated API documentation
- ✅ ObjectId validation and handling

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

**⚠️ IMPORTANT: This step is required before running the application!**

Create a `.env` file in the project root with your MongoDB connection details:

```env
# MongoDB Configuration (REQUIRED)
MONGODB_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/database_name?retryWrites=true&w=majority

# Database Configuration (Optional - defaults provided)
DATABASE_NAME=tea_database
COLLECTION_NAME=teas
```

**Security Notes:**
- The `MONGODB_URI` environment variable is **mandatory**
- Never commit your `.env` file to version control
- Use `.env.example` as a template for team members
- Replace `username`, `password`, and cluster details with your actual MongoDB Atlas credentials

### 3. MongoDB Atlas Setup

1. Create a MongoDB Atlas account at [https://www.mongodb.com/atlas](https://www.mongodb.com/atlas)
2. Create a new cluster
3. Create a database user with read/write permissions
4. Get your connection string and add it to the `.env` file
5. Make sure to replace `<password>` with your actual password in the connection string

### 4. Run the Application

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`

## API Documentation

Visit `http://127.0.0.1:8000/docs` for interactive API documentation (Swagger UI).

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/teas` | Get all teas |
| POST | `/teas` | Create a new tea |
| GET | `/teas/{tea_id}` | Get a specific tea by ID |
| PUT | `/teas/{tea_id}` | Update a tea |
| DELETE | `/teas/{tea_id}` | Delete a tea |
| POST | `/init-data` | Initialize sample data |

## Data Model

### Tea
```json
{
  "id": "string (MongoDB ObjectId)",
  "name": "string",
  "origin": "string"
}
```

### Create Tea
```json
{
  "name": "string",
  "origin": "string"
}
```

### Update Tea
```json
{
  "name": "string (optional)",
  "origin": "string (optional)"
}
```

## Usage Examples

### Create a new tea
```bash
curl -X POST "http://127.0.0.1:8000/teas" \
     -H "Content-Type: application/json" \
     -d '{"name": "Chamomile", "origin": "Egypt"}'
```

### Get all teas
```bash
curl -X GET "http://127.0.0.1:8000/teas"
```

### Get a specific tea
```bash
curl -X GET "http://127.0.0.1:8000/teas/{tea_id}"
```

### Update a tea
```bash
curl -X PUT "http://127.0.0.1:8000/teas/{tea_id}" \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Tea Name"}'
```

### Delete a tea
```bash
curl -X DELETE "http://127.0.0.1:8000/teas/{tea_id}"
```

## Project Structure

```
FastAPI/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in version control)
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Security Notes

- Always use environment variables for sensitive configuration
- Never commit `.env` files to version control
- Use strong passwords for your MongoDB Atlas cluster
- Consider using IP whitelisting in MongoDB Atlas for additional security

## Development

To run in development mode with auto-reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Dependencies

- **fastapi**: Modern web framework for APIs
- **motor**: Async MongoDB driver
- **pymongo**: MongoDB driver (motor dependency)
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation and settings management
- **uvicorn**: ASGI server

## License

This project is open source and available under the [MIT License](LICENSE).
