import * as React from 'react'
import * as ReactDOM from 'react-dom'
import SongView from './internal/SongView'

class SpotifySong {
  constructor() {
    this.init()
  }

  init = () => {
    const elem = document.getElementById('SpotifySong')
    if (elem === undefined) return    

    const song = JSON.parse(document.getElementById('song_data').textContent);
    const comments = JSON.parse(document.getElementById('comments').textContent);

    const session = React.createElement(SongView, {
        song,
        comments
    })
  
    ReactDOM.render(session, elem)
  }
}

export default SpotifySong
