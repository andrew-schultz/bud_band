import * as React from 'react'
import * as ReactDOM from 'react-dom'
import * as utils from '../../utils.jsx'
import api from '../../api'
import CommentsBlock from '../../Comments/CommentsBlock'
import SongForm from './SongForm'
import SongDetail from './SongDetail'
import SSHeader from '../../Header.jsx'


class SongView extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            id: this.props.song.id ? this.props.song.id : null,
            song: this.props.song ? this.props.song : {},
            comments: [],
            modalOpen: false,
            newSong: {
                uri: '',
                playlist_id: this.props.playlist_id,
            },
            newComment: {
                song_id: this.props.song.id,
                text: '',
            },
            playlistId: this.props.playlist_id,
            loading: false
        }

        this.csrftoken = null;
    }

    componentDidMount() {
        this.csrftoken = utils.getCookie('csrftoken');
        this.headers = {
            'HTTP-X-CSRFToken': this.csrftoken,
            'X-CSRFToken': this.csrftoken
        }

        this.setState({comments: this.props.comments})
    }

    handleCommentChange = (event) => {
        var comment = this.state.newComment
        comment[event.target.name] = event.target.value
        this.setState({newComment: comment})
    }

    handleCommentSubmit = async () => {
        const {newComment, song, comments} = this.state
        var request_data = {
            text: newComment.text,
            spotify_song_id: song.id,
        }
        const {data} = await api.comment.create(request_data, this.headers)

        comments.push(data)
        newComment.text = ''

        this.setState({comments: comments, newComment: newComment})
        // if error: show error
    }

    handleSongChange = (event) => {
        var {newSong} = this.state;
        newSong[event.target.name] = event.target.value
        this.setState({newSong: newSong})
    }

    handleSongSubmit = async () => {
        const {newSong} = this.state
        this.setState({loading: true})
        var request_data = {
            uri: newSong.uri,
            playlist_id: newSong.playlist_id
        }
        const {data} = await api.spotifySong.create(request_data, this.headers)

        if (data && data.id) {
            const url = new URL(window.location)
            var newUrl = `${url.origin}/api/v1/spotify_song/${data.id}/edit/`
            window.history.pushState({}, '', newUrl)

            newSong.uri = ''
            this.setState({song: data, newSong: newSong, loading: false})
        } else {
            // there was an error, wooooops
            this.setState({loading: false})
        }
    }

    render() {
        const {
            newComment,
            newSong,
            song,
            comments,
            playlistId,
            loading
        } = this.state

        return (
            <div>
                <SSHeader addType='spotify_song' playlistId={playlistId}></SSHeader>
                <div className='column twelve top-gap'></div>
                {(song && song.id) ? 
                    <SongDetail song={song}/> : 
                    <SongForm 
                        newSong={newSong}
                        handleSongChange={this.handleSongChange}
                        onSubmit={this.handleSongSubmit}
                        loading={loading}
                    />
                }
                {(song && song.id) ? 
                    <CommentsBlock 
                        comments={comments}
                        newComment={newComment}
                        parent={song}
                        handleCommentChange={this.handleCommentChange}
                        handleCommentSubmit={this.handleCommentSubmit}
                    /> : ''
                }
            </div>
        )
    }
}
    
export default SongView
