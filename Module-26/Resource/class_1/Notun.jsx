



function Notun() {
    const projects = ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'];
    return (
        <div>
            {
                projects.map((project, index) => {
                    return <div>{project}</div>;
                })
            }
        </div>
    )
}

export default Notun