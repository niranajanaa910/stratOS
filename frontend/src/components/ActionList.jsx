function ActionList({ actions = [] }) {

    return (

        <div className="card">

            <h2 className="section-title">
                ✅ Recommended Actions
            </h2>

            <ul>

                {actions.length === 0 ? (

                    <li>No actions available.</li>

                ) : (

                    actions.map((action, index) => (

                        <li
                            key={index}
                            style={{marginBottom:"10px"}}
                        >

                            {action}

                        </li>

                    ))

                )}

            </ul>

        </div>

    );

}

export default ActionList;