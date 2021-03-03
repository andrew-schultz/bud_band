import * as React from 'react'

class CommentForm extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        const {
            newComment
        } = this.props

        if (!newComment) {
            return(<div></div>)
        }

        return (
            <div className='comment-container'>
                <div className='form comment'>
                    <textarea 
                        className='comment-input'
                        name='text'
                        placeholder="Whatcha think?"
                        defaultValue={newComment.text}
                        onChange={this.props.textChangeHandler}
                        rows="4" 
                        cols="3"
                    />

                    <div className='column nine'></div>
                    <div className='column three'>
                        <div className='submit-button column content-block shadow clickable rectangle-bubble' onClick={this.props.onSubmit}>Submit</div>
                    </div>
                </div>
            </div>
        )
    }
}

export default CommentForm