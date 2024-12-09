import React, { useEffect, useState } from 'react';
import { getCourses } from '../services/apiService';

const CourseList = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    getCourses().then(data => setCourses(data));
  }, []);

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map(course => (
          <li key={course._id}>{course.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default CourseList;
