import axios from 'axios'

const apiBase = '/api/v1'

const apiConfig = {
  baseURL: apiBase,
}

export const api = axios.create(apiConfig)
