
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/movie-management-system.git
   cd movie-management-system
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
   uvicorn app.main:app --reload
   uvicorn app.main:app --reload --log-level debug
   ```

### API Documentation
Access the FastAPI Swagger UI:
```
http://localhost:8000/docs
```

#### SQL Commands
```sql
-- Creating New DB
    CREATE DATABASE ecommate;

-- Creating USER
   CREATE USER dataworkx WITH PASSWORD 'jnjnuh';
   ALTER  USER dataworkx  WITH PASSWORD 'jnjnuh';

-- Granting previleges to use on NEW DB
	GRANT ALL PRIVILEGES ON DATABASE ecommate to dataworkx;

-- Make the user as Super User
	ALTER USER dataworkx WITH SUPERUSER;

-- login to database
   psql -h 127.0.0.1 -U dataworkx ecommate

-- Print user details
SELECT
    "users".id,
    "users".user_first_name,
    "users".user_last_name,
    "users".user_login_id,
    "users".user_password,
    roles.role_name,
    roles.id
FROM
    "users"
LEFT JOIN
    user_roles ON "users".id = user_roles.user_id
LEFT JOIN
    roles ON user_roles.role_id = roles.id;

SELECT
    "users".id,
    "users".user_login_id,
    "users".user_password,
    roles.role_name,
    roles.id as role_id
FROM
    "users"
LEFT JOIN
    user_roles ON "users".id = user_roles.user_id
LEFT JOIN
    roles ON user_roles.role_id = roles.id;

-- Update user's pass with common password 'first char in email + jnjnuh'
UPDATE users
SET user_password = LOWER(LEFT(user_login_id, 1)) || 'jnjnuh'
WHERE id > 0;
```