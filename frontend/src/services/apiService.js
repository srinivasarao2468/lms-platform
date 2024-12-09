import axios from 'axios';

const API_URL = process.env.REACT_APP_BACKEND_URL;

export const getCourses = async () => {
  const response = await axios.get(`${API_URL}/courses`);
  return response.data;
};

export const createCourse = async (course) => {
  const response = await axios.post(`${API_URL}/courses`, course);
  return response.data;
};
