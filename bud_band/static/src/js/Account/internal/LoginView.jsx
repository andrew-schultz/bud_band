import * as React from 'react'
import * as ReactDOM from 'react-dom'
import * as utils from '../../utils.jsx'
import api from '../../api'


class LoginView extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            account: {
                username: '',
                password: ''
            },
            showError: false,
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

    handleFormChange = (event) => {
        var account = this.state.account
        account[event.target.name] = event.target.value
        this.setState({account: account})
    }

    handleSubmit = async () => {
        const {account, showError} = this.state
        var request_data = {
            username: account.username,
            password: account.password,
        }
        await api.account.login(request_data, this.headers).then( response => {
            const url = new URL(window.location)
            var newUrl = `${url.origin}/api/v1/spotify_song/list/?limit=100&offset=0`
            window.location.href = newUrl;
        }).catch(error => {
            this.setState({showError: true})
        })
    }

    render() {
        const {
            username,
            password,
            showError,
        } = this.state

        return (
            <div className='song-form-container'>
                <div className='song-form-inner-container'>
                    <div className='column three'></div>
                    <div className='column six'>
                        <div className='song-form-wrapper column content-block shadow'>
                            <div className='song-form-inner-wrapper'>
                                <div className='song-form-title'>
                                    <p className='top'>Login</p>
                                    {showError ? 
                                        <p className='error-login'>Ope! Something's off, try again plz</p>
                                        : ''}
                                </div>
                                <div className='form song'>
                                    <input
                                        className='song-input'
                                        type='text'
                                        name='username'
                                        placeholder='username'
                                        onChange={this.handleFormChange}
                                        value={username}
                                    />
                                </div>
                                <div className='form song'>
                                    <input
                                        className='song-input login'
                                        type='password'
                                        name='password'
                                        placeholder='password'
                                        onChange={this.handleFormChange}
                                        value={password}
                                    />
                                </div>
                                <div>
                                    <div className='column nine'></div>
                                    <div className='column three'>
                                        <div className='submit-button column content-block shadow clickable rectangle-bubble' onClick={this.handleSubmit}>Submit</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className='column three'></div>
                </div>
            </div>
        )
    }
}

export default LoginView
