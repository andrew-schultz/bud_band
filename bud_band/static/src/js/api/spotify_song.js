import { api as request } from './api'

export default {
    get: song_id => request.get(`/spotify_song/${song_id}/`),
    create: (data, headers) => request.post(`/spotify_song/`, data, {headers: headers}),
    fetch: (params, headers) => request.get(`/spotify_song/list_api/`, {headers: headers, params: params} )
}