import * as React from 'react'

class PlaylistCell extends React.Component {
    openPlaylistLink = () => {
        const {playlist} = this.props;
        const url = new URL(window.location)
        var newUrl = `${url.origin}/api/v1/spotify_song/list/?limit=100&offset=0&playlist_id=${playlist.id}`
        window.location.href = newUrl;
    }

    render() {
        const {
            playlist,
        } = this.props

        if (!playlist.id) {
            return <div></div>
        }

        return (
            <div className='song-cell-container'>
                <div className='column twelve song-cell highlight-background shadow round-corners clickable' onClick={this.openPlaylistLink}>
                    <div className='song-inner'>
                        <div className='song-inner-image'>
                            {playlist.artwork ? <img src={playlist.artwork} /> : ''}
                        </div> 
                        {/* <div className='column twelve ios-padding'></div>} */}
                        
                        <div className='song-inner-text-wrapper'>
                            <div className='song-inner-text'>
                                <p className='song-inner-title'>{playlist.name}</p>
                                <p className='song-inner-description'>{playlist.description}</p>
                                <div className='ios-gap'></div>
                                <p className='song-inner-reporter'>reported by {playlist.user.username}</p>
                            </div>
                        </div>

                        {/* <div className='byline'>
                            
                            <p className='timestamp'>{song_date ? song_date : ''}</p>
                        </div> */}
                    </div>
                </div>
                <div className='column twelve ios-gap'></div>
            </div>
        )
    }
}

export default PlaylistCell
