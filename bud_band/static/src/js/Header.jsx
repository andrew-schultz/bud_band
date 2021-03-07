import * as React from 'react'

class SSHeader extends React.Component {
    constructor(props) {
        super(props)
    }

    handleBack = () => {
        window.history.back();
    }

    handleAdd = () => {
        const url = new URL(window.location)
        var newUrl = `${url.origin}/api/v1/spotify_song/create/`
        window.location.href = newUrl;
    }

    handleHome = () => {
        const url = new URL(window.location)
        var newUrl = `${url.origin}/api/v1/spotify_song/list/?limit=10&offset=0`
        window.location.href = newUrl;
    }

    render() {
        return (
            <div className='column twelve'>
                <div className='header-container'>
                    <div className='button-wrapper'>
                        <div className='back-button-inner column shadow clickable' onClick={this.handleBack}>
                            <p>&#8249;</p>
                        </div>
                        <p className='site-title' onClick={this.handleHome}>BudBand</p>
                        <div className='add-button-inner column shadow clickable' onClick={this.handleAdd}>
                            <p>&#43;</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default SSHeader