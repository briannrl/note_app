from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from database import db

app = FastAPI()

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def get_routes():
    return ["/notes", "/notes/<pk>"]

@app.get("/notes")
def get_notes():
    # notes = db.search_by_value(schema="notesapp", table="notes", search_attribute="id", search_value="*", get_attributes=["*"])
    notes = db.sql("SELECT * FROM notesapp.notes ORDER BY __updatedtime__ DESC") # SAME FUNCTION AS ABOVE CODE
    return notes

@app.get("/notes/{pk}")
def get_note(pk:str):
    notes = db.search_by_hash('notesapp', 'notes', [pk])
    return notes[0]

@app.post("/notes")
def add_note(data=Body()): # Body() IS USED AS A CONTAINER FOR NEW DATA
    db.insert(schema="notesapp", table="notes", records=[{"description":data["description"]}]) # ADD NEW DATA WITH NEW COLUMN "description"
    # {"description":"First database entry"} ENTRY EXAMPLE
    # THIS IS THE WAY TO FORMAT THE NEW ENTRY. {"name_of_column":"data_to_be_inserted"}
    notes = db.sql("SELECT * FROM notesapp.notes ORDER BY __updatedtime__ DESC")
    return notes

@app.put("/notes/{pk}")
def update_notes(pk:str, data=Body()):
    db.update(schema="notesapp", table="notes", records=[{"id":pk, "description":data["description"]}])
    notes = db.sql("SELECT * FROM notesapp.notes ORDER BY __updatedtime__ DESC")
    return notes

@app.delete("/notes/{pk}")
def delete_note(pk:str):
    db.delete("notesapp", "notes", [pk])
    notes = db.sql("SELECT * FROM notesapp.notes ORDER BY __updatedtime__ DESC")
    return notes