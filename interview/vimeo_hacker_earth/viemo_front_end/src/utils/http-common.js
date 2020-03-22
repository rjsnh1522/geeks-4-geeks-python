import axios from 'axios'

export const API_BASE_URL = '//starlord.hackerearth.com/'

export const http = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json'
    }
})

export default http
