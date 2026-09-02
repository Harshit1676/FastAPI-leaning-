from fastapi import FastAPI, Depends

app = FastAPI()


# dependecy function
def get_db():
    db = {'connection' : 'mock_database_connection'}
    try:
        yield db
    finally:
        db.close()
        



# endpoints 
@app.get('/home')
def  home(db=Depends(get_db)):
    return {'db_status' : db['connection']}