import * as React from 'react'

class SongForm extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        const {
            newSong,
            loading,
        } = this.props

        return (
            <div className='song-form-container'>
                <div className='song-form-inner-container'>
                    <div className='column three'></div>
                    <div className='column six'>
                        <div className='song-form-wrapper column content-block shadow'>
                            <div className='song-form-inner-wrapper'>
                                <div className='song-form-title'>
                                    <p className='top'>Listen to anything good lately?</p>
                                    <p className='bottom'>Enter a Spotify Song Link</p>
                                </div>
                                <div className='form song'>
                                    <input
                                        className='song-input'
                                        type='text'
                                        name='uri'
                                        onChange={this.props.handleSongChange}
                                        value={newSong.uri}
                                    />
                                </div>
                                <div>
                                    <div className='column nine'></div>
                                    <div className='column three'>
                                        { loading ?
                                            <div className='submit-button column content-block shadow rectangle-bubble'>
                                                <p className='loader'></p>
                                            </div> :
                                            <div className='submit-button column content-block shadow clickable rectangle-bubble' onClick={this.props.onSubmit}>
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
        )
    }
}

export default SongForm