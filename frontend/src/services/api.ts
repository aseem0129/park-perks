import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { User, ParkingSession, ParkingLot, BusinessSponsorship } from '../types';

const API_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use(async (config) => {
  const token = await AsyncStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth endpoints
export const auth = {
  login: async (email: string, password: string) => {
    const response = await api.post('/auth/login', { username: email, password });
    return response.data;
  },
  register: async (userData: Partial<User>) => {
    const response = await api.post('/auth/register', userData);
    return response.data;
  },
};

// Parking endpoints
export const parking = {
  getSessions: async () => {
    const response = await api.get('/parking/sessions');
    return response.data;
  },
  createSession: async (sessionData: Partial<ParkingSession>) => {
    const response = await api.post('/parking/sessions', sessionData);
    return response.data;
  },
  getSession: async (id: number) => {
    const response = await api.get(`/parking/sessions/${id}`);
    return response.data;
  },
  updateSession: async (id: number, sessionData: Partial<ParkingSession>) => {
    const response = await api.put(`/parking/sessions/${id}`, sessionData);
    return response.data;
  },
};

// Parking lot endpoints
export const parkingLots = {
  getLots: async () => {
    const response = await api.get('/parking/lots');
    return response.data;
  },
  getLot: async (id: number) => {
    const response = await api.get(`/parking/lots/${id}`);
    return response.data;
  },
};

// Business sponsorship endpoints
export const sponsorships = {
  getSponsorships: async () => {
    const response = await api.get('/sponsorships');
    return response.data;
  },
  getSponsorship: async (id: number) => {
    const response = await api.get(`/sponsorships/${id}`);
    return response.data;
  },
};

export default api; 