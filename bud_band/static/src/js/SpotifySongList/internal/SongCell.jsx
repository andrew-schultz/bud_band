import * as React from 'react'

class SongCell extends React.Component {
    openSongLink = () => {
        const {song} = this.props;
        const url = new URL(window.location)
        var newUrl = `${url.origin}/api/v1/spotify_song/${song.id}/edit/`
        window.location.href = newUrl;
    }

    render() {
        const {
            song,
        } = this.props

        if (!song.id) {
            return <div></div>
        }

        return (
            <div className='song-cell-container'>
                <div className='column twelve song-cell highlight-background shadow round-corners clickable' onClick={this.openSongLink}>
                    <div className='song-inner'>
                        <div className='song-inner-image'>
                            <img src={song.artwork} />
                        </div>
                        <div className='song-inner-text'>
                            <p className='song-inner-title'>{song.title}</p>
                            <p className='song-inner-artist'>{song.artist}</p>
                            <div>
                            <p className='song-inner-reporter'>reported by {song.owner.username}</p>

                            </div>
                        </div>

                        {/* <div className='byline'>
                            
                            <p className='timestamp'>{song_date ? song_date : ''}</p>
                        </div> */}
                    </div>
                </div>
                <div className='column twelve'></div>
            </div>
        )
    }
}

export default SongCell
