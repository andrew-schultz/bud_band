import { api as request } from './api'

export default {
    get: id => request.get(`/comment/${id}/`),
    create: (data, headers) => request.post(`/comment/`, data, {headers: headers}),
}