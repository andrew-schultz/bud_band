import * as React from 'react'
import CommentCell from './CommentCell'
import CommentForm from './CommentForm'


class CommentsBlock extends React.Component {
    render() {
        const {
            comments,
            parent,
        } = this.props

        return (
            <div className="commentsBlock">
                hello comments
                <CommentForm
                    type={parent.type}
                    textChangeHandler={this.props.textChangeHandler}
                    onSubmit={this.props.handleCommentSubmit}
                />
                {comments.map((comment, i) => {
                    <CommentCell
                        key={i}
                        comment={comment}
                    />
                })}
            </div>
        )
    }
}

export default CommentsBlock
