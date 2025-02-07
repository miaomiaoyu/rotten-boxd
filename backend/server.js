require('dotenv').config();
const express = require('express');
const fetch = require('node-fetch');

const app = express();

// Middleware to parse JSON requests
app.use(express.json());

app.post('/api/search', async (req, res) => {
  const { movieName } = req.body;

  if (!movieName) {
    return res.status(400).json({ error: "Movie name is required" });
  }

  const apiKey = process.env.API_KEY;
  const apiUrl = `http://www.omdbapi.com/?apikey={apiKey}`;
  try {
    const apiResponse = await fetch(apiUrl);
    const data = await apiResponse.json();
    res.json(data);
  } catch (error) {
    console.error('API error:', error);
    res.status(500).json({ error: "Failed to fetch data" });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});