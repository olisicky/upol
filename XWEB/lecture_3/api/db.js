const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host: 'database',    // navazuje na compose service name
    user: 'test',
    password: 'heslo',    // normálně bych tahal z .env, ale pro jednoduchost to nechám tady
    database: 'moje_db',
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

module.exports = pool;