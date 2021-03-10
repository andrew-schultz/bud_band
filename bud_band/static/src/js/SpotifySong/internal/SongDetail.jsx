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
                    <div className='column one'></div>
                    <div className='column ten'>
                        <div className='column content-block shadow content-main'>
                            <div className='attribute-div image '>
                                <img className='shadow' src={song.artwork} />
                            </div>
                            <div className='attribute-div title'>
                                <p className='value-title'>{song.title} </p> <br />
                                <p className='value-artist'>{song.artist}</p>
                            </div>
                            <div className='attribute-div album'>
                                <p><span className='label'>From the Album</span><br/>{song.album}</p>
                            </div>
                            <div className='attribute-div reported-by' >
                                <p className='label'>Reported by:</p> <p className='value'>{song.owner.username}</p>
                                <div className='ios-gap'></div>
                            </div>
                        </div>
                    </div>
                    <div className='column one'></div>

                    <div className='column twelve small-ios-gap'></div>
                    
                    <div className='row'>
                        <div className='column four'></div>
                        <div className='column four'>
                            <div className='column content-block shadow clickable rectangle-bubble content-main top-gap' onClick={this.openSongLink}>
                                <div className='attribute-div link'>
                                    <p className='value link'>Open in Spotify</p>
                                </div>
                            </div> 
                        </div>
                        <div className='column four'></div>
                    </div>

                    <div className='column twelve'></div>
                </div>
            </div>
        )
    }
}

export default SongDetail