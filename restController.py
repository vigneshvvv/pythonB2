from fastapi import FastAPI, HTTPException
from db_connection import db_connection_operation
import uvicorn
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    book_name: str
    author: str
    price: int
app = FastAPI()

@app.get("/getBooks")
def get_book_details():
    conn = db_connection_operation()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("select * from books")
        result = cursor.fetchall()
        print(result)
        return result
    finally:
        cursor.close()
        conn.close()

@app.post("/insertBookDetails")
def insert_book_details(book: Book):
    connection  = db_connection_operation()
    cursor  = connection.cursor(dictionary=True)

    try:
        query = "INSERT INTO books (id, book_name, author, price) values (%s,%s,%s,%s)"
        values = (book.id, book.book_name, book.author, book.price)
        cursor.execute(query, values)
        connection.commit()
        new_data = cursor.lastrowid
        return {
            "message": "Book data created",
            "id": new_data,
            "data": book.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()




if __name__ == "__main__":
    uvicorn.run("restController:app", host="127.0.0.1", port=8081, reload=True)


