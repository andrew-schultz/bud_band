import * as React from 'react'
import * as ReactDOM from 'react-dom'
import PlaylistsView from './internal/PlaylistsView'

class PlaylistList {
  constructor() {
    this.init()
  }

  init = () => {
    const elem = document.getElementById('PlaylistList')
    if (elem === undefined) return    

    const playlists = JSON.parse(document.getElementById('playlists_data').textContent);

    const session = React.createElement(PlaylistsView, {
        playlists
    })
  
    ReactDOM.render(session, elem)
  }
}

export default PlaylistList
