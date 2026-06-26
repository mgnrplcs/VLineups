import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

if (!API_BASE_URL && import.meta.env.PROD) {
  throw new Error('🔑 VITE_API_BASE_URL is required.')
}

const apiClient = axios.create({
  baseURL: API_BASE_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient