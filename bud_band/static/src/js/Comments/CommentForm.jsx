import * as React from 'react'

class CommentForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            comment_text: null,
        }
    }

    render() {
        const {
            parentId,
            parentType,
        } = this.props

        if (!this.props.comment) {
            return(<div></div>)
        }

        return (
            <div className='form'>
                hello comment form
                <input
                    type='text'
                    name='text'
                    defaultValue=''
                    onChange={this.props.textChangeHandler}
                //   value={}
                />
                <div className='submit' onClick={this.props.onSubmit}>Submit</div>
            </div>
        )
    }
}

export default CommentForm