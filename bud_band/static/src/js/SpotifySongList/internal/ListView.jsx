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
            limit: 100,
            offset: 100,
            more: true,
            loading: true,
            playlistId: this.props.playlist_id
        }

        this.csrftoken = null;
    }

    componentDidMount() {
        this.csrftoken = utils.getCookie('csrftoken');
        this.headers = {
            'HTTP-X-CSRFToken': this.csrftoken,
            'X-CSRFToken': this.csrftoken
        }

        this.setState({songs: this.props.songs, loading: false})
        
        document.addEventListener('scroll', this.handleScroll)
    }
    
    handleScroll = async (e) => {
        const {limit, offset, more, songs, loading, playlistId} = this.state

        if (!loading && more) {
            while(true) {
                // document bottom
                let windowRelativeBottom = document.documentElement.getBoundingClientRect().bottom;
            
                // if the user hasn't scrolled far enough (>100px to the end)
                if (windowRelativeBottom > document.documentElement.clientHeight + 100) break;
                this.setState({loading: true})

                // let's add more data
                const params = {
                    limit: limit,
                    offset: offset,
                    playlist_id: playlistId,
                }
                await api.spotifySong.fetch(params, this.headers).then(response => {
                    var existingSongs = response.data.songs_data;
                    var isThereMore = false

                    if (response.data.next_query) {
                        isThereMore = true
                    }

                    songs.push(existingSongs);
                    var newSongs = songs.flat()
                    
                    this.setState({
                        songs: newSongs,
                        offset: offset + limit,
                        loading: false,
                        more: isThereMore
                    })
                }).catch(error => {
                    console.log(`OPE! ${error}`)
                })
            }
        }
    }

    render() {
        const {
            songs,
        } = this.state

        if (!songs) {
            return <div></div>
        }

        return (
            <div>
                <SSHeader addType='spotify_song' playlistId={this.props.playlist_id}></SSHeader>
                <div className='column twelve top-gap'></div>
                <div>
                    {
                        songs.length ?
                        songs.map((song, i) => (<SongCell key={i} song={song} />)) :
                        <div className='column twelve'>
                            <div className='column inverse-shadow round-corners placeholder-text'>No Songs</div>
                        </div>
                    }
                </div>
                <div className='column twelve bottom-gap-ios'></div>
            </div>
        )
    }
}
    
export default ListView
