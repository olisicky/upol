const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host: 'database',    // navazuje na compose service name
    user: 'test',
    password: 'heslo',
    database: 'moje_db',
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

module.exports = pool;