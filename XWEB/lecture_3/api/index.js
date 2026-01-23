const express = require('express');
const pool = require('./db');

const app = express();
app.use(express.json());
const PORT = process.env.PORT || 3000;


app.get('/get', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM userLog');
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: 'Chyba databáze', details: err.message });
  }
});

app.get('/get/:id', async (req, res) => {

  const userId = req.params.id;

  try {
    const [rows] = await pool.query('SELECT * FROM userLog WHERE id = ?', [userId]);

    if (rows.length === 0) {
      return res.status(404).json({ error: 'Uživatel nenalezen' });
    }
  
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: 'Chyba databáze', details: err.message });
  }
});


app.post('/post', async (req, res) => {
  const { name, lastname, email} = req.body;

  try {
    const [result] = await pool.query(
      'INSERT INTO userLog (name, lastname, email) VALUES (?, ?, ?)', 
      [name, lastname, email]
    );
    res.status(201).json({ id: result.insertId, name, lastname, email });
  } catch (err) {
    res.status(500).json({ error: 'Chyba při zápisu uživatele', details: err.message });
  }
});


app.post('/update/:id', async (req, res) => {
  const userId = req.params.id;
  const { name, lastname, email } = req.body;

  try {
    const [result] = await pool.query(
      'UPDATE userLog SET name = ?, lastname = ?, email = ? WHERE id = ?', 
      [name, lastname, email, userId]
    );

    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'Uživatel nenalezen' });
    }

    res.json({ id: userId, name, lastname, email });
  } catch (err) {
    res.status(500).json({ error: 'Chyba při aktualizaci uživatele', details: err.message });
  }
});

app.delete('/delete/:id', async (req, res) => {
  const userId = req.params.id;

  try {
    const [result] = await pool.query('DELETE FROM userLog WHERE id = ?', [userId]);

    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'Uživatel nenalezen' });
    }

    res.json({ message: 'Uživatel smazán' });
  } catch (err) {
    res.status(500).json({ error: 'Chyba při mazání uživatele', details: err.message });
  }
});

// pro docker i localhost nastavení
app.listen(PORT, '0.0.0.0', () => console.log(`API běží na portu ${PORT}`));