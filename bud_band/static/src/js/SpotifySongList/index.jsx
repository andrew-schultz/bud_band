import * as React from 'react'
import * as ReactDOM from 'react-dom'
import ListView from './internal/ListView'

class SpotifySongList {
  constructor() {
    this.init()
  }

  init = () => {
    const elem = document.getElementById('SpotifySongList')
    if (elem === undefined) return    

    const songs = JSON.parse(document.getElementById('songs_data').textContent);
    const next_query = JSON.parse(document.getElementById('next_query').textContent);
    const previous_query = JSON.parse(document.getElementById('previous_query').textContent);
    const count = JSON.parse(document.getElementById('count').textContent);
    const playlist_id = JSON.parse(document.getElementById('playlist_id').textContent);

    const session = React.createElement(ListView, {
        songs,
        playlist_id,
        next_query,
        previous_query,
        count
    })
  
    ReactDOM.render(session, elem)
  }
}

export default SpotifySongList
