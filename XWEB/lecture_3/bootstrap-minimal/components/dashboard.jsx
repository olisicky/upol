function Dashboard() {

    // Připravím si proměnné, které se mi budou měnit případně podle uživatelského vstupu
    // dvojice proměnná + funkce pro změnu proměnné
    const [data, setData] = React.useState();
    const [nRows, setNRows] = React.useState(10);
    const [deleteId, setDeleteId] = React.useState(null);
    // funkce, která se zavolá při změně inputu (podle nastavené hodnoty v inputu)
    const handleChange = (event) => {
        setNRows(event.target.value);
    };
        
    React.useEffect(() => {
        // posílám GET, který zpracovávám v handleGet u Controlleru
        fetch(`/dashboard?limit=${nRows}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        })
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error fetching dashboard data:', error));
        }, [nRows]);    // závislist pro vykreslení - když se změní nRows, znovu se zavolá useEffect
    
    React.useEffect(() => {
        if (deleteId !== null) {
            fetch(`/users/deleteLog/${encodeURIComponent(deleteId)}`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (response.ok) {
                    // po úspěšném smazání znovu načtu data
                    fetch(`/dashboard?limit=${nRows}`, {
                        method: 'GET',
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest'
                        },
                    })
                        .then(response => response.json())
                        .then(data => setData(data))
                        .catch(error => console.error('Error fetching dashboard data:', error));
                }
                else {
                    console.error('Chyba při mazání uživatele.');
                }
            });
        }
    }, [deleteId, nRows]);

    return (
        <div>
            <p>Welcome to the dashboard! </p>
            <input
                type="number"
                placeholder="Počet řádků"
                value={nRows} 
                onChange={handleChange} 
            />
            <table className="table">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">When logged in</th>
                    <th scope="col">Delete log</th>
                    </tr>
                </thead>
                <tbody>
                    {data && data.length > 0 ? (
                        data.map((user, index) => (
                            <tr key={index}>
                                <th scope="row">{index + 1}</th>
                                <td>{user.name}</td>
                                <td>{user.lastname}</td>
                                <td>{user.email}</td>
                                <td>{user.timestamp}</td>
                                <td>
                                    <button className="btn btn-danger btn-sm delete_button" data-id={user.id} onClick={() => setDeleteId(user.id)}>
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))
                    ) : (
                    <tr>
                        <td colSpan="6" className="text-center">No users found</td>
                    </tr>
                    )}
                </tbody>
            </table>

        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('react-dashboard'));
root.render(<Dashboard />);