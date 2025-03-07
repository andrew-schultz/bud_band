require('../css/scss/main.scss')

import React from 'react'
import { render } from 'react-dom'

import SpotifySong from './SpotifySong'
import SpotifySongList from './SpotifySongList'
import AccountLogin from './Account'
import PlaylistList from './PlaylistList'
import Playlist from './Playlist'

const page_apps = {
  SpotifySong,
  SpotifySongList,
  AccountLogin,
  Playlist,
  PlaylistList,
};

function renderAppInElement(el) {
  var App = page_apps[el.id]

  if (!App) return
  var x = new App(el.dataset)
}

let apps = document.querySelectorAll('.__react-root').forEach(function(e) {
  renderAppInElement(e)
})
