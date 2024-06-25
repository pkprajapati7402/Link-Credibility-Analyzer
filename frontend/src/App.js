import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/analyze', { url });
      setResult(response.data);
    } catch (error) {
      console.error('Error analyzing URL:', error);
      setResult({ error: 'Failed to analyze URL' });
    }
  };

  return (
    <div className="App">
      <h1>Link Safety and Credibility Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={url} 
          onChange={(e) => setUrl(e.target.value)} 
          placeholder="Enter URL" 
          required
        />
        <button type="submit">Analyze</button>
      </form>
      {result && (
        <div className={`result ${result.status}`}>
          {result.error ? (
            <p>{result.error}</p>
          ) : (
            <>
              <p>Score: {result.score}%</p>
              <p>Status: {result.status}</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
