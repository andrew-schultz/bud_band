import * as React from 'react'

class SongForm extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        const {
            newSong
        } = this.props

        return (
            <div className='song-form-container'>
                <div className='column twelve'></div>

                <div className='column three'></div>
                <div className='column six'>
                    <div className='song-form-title'>
                        <p className='top'>Listen to anything good lately?</p>
                        <p className='bottom'>Enter a Spotify Song URI</p>
                    </div>
                </div>
                <div className='column three'></div>

                <div className='column three'></div>
                <div className='column six'>
                    <div className='form song'>
                        <input
                            className='song-input'
                            type='text'
                            name='uri'
                            onChange={this.props.handleSongChange}
                            value={newSong.uri}
                        />

                        <div>
                            <div className='column nine'></div>
                            <div className='column three'>
                                <div className='submit-button column content-block shadow clickable rectangle-bubble' onClick={this.props.onSubmit}>Submit</div>
                            </div>
                        </div>
                    
                            {/* <div className='submit' onClick={this.props.onSubmit}>Submit</div> */}
                    </div>
                </div>
                <div className='column three'></div>

                <div className='column twelve'></div>
    
            </div>
        )
    }
}

export default SongForm