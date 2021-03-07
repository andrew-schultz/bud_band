import * as React from 'react'
import * as ReactDOM from 'react-dom'
import LoginView from './internal/LoginView'

class AccountLogin {
    constructor() {
        this.init()
    }

    init = () => {
        const elem = document.getElementById('AccountLogin')
        if (elem === undefined) return


        const session = React.createElement(LoginView, {})

        ReactDOM.render(session, elem)
    }
}

export default AccountLogin
