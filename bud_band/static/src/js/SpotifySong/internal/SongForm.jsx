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
            <div className='form song'>
                <input 
                type='text'
                name='uri'
                defaultValue={newSong.uri}
                onChange={this.props.uriChangeHandler}
                />
                <div className='submit' onClick={this.props.onSubmit}>Submit</div>
            </div>
        )
    }
}

export default SongForm