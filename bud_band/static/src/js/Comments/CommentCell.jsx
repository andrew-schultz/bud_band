import * as React from 'react'

class CommentCell extends React.Component {
    render() {
        const {
            comment,
        } = this.props

        if (!comment.id) {
            return <div></div>
        }

        let comment_date =  ''
        if (comment && comment.created_at) {
            const options = {
                year: 'numeric', month: 'numeric', day: 'numeric',
                hour: 'numeric', minute: 'numeric', second: 'numeric',
                // hour12: false,
                timeZone: 'America/New_York'
            };
            comment_date = new Intl.DateTimeFormat(
                "default", options).format(new Date(comment.created_at))}
        console.log(comment_date)

        return (
            <div className='comment-container'>
                <div className='column comment highlight-background inverse-shadow round-corners'>
                    <div className='comment-inner'>
                        <div className='byline'>
                            <p className='author'>{comment.user.username}</p>
                            <p className='timestamp'>{comment_date ? comment_date : ''}</p>
                        </div>
                        <div className='text'>
                            <p>{comment.text}</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default CommentCell
