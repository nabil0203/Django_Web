function Map(){

    const my_projects = ['Taskify', 'ShopNest', 'EduStack', 'CarHub'];

    return(

        <div>
        {
            my_projects.map((project, index) => {
                    return <div>{project}</div>
                })
        }

        </div>

    )

}

export default Map