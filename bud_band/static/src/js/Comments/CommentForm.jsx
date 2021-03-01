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
            <div className='form comment'>
                <textarea 
                    name='text'
                    defaultValue={newComment.text}
                    onChange={this.props.textChangeHandler}
                    rows="4" 
                    cols="50"
                />
                <div className='submit-block'>
                    <div className='submit-gap'></div>
                    <div className='submit-button' onClick={this.props.onSubmit}>Submit</div>
                </div>
            </div>
        )
    }
}

export default CommentForm