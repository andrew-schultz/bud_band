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
                    <div className='column twelve empty'></div>
                    
                    <div className='row'>
                        <div className='column one'></div>
                        <div className='column ten'>
                            <div className='column content-block shadow content-main'>
                                <div className='attribute-div title'>
                                    <p className='value'>{song.title}<br /><span className='by'>by</span><br />{song.artist}</p>
                                </div>
                                <div className='attribute-div image '>
                                    <img src={song.artwork} />
                                </div>
                                <div className='attribute-div center album'>
                                    <p> <span className='label'>From the Album</span> {song.album}</p>
                                </div>
                                <div className='attribute-div reported-by' >
                                    <p className='label'>Reported by:</p> <p className='value'>{song.owner.username}</p>
                                </div>
                            </div>
                        </div>
                        <div className='column one'></div>
                    </div>

                    <div className='column twelve'></div>
                    
                    <div className='row'>
                        <div className='column five'></div>
                        <div className='column two'>
                            <div className='column content-block shadow clickable rectangle-bubble content-main' onClick={this.openSongLink}>
                                <div className='attribute-div link'>
                                    <p className='value link'>Open in Spotify</p>
                                </div>
                            </div> 
                        </div>
                        <div className='column five'></div>
                    </div>

                    <div className='column twelve'></div>
                </div>
            </div>
        )
    }
}

export default SongDetail