import * as React from 'react'
import * as ReactDOM from 'react-dom'
import * as utils from '../../utils.jsx'
import api from '../../api'
import SSHeader from '../../Header.jsx'
import PlaylistCell from './PlaylistCell.jsx'


class PlaylistsView extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            playlists: [],
            limit: 100,
            offset: 100,
            more: true,
            loading: true,
        }

        this.csrftoken = null;
    }

    componentDidMount() {
        this.csrftoken = utils.getCookie('csrftoken');
        this.headers = {
            'HTTP-X-CSRFToken': this.csrftoken,
            'X-CSRFToken': this.csrftoken
        }

        this.setState({playlists: this.props.playlists, loading: false})
        
        document.addEventListener('scroll', this.handleScroll)
    }
    

    handleScroll = async (e) => {
        const {limit, offset, more, playlists, loading} = this.state

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
                    offset: offset
                }
                await api.playlist.fetch(params, this.headers).then(response => {
                    var existingPlaylists = response.data.playlists_data;
                    var isThereMore = false

                    if (response.data.next_query) {
                        isThereMore = true
                    }

                    playlists.push(existingPlaylists);
                    var newPlaylists = playlists.flat()

                    this.setState({
                        playlists: newPlaylists,
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
            playlists
        } = this.state

        if (!playlists) {
            return <div></div>
        }

        return (
            <div>
                <SSHeader addType='playlist'></SSHeader>
                <div className='column twelve top-gap'></div>
                <div>
                    {playlists.map((playlist, i) => (<PlaylistCell key={i} playlist={playlist} />))}
                </div>
                <div className='column twelve bottom-gap-ios'></div>
            </div>
        )
    }
}
    
export default PlaylistsView
