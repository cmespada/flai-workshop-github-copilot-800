import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME || 'localhost';
    const apiUrl = codespace !== 'localhost' 
      ? `https://${codespace}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';
    
    console.log('Fetching workouts from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Workouts</h2>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout, index) => (
            <div key={workout._id || index} className="col-md-6 mb-4">
              <div className="card shadow-sm">
                <div className="card-body">
                  <h5 className="card-title">{workout.workout_name}</h5>
                  <h6 className="card-subtitle mb-2 text-muted">{workout.category}</h6>
                  <p className="card-text">{workout.description}</p>
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                      <strong>Difficulty:</strong> <span className="badge bg-warning">{workout.difficulty_level}</span>
                    </li>
                    <li className="list-group-item">
                      <strong>Duration:</strong> {workout.estimated_duration_minutes} minutes
                    </li>
                    <li className="list-group-item">
                      <strong>Calories:</strong> {workout.estimated_calories} kcal
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <p className="text-center">No workouts found</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
