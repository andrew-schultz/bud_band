import * as React from 'react'
import * as ReactDOM from 'react-dom'
import * as utils from '../../utils.jsx'
import api from '../../api'
import SongCell from './SongCell'
import SSHeader from '../../Header.jsx'


class ListView extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            songs: [],
        }

        this.csrftoken = null;
    }

    componentDidMount() {
        this.csrftoken = utils.getCookie('csrftoken');
        this.headers = {
            'HTTP-X-CSRFToken': this.csrftoken,
            'X-CSRFToken': this.csrftoken
        }

        this.setState({songs: this.props.songs})
    }

    render() {
        const {
            songs
        } = this.props

        return (
            <div>
                <SSHeader></SSHeader>
                <div className='column twelve top-gap'></div>
                <div>
                    {songs.map((song, i) => (<SongCell key={i} song={song} />))}
                </div>
            </div>
        )
    }
}
    
export default ListView
