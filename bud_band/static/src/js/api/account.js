import { api as request } from './api'

export default {
    login: (data, headers) => request.post(`/account/login_token/`, data, {headers: headers}),
}