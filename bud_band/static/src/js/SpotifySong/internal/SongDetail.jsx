import * as React from 'react'

class SongDetail extends React.Component {
    constructor(props) {
        super(props)
    }

    openSongLink = () => {
        const {song} = this.props
        window.open(song.link, '_blank');
    }

    render() {
        const {
            song
        } = this.props

        return (
            <div className='detail'>
                <div className='container'>
                    <div className='row'>
                        <div className='column twelve empty'></div>
                    </div>
                    
                    <div className='row'>
                        <div className='column one'></div>
                        <div className='column ten content-block shadow'>
                            <div className='attribute-div title'>
                                <p className='value'>{song.title} by {song.artist}</p>
                            </div>
                            <div className='attribute-div image '>
                                <img src={song.artwork} />
                            </div>
                            <div className='attribute-div center album'>
                                <p className='label'>From the Album </p> <p className='value'>{song.album}</p>
                            </div>
                            <div className='attribute-div reported-by' >
                                <p className='label'>Reported by:</p> <p className='value'>{song.owner.username}</p>
                            </div>
                        </div>
                        <div className='column one'></div>
                    </div>

                    <div className='row'>
                        <div className='column twelve'></div>
                    </div>
                    
                    <div className='row'>
                        <div className='column five'></div>
                        <div className='column two content-block shadow clickable rectangle-bubble' onClick={this.openSongLink}>
                            <div className='attribute-div link'>
                                <p className='value link'>Open in Spotify</p>
                            </div>
                        </div>
                        <div className='column five'></div>
                    </div>

                    <div className='row'>
                        <div className='column twelve'></div>
                    </div>
                </div>
            </div>
        )
    }
}

export default SongDetail