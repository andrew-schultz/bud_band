import * as React from 'react'
import * as ReactDOM from 'react-dom'
import * as utils from '../../utils.jsx'
import api from '../../api'
import CommentsBlock from '../../Comments/CommentsBlock'


class SongView extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            id: this.props.song.id ? this.props.song.id : null,
            song: this.props.song ? this.props.song : {},
            modalOpen: false,
            newComment: {
                song_id: this.props.song.id,
                text: ''
            }
        }

        this.csrftoken = null;
    }

    componentDidMount() {
        this.csrftoken = utils.getCookie('csrftoken');
        this.headers = {
            'HTTP-X-CSRFToken': this.csrftoken,
            'X-CSRFToken': this.csrftoken
        }
    }

    handleCommentChange = (event) => {
        var comment = this.state.newComment
        // var field = event.target.name
        console.log(`field name from target ${event.target.name}`)
        comment[event.target.name] = event.target.value
        this.setState({newComment: comment})
    }

    handleCommentSubmit = async () => {
        const {comment} = this.state
        var request_data = {
            // do we need to break down the fiels?
            text: comment.text
        }
        const { ata} = await api.comments.create(request_data, this.headers)
        // if success: reload
        // if error: show error
    }

    handleSongChange = (event) => {
        var {song} = this.state;
        song[event.target.name] = event.target.value
        this.setState({song: song})
    }

    handleSongSubmit = async () => {
        const {song} = this.state
        var request_data = {
            uri: song.uri
        }
        const {data} = await api.spotifySong.create(request_data, this.headers)


        // update the url without reloading the page all the way?
        // window.history.pushState({"html":response.html,"pageTitle":response.pageTitle},"", urlPath);
    }

    render() {
        const {
            song,
            comments
        } = this.props

        const {
            newComment
        } = this.state
        console.log('hello newComment')
        debugger
        return (
            <CommentsBlock 
                comments={comments}
                newComment={newComment}
                parent={song}
                textChangehandler={this.handleCommentChange}
                handleCommentSubmit={this.handleCommentSubmit}
            />
        )
    }
}
    
export default SongView
