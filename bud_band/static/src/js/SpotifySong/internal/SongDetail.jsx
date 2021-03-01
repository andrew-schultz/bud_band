import * as React from 'react'

class SongDetail extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        const {
            song
        } = this.props

        return (
            <div className='detail'>
                <div className='container'>
                    <div className='column twelve empty'></div>

                    <div className='column two'></div>
                    <div className='column eight content-block shadow'>
                        <div className='attribute-div title'>
                            <p className='value'>{song.title} by {song.artist}</p>
                        </div>
                        <div className='attribute-div image '>
                            <img className='shadow' src={song.artwork} />
                        </div>
                        <div className='attribute-div reported-by' >
                            <p className='label'>Reported by:</p> <p className='value'>{song.owner.username}</p>
                        </div>
                        
                    </div>
                    <div className='column two'></div>

                    <div className='column twelve'></div>

                    <div className='column four'></div>
                    <div className='column four content-block shadow'>
                        <div className='attribute-div center'>
                            <p className='label'>From the Album </p> <p className='value'>{song.album}</p>
                        </div>
                    </div>
                    <div className='column four'></div>

                </div>


                {/* <div className='attribute-div'>
                    <p className='label'>Uri:</p> <p className='value'>{song.uri}</p>
                </div> */} 
                <div className='attribute-div link'>
                    <p className='label'>Link:</p> <p className='value link'><a href={song.link} _blank='true'>Open in Spotify</a></p>
                </div>

                <div className='attribute-div title'>
                    <p className='value'>{song.title} by {song.artist}</p>
                </div>
                <div className='attribute-div image'>
                    <img src={song.artwork} />
                </div>
                <div className='attribute-div reported-by' >
                    <p className='label'>Reported by:</p> <p className='value'>{song.owner.username}</p>
                </div>
            </div>
        )
    }
}

export default SongDetail