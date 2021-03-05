import * as React from 'react'
import CommentCell from './CommentCell'
import CommentForm from './CommentForm'

const ConditionalComments = ({comments=[]}) =>{
    if (comments.length > 0) {
        return <div>{comments.map((comment, i) => (<CommentCell key={i} comment={comment} />))}</div>
    }

    return <div></div>
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
                <div className='column twelve ios-gap'></div>

                <div className='row'>
                    <div className='column three'></div>
                    <div className='column six'>
                        <CommentForm
                            type={parent.type}
                            newComment={newComment}
                            handleCommentChange={this.props.handleCommentChange}
                            onSubmit={this.props.handleCommentSubmit}
                        />
                    </div>
                    <div className='column three'></div>
                </div>

                <div className='row'>
                    <div className='column twelve'></div>
                </div>
                
                <div className='row'>
                    <div className='column three'></div>
                    <div className='column six'>
                        <ConditionalComments comments={comments} />
                    </div>
                    <div className='column three'></div>
                </div>
                
                <div className='row'>
                    <div className='column twelve empty bottom-gap-ios'></div>
                </div>
            </div>
        )
    }
}

export default CommentsBlock
