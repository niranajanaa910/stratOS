function ToolCard({ tools = [] }) {

  return (

    <div className="card">

      <h2 className="section-title">
        🛠 MCP Tools Used
      </h2>

      {tools.length === 0 ? (
        <p>No tools used.</p>
      ) : (
        <ul>
          {tools.map((tool, index) => (
            <li key={index} style={{ marginBottom: "10px" }}>
              ✅ {tool}
            </li>
          ))}
        </ul>
      )}

    </div>

  );

}

export default ToolCard;