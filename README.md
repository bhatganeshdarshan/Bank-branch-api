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
git clone https://github.com/bhatganeshdarshan/bank-branch-api.git
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
  ![Screenshot from 2023-08-20 18-10-27](https://github.com/bhatganeshdarshan/Bank-branch-api/assets/88202395/efe76fb5-5b42-47f1-8128-f0ca8f004441)

- '/all' Get all bank branches
  ![Screenshot from 2023-08-20 18-13-09](https://github.com/bhatganeshdarshan/Bank-branch-api/assets/88202395/907ac7db-1385-4682-912d-1179a133f4d8)
  
- '/search?loc=city_name' Search bank branches by location
  ![Screenshot from 2023-08-20 18-11-18](https://github.com/bhatganeshdarshan/Bank-branch-api/assets/88202395/06eb6f3e-5b21-4dc7-a133-c78af76424ee)
