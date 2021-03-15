import * as React from 'react'
import * as ReactDOM from 'react-dom'
import * as utils from '../../utils.jsx'
import api from '../../api'
import SSHeader from '../../Header.jsx'

class PlaylistForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            playlist: {
                name: '',
                description: '',
                loading: false
            }
        }
    }

    componentDidMount() {
        this.csrftoken = utils.getCookie('csrftoken');
        this.headers = {
            'HTTP-X-CSRFToken': this.csrftoken,
            'X-CSRFToken': this.csrftoken
        }
    }

    handlePlaylistChange = (event) => {
        var {playlist} = this.state;
        playlist[event.target.name] = event.target.value
        this.setState({playlist: playlist})
    }

    onSubmit = async () => {
        const {playlist} = this.state
        this.setState({loading: true})
        var request_data = {
            name: playlist.name,
            description: playlist.description
        }
        const {data} = await api.playlist.create(request_data, this.headers)

        if (data && data.id) {
            const url = new URL(window.location)
            var newUrl = `${url.origin}/api/v1/spotify_song/list/?limit=100&offset=0&playlist_id=${data.id}`
            // window.history.pushState({}, '', newUrl)
            window.location.href = newUrl;
        } else {
            // there was an error oooops
            this.setState({loading: false})
        }
    }
    

    render() {
        const {
            playlist,
            loading,
        } = this.state

        return (
            <div>
                <SSHeader addType='playlist'></SSHeader>
                <div className='column twelve top-gap'></div>
                <div className='song-form-container'>
                    <div className='song-form-inner-container playlist'>
                        <div className='column three'></div>
                        <div className='column six'>
                            <div className='song-form-wrapper column content-block shadow'>
                                <div className='song-form-inner-wrapper'>
                                    <div className='song-form-title'>
                                        <p className='top'>Create a new Playlist</p>
                                        <p className='bottom'>What's it called?</p>
                                    </div>
                                    <div className='form song'>
                                        <input
                                            className='song-input'
                                            type='text'
                                            name='name'
                                            onChange={this.handlePlaylistChange}
                                            value={playlist.name}
                                        />
                                    </div>
                                </div>
                                <div className='song-form-inner-wrapper'>
                                    <div className='song-form-title'>
                                        <p className='bottom'>Anything you'd like to say about it?</p>
                                    </div>
                                    <div className='form song'>
                                        <textarea
                                            className='song-input big'
                                            type='text'
                                            name='description'
                                            plaaceholder='description'
                                            onChange={this.handlePlaylistChange}
                                            value={playlist.description}
                                        />
                                    </div>
                                    <div>
                                        <div className='column nine'></div>
                                        <div className='column three'>
                                            { loading ?
                                                <div className='submit-button column content-block shadow rectangle-bubble'>
                                                    <p className='loader'></p>
                                                </div> :
                                                <div className='submit-button column content-block shadow clickable rectangle-bubble' onClick={this.onSubmit}>
                                                    <p>Submit</p> 
                                                </div>
                                            }
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className='column three'></div>
                    </div>
                </div>
            </div>
            
        )
    }
}

export default PlaylistForm