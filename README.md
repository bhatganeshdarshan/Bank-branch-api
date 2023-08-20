# Bank Branch API
A simple flask based api to access all the bank, bank address, ifsc code of specified bank branch

### Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite (for the database)

Required python package :
```bash
pip install Flask Flask-SQLAlchemy
```
### Running the API
1.Clone the repo
```bash
git clone https://github.com/yourusername/bank-branch-api.git
cd bank-branch-api
```

### Setting Database
```bash
python
```
```python
from app import db
db.create_all()
exit()
```
### Start the server by 
```python
app.py
```
API will be available at http://localhost:5000/

### Endpoints
- '/' Home page
- '/all' Get all bank branches
- '/search?loc=city_name' Search bank branches by location


