import React, {useState, useEffect} from 'react'
import List_Item from '../components/List_Item'
import { Link } from 'react-router-dom'
import { ReactComponent as AddIcon } from '../assets/add.svg'

// let dummyData = [{"id":"1", "description":"Get milk"}, {"id":"2", "description":"Wash car"}, {"id":"3", "description":"Get bread"}, {"id":"4", "description":"Go to school"}]

const Notes = () => {
  let [notes, setNotes] = useState([])

  useEffect(() => {
    getNotes()
  }, [])

  let getNotes = async () => {
    let response = await fetch("/notes")
    let data = await response.json()
    setNotes(data)
  }

  return (
    <div className='notes'>
      <div className="notes-header">
        <h2 className="notes-title">&#9782; Notes</h2>
        <p className="notes-count">{notes.length}</p>
      </div>

      {/* <Link to={'/add'}>Add</Link> */}
      <div className='notes-list'>
        {notes.map((note) => (
          <List_Item key={note.id} note={note} />
        ))}
      </div>

      <Link to="/add" className='floating-button'>
        <AddIcon />
      </Link>
    </div>
  )
}

export default Notes