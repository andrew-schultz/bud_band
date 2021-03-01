import * as React from 'react'
import CommentCell from './CommentCell'
import CommentForm from './CommentForm'

const ConditionalComments = ({comments=[]}) =>{
    if (comments.length > 0) {
        return <div>{comments.map((comment, i) => (<CommentCell key={i} comment={comment} />))}</div>
    }

    return <div>buttz</div>
}


class CommentsBlock extends React.Component {
    render() {
        const {
            comments,
            parent,
            newComment,
        } = this.props

        return (
            <div className="comments-block">
                <CommentForm
                    type={parent.type}
                    newComment={newComment}
                    textChangeHandler={this.props.textChangeHandler}
                    onSubmit={this.props.handleCommentSubmit}
                />
                <ConditionalComments comments={comments} />
            </div>
        )
    }
}

export default CommentsBlock
