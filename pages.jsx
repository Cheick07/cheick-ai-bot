<<<<<<< HEAD
import React, { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    const data = {
      home_rank: 5,
      away_rank: 20,
      odds_home: 1.8,
      odds_draw: 3.2,
      odds_away: 4.5
    };
    const res = await axios.post("http://localhost:8000/predict", data);
    setResult(res.data);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Cheick AI Bot</h1>
      <button onClick={handlePredict} className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
        Prédire un match
      </button>
      {result && (
        <div className="mt-4">
          <p>Victoire domicile : {result.home_win}</p>
          <p>Nul : {result.draw}</p>
          <p>Victoire extérieur : {result.away_win}</p>
        </div>
      )}
    </div>
  );
}
=======
import React, { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    const data = {
      home_rank: 5,
      away_rank: 20,
      odds_home: 1.8,
      odds_draw: 3.2,
      odds_away: 4.5
    };
    const res = await axios.post("http://localhost:8000/predict", data);
    setResult(res.data);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Cheick AI Bot</h1>
      <button onClick={handlePredict} className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
        Prédire un match
      </button>
      {result && (
        <div className="mt-4">
          <p>Victoire domicile : {result.home_win}</p>
          <p>Nul : {result.draw}</p>
          <p>Victoire extérieur : {result.away_win}</p>
        </div>
      )}
    </div>
  );
}
>>>>>>> 9dc4bd644be0ed03501e8b7274f948aedbb1854b
