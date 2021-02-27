import * as React from 'react'
import { Z_FILTERED } from 'zlib'

class CommentCell extends React.Component {
    render() {
        const {
            comment,
        } = this.props

        return (
            <div className='comment'>
                <div className='byline'>
                    <p className='author'>{comment.user.username}</p>
                    <p className='timestamp'>{comment.created_at}</p>
                </div>
                <div class='text'>
                    <p>{comment.text}</p>
                </div>
            </div>
        )
    }
}

export default CommentCell
