import * as React from 'react'
import * as ReactDOM from 'react-dom'
import PlaylistForm from './internal/PlaylistForm'

class Playlist {
  constructor() {
    this.init()
  }

  init = () => {
    const elem = document.getElementById('Playlist')
    if (elem === undefined) return    

    const session = React.createElement(PlaylistForm, {})
  
    ReactDOM.render(session, elem)
  }
}

export default Playlist
